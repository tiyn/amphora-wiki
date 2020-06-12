import os
from flask import Flask, flash, make_response, render_template, request, redirect, abort

import content as cont
import config
import search as src
from forms import SearchForm, csrf

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.secret_key = SECRET_KEY
csrf.init_app(app)

TITLE = config.TITLE
STYLE = config.STYLE


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', title=TITLE, errorcode='404', style=STYLE), 404


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title=TITLE, style=STYLE), 200


@app.route('/search', methods=['GET', 'POST'])
@app.route('/search.html', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == 'POST':
        query_str = request.form['query_str']
        content = cont.gen_query_res_string(query_str)
        return render_template('search.html', title=TITLE, style=STYLE, form=form, content=content), 200
    return render_template('search.html', title=TITLE, style=STYLE, form=form, content=''), 200


@app.route('/entry/<path:fullurl>')
def entry(fullurl):
    content = cont.gen_stand_string(fullurl)
    return render_template('entry.html', title=TITLE, style=STYLE, content=content), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
