from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.personal_model import *


@app.route('/personal', methods=['get', 'post'])
def personal():
    conn = get_db_connection()
    session['user_id'] = 1
    error_param = []

    # Если нажата кнопка "Сохранить изменения"
    if request.values.get('save'):
        new_data_user = request.form.getlist('data_user')
        update_data_user(conn, session['user_id'], new_data_user)

        new_param_user = request.form.getlist('param_user')

        for elem in range(len(new_param_user)):
            if (new_param_user[elem].isdigit() is True) or (new_param_user[elem] == ''):
                update_param_user(conn, session['user_id'], elem, new_param_user)
                error_param.append('q')
            else:
                error_param.append(new_param_user[elem])

    df_data_user = get_data_user(conn, session['user_id'])
    df_param_user = get_param_user(conn, session['user_id'])

    html = render_template(
        'personal.html',
        user=session['user_id'],
        data_user=df_data_user,
        param_user=df_param_user,
        error_param=error_param,
        len=len)

    return html
