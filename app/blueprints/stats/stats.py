from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user
from sqlalchemy import desc

from ..transactions.models import Transaction, db


# Blueprint Configuration
stats_bp = Blueprint(
    "stats_bp", __name__, template_folder="templates", static_folder="static"
)


@stats_bp.route("/stats", methods=["GET"])
@login_required
def stats():
    return render_template(
        'stats.jinja2',
        transactions=Transaction.query.order_by( desc(Transaction.date) ).all(),
        title="Statistics | Partner app"
    )
