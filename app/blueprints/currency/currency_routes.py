"""Routes for currency pages."""
from flask import Blueprint, render_template


currency_bp = Blueprint(
    'currency_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@currency_bp.route('/', methods=['GET'])
def home():
    """Homepage route."""
    return render_template(
        'index.jinja2',
        title='Currencies | Partner app',
        template='home-static main',
        body="Home"
    )