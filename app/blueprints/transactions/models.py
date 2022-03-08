from sqlalchemy import ForeignKey
from ..auth.models import User
from ... import db


class Transaction(db.Model):
    """Model for transactions."""

    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.Enum('clothes','food','cosmetics','fun','kids','salary','other'), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey(User.id), nullable=False)
    currency = db.Column(db.String(3), nullable=False, unique=False)
    total = db.Column(db.Numeric(8,2), nullable=False, unique=False)
    note = db.Column(db.String(255), nullable=False, unique=False)

    user = db.relationship('User', foreign_keys='Transaction.user_id')

    def set_user_id(self, user_id):
        """Create hashed password."""
        self.user_id = user_id