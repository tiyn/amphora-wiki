from flask_wtf import FlaskForm
from flask_wtf import CSRFProtect
from wtforms import TextField, SubmitField, ValidationError, validators

csrf = CSRFProtect()


class SearchForm(FlaskForm):
    query_str = TextField(
        "Query", [validators.Required("Please enter the search term")])
    submit = SubmitField("Send")
