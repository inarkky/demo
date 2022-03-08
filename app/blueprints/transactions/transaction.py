from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user

from ...auth import login_manager
from ...assets import compile_auth_assets
from .forms import NewTransaction
from .models import Transaction, db


# Blueprint Configuration
transaction_bp = Blueprint(
    "transaction_bp", __name__, template_folder="templates", static_folder="static"
)


@transaction_bp.route("/transaction/new", methods=["GET", "POST"])
@login_required
def new():
    return

@transaction_bp.route("/transaction/list", methods=["GET", "POST"])
@login_required
def list():
    return