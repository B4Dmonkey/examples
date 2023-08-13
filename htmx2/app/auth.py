import functools
from flask import request, Blueprint, render_template, g, redirect, url_for

bp = Blueprint('auth', __name__, url_prefix='/auth')

# ? not sure if this is the correct way to do this
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect('/')

        return view(**kwargs)

    return wrapped_view

@bp.route('/submit_phone', methods=['POST'])
def submit_phone():
    phone = request.form['phone']
    if len(phone) > 3:
        return render_template('auth/login.html')
    return render_template('auth/join_wait_list.html')
