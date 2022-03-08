"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length


class NewTransaction(FlaskForm):
    """User Sign-up Form."""
    date = DateField('Transaction date')
    type = SelectField(
        'Transaction type',
        [DataRequired()],
        choices=[
            ('Clothes', 'clothes'),
            ('Food', 'food'),
            ('Cosmetics', 'cosmetics'),
            ('Fun', 'fun'),
            ('Kids', 'kids'),
            ('Salary', 'salary'),
            ('Other', 'other')
        ]
    )
    currency = StringField(
        "Currency code", 
        validators=[
            DataRequired(),
            Length(min=3, max=3, message="Code must be exactly 3 letters long")
        ]
    )
    total = StringField("Total", validators=[DataRequired()])
    note = total = StringField("Total", validators=[DataRequired()])
    submit = SubmitField("Transfer")