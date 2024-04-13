from flask_wtf import CSRFProtect, FlaskForm
from wtforms import StringField, SubmitField, ValidationError, validators

csrf = CSRFProtect()


class SearchForm(FlaskForm):
  query_str = StringField("Query", [validators.DataRequired("Please enter the search term")])
  submit = SubmitField("Search")
