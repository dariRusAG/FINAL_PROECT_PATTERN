import pandas


# Выводим данные выкройки
def get_data_pattern(conn, pattern_id):
    return pandas.read_sql(f'''
    SELECT
        pattern_name AS Название, 
        category_name AS Категория
    FROM pattern
    JOIN category USING (category_id)
    WHERE pattern_id == {pattern_id}
    ''', conn)


# Выводим мерки выкройки
def get_measure(conn, pattern_id):
    return pandas.read_sql(f'''
    WITH get_all_measure(detail_id, measure_name, measure_full_name)
    AS (
        SELECT 
            detail_id, 
            group_concat(measure_name, ', ') AS measure_name,
            group_concat(measure_full_name, ', ') AS measure_full_name
        FROM detail_measure 
        JOIN measure USING (measure_id)
        GROUP BY detail_id
    )
    SELECT 
        group_concat(measure_full_name, ', ') AS measure_full_name,
        group_concat(measure_name, ', ') AS measure_name
    FROM pattern_detail 
    JOIN get_all_measure USING (detail_id) 
    WHERE pattern_id == {pattern_id}
    ''', conn)


# Выводим параметры пользователя
def get_param_user(conn, user_id):
    return pandas.read_sql(f'''
    SELECT 
        param_name, 
        user_param.[param_value] AS user_param
    FROM param 
    INNER JOIN user_param ON param.param_id = user_param.param_id
    WHERE user_id = {user_id} AND user_param != ''
    ''', conn)


# Вывести название выкройки
def get_pattern_name(conn, pattern_id):
    return pandas.read_sql(f'''
    SELECT pattern_name
    FROM pattern
    WHERE pattern_id == {pattern_id}
    ''', conn).values[0][0]


