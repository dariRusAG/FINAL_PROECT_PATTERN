import pandas


# Создаем таблицу для сравнения
def get_list_compare(conn, pattern_list):
    return pandas.read_sql(f'''
    WITH get_measure(detail_id, measure_full_name)
    AS(
        SELECT detail_id, group_concat(measure_full_name, ', ')
        FROM detail_measure 
        JOIN measure USING (measure_id)
        GROUP BY detail_id
    )
    SELECT
        pattern_id AS ID,
        pattern_name AS Название, 
        category_name AS Категория,
        COUNT(detail_id) AS amount,
        group_concat(measure_full_name, ', ') AS Мерки
    FROM pattern
    JOIN category USING (category_id)
    JOIN pattern_detail USING (pattern_id)
    JOIN detail USING (detail_id)
    JOIN get_measure USING (detail_id)
    WHERE pattern_id IN ({str(pattern_list).strip('[]')}) OR {not pattern_list}
    GROUP BY pattern_id
    ORDER BY pattern_name
    ''', conn)


# Выводим количество деталей у каждой выкройки
def get_detail(conn):
    return pandas.read_sql(f'''
    SELECT 
        pattern_id,
        COUNT(detail_id) AS amount
    FROM pattern_detail
    GROUP BY pattern_id
    ''', conn)
