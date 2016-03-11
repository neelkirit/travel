__author__ = 'nk'

from functools import wraps

from flask import session, url_for, flash
from flask import redirect


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('index'))

    return wrap

