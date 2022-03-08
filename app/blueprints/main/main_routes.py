"""Routes for currency pages."""
from flask import Blueprint, render_template


main_bp = Blueprint(
    'main_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=['GET'])
def home():
    """Homepage route."""
    return render_template(
        'index.jinja2',
        title='Home | Partner app',
        template='home-static main',
        body="Home"
    )