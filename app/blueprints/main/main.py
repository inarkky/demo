"""Routes for currency pages."""
from flask import Blueprint
from flask import current_app as app
from flask import redirect, render_template, session, url_for
from flask_login import current_user, login_required, logout_user

from ...assets import compile_auth_assets


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
    session["redis_test"] = "This is a session variable."
    return render_template(
        'index.jinja2',
        title='Home | Partner app',
        template='home-static main',
        body="Home"
    )


@main_bp.route("/session", methods=["GET"])
@login_required
def session_view():
    """Display session variable value."""
    return render_template(
        "session.jinja2",
        title="Session | Partner app",
        template="dashboard-template",
        session_variable=str(session["redis_test"]),
    )


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))