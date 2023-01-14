from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.scheme_model import *
from controllers.functions import *
from models.compare_model import *


@app.route('/scheme', methods=['get', 'post'])
def scheme():
    conn = get_db_connection()

    session['user_id'] = 1

    user_measure = []
    df_data_pattern = []
    error_param = []

    pattern_id = request.values.get('pattern')
    cat = request.form.getlist('cat')
    detail_start = request.values.get('detail_start')
    detail_end = request.values.get('detail_end')
    pat = request.values.get('pattern')

    df_measure = get_measure(conn, pattern_id)
    df_param_user = get_param_user(conn, session['user_id'])
    measure_name = int_list(str(df_measure.loc[0, "measure_name"]).split(","))
    measure_full_name = int_list(str(df_measure.loc[0, "measure_full_name"]).split(","))
    pattern_name = get_pattern_name(conn, pattern_id)

    # Если нажата кнопка "Построить" со страницы схемы
    if request.values.get('build_scheme'):
        user_measure = request.form.getlist('measure')

        for elem in range(len(user_measure)):
            if user_measure[elem].isdigit() is True:
                if measure_name[elem] == 'ВБ':
                    if 20 > int(user_measure[elem]) or int(user_measure[elem]) > 25:
                        error_param.append(elem)
                elif measure_name[elem] == 'ОБ':
                    if 70 > int(user_measure[elem]) or int(user_measure[elem]) > 130:
                        error_param.append(elem)
                elif measure_name[elem] == 'ДИ':
                    if 30 > int(user_measure[elem]) or int(user_measure[elem]) > 120:
                        error_param.append(elem)
                elif measure_name[elem] == 'ОТ':
                    if 40 > int(user_measure[elem]) or int(user_measure[elem]) > 100:
                        error_param.append(elem)
            else:
                error_param.append(elem)

        if not error_param:
            df_data_pattern = get_data_pattern(conn, pattern_id)

    # Если нажата кнопка "Сравнить" со страницы поиска
    elif request.values.get('compare'):
        pattern_list = request.values.getlist('pattern_list')
        df_compare = get_list_compare(conn, pattern_list)

        html = render_template(
            'compare.html',
            pattern_list=pattern_list,
            df_compare=df_compare,
            len=len,
            str=str,
            int_list=int_list,
            cat=cat,
            detail_start=detail_start,
            detail_end=detail_end,
            pat=pat
        )

        return html

    html = render_template(
        'scheme.html',
        pattern_id=pattern_id,
        pattern=df_data_pattern,
        pattern_name=pattern_name,
        measure_name=measure_name,
        measure_full_name=measure_full_name,
        param_user=df_param_user,
        user_measure=user_measure,
        len=len,
        zip=zip,
        error_param=error_param,
        cat=cat,
        detail_start=detail_start,
        detail_end=detail_end,
        pat=pat,
        int=int
    )
    return html
