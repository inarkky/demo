from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user

from ..transactions.models import Transaction


# Blueprint Configuration
stats_bp = Blueprint(
    "stats_bp", __name__, template_folder="templates", static_folder="static"
)


@stats_bp.route("/stats", methods=["GET"])
@login_required
def stats():
    by_currency = Transaction.get_sum_by_currency()
    by_type = Transaction.get_sum_by_type()
    all_types = Transaction.get_all_types()
    return render_template(
        'stats.jinja2',
        transactions_by_currency = by_currency,
        transactions_by_type = by_type,
        types = all_types,
        title="Statistics | Partner app"
    )
