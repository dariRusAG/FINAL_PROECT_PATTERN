from app import app
from flask import render_template, request
from utils import get_db_connection
from models.compare_model import *
from controllers.functions import *


@app.route('/compare', methods=['get', 'post'])
def compare():
    conn = get_db_connection()

    pattern_list = request.values.getlist('pattern_list')
    df_compare = get_list_compare(conn, pattern_list)

    html = render_template(
        'compare.html',
        pattern_list=pattern_list,
        df_compare=df_compare,
        len=len,
        str=str,
        int_list=int_list
    )

    return html
