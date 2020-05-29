from flask import Flask, flash, make_response, render_template, request, redirect, abort

import content as con_gen
import config


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', title=config.TITLE, errorcode='404', style=config.STYLE), 404


@app.route('/')
@app.route('/index.html')
def index():
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
