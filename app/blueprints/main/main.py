"""Routes for currency pages."""
import requests
from decimal import Decimal, getcontext
from flask import Blueprint
from flask import current_app as app
from flask import redirect, render_template, session, url_for
from flask_login import current_user, login_required, logout_user

from ...assets import compile_auth_assets
from ..transactions.models import Transaction


main_bp = Blueprint(
    'main_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route("/", methods=["GET"])
@login_required
def home():
    """Homepage route."""
    balances = Transaction.get_all_balances()
    exchange_data = fetch_exchange_rates()
    exchanged_balances = {}
    exchanged_total = 0
    getcontext().prec = 10
    
    
    for balance in balances:

        translated = translate_currency(balance.currency, exchange_data)
        exchanged_balances[balance.currency] = Decimal(balance.total) * Decimal(translated)
        exchanged_total += exchanged_balances[balance.currency] 

    return render_template(
        'index.jinja2',
        balances = balances,
        exchanged_balances = exchanged_balances,
        exchanged_total = exchanged_total,
        title = 'Home | Partner app',
        template = 'home-static main',
        body = "Home"
    )


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))


def fetch_exchange_rates():
    exchange_rates = requests.get("https://api.hnb.hr/tecajn/v2")
    return exchange_rates.json()

def translate_currency(currency, data):
    if currency != "HRK":
        x = list(filter(lambda x:x["valuta"]==str(currency), data))
        translated = x[0]["srednji_tecaj"].replace(',', '.')
    else:
        translated = 1
    
    return Decimal(translated)