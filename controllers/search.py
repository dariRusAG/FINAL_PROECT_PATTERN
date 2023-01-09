from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.search_model import *
from controllers.functions import *


@app.route('/', methods=['get', 'post'])
def search():
    conn = get_db_connection()

    df_category = get_category(conn)
    max_detail = max(get_detail(conn)['amount']) + 1
    min_detail = min(get_detail(conn)['amount'])

    pattern_list = request.form.getlist('pattern_list')
    cat = request.form.getlist('cat')
    pat = request.values.getlist('pat')

    # Если нажата кнопка "Найти"
    if request.values.get('search'):
        category = request.form.getlist('category')
        detail_start = request.values.get('int_start')
        detail_end = request.values.get('int_end')

        if detail_start == "" or detail_start.isdigit() is False:
            detail_start = min_detail
        if detail_end == "" or detail_end.isdigit() is False:
            detail_end = max_detail

        detail_start = int(detail_start)
        detail_end = int(detail_end)
        if detail_end > max_detail:
            detail_end = max_detail
        number_details = list(range(detail_start, detail_end))
        pat = 'q'

    # Если нажата кнопка "Вернуться на страницу поиска" со страницы сравнить или схемы
    elif request.values.get('search_h'):
        pat = int(request.values.get('pat'))
        category = cat
        detail_start = request.values.get('detail_start')
        detail_end = request.values.get('detail_end')
        number_details = list(range(int(detail_start), int(detail_end)))

    # Если нажата кнопка "Очистить" или вход на сайт впервые
    else:
        category = []
        detail_start = min_detail
        detail_end = max_detail
        number_details = list(range(min_detail, max_detail))
        pat = 'q'

    df_pattern = get_pattern(conn, category, number_details)

    html = render_template(
        'search.html',
        category=df_category,
        choice=category,
        pattern=df_pattern,
        detail_start=detail_start,
        detail_end=detail_end,
        max_detail=max_detail,
        min_detail=min_detail,
        len=len,
        str=str,
        int_list=int_list,
        pattern_list=pattern_list,
        cat=cat,
        pat=pat
    )
    return html
