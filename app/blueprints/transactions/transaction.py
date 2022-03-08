from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user

from .forms import NewTransaction
from .models import Transaction, db


# Blueprint Configuration
transaction_bp = Blueprint(
    "transaction_bp", __name__, template_folder="templates", static_folder="static"
)


@transaction_bp.route("/transaction/new", methods=["GET", "POST"])
@login_required
def new():
    """
    Log-in page for registered users.
    GET: Serve new transaction form page.
    POST: Validate form and redirect user to all transactions.
    """
    form = NewTransaction()
    if form.validate_on_submit():
        transaction = Transaction(
            date=form.date.data, 
            type=form.type.data,
            currency=form.currency.data,
            total=form.total.data,
            note=form.note.data
        )
        transaction.set_user_id(current_user.get_id())
        db.session.add(transaction)
        db.session.commit()  # Save new transaction
        return redirect(url_for("main_bp.home"))
    return render_template(
        "new.jinja2",
        form=form,
        title="New | Partner app.",
        template="newtransaction-page",
        body="New transaction.",
    )

@transaction_bp.route("/transaction/list", methods=["GET"])
@login_required
def list():
    return