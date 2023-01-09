import sqlite3
con = sqlite3.connect("DB.sqlite")

con.executescript('''
CREATE TABLE IF NOT EXISTS category (
 category_id INTEGER PRIMARY KEY AUTOINCREMENT,
 category_name VARCHAR(30)
);

INSERT INTO category (category_name)
VALUES
('Брюки'),
('Платья'),
('Рубашки'),
('Футболки'),
('Юбки');


CREATE TABLE IF NOT EXISTS pattern (
 pattern_id INTEGER PRIMARY KEY AUTOINCREMENT,
 pattern_name VARCHAR(70),
 category_id INTEGER,
 FOREIGN KEY (category_id) REFERENCES category (category_id) ON DELETE CASCADE
);

INSERT INTO pattern (pattern_name, category_id)
VALUES
('Футболка поло', 4),
('Футболка Дженни', 4),
('Классическая футболка', 4),
('Классическая рубашка', 3),
('Пляжная рубашка', 3),
('Юбка-карандаш', 5),
('Юбка-солнце', 5),
('Классические брюки', 1),
('Брюки бананы', 1),
('Брюки скинни', 1),
('Брюки карго', 1), 
('Платье-футляр', 2);


CREATE TABLE IF NOT EXISTS detail (
 detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
 detail_name VARCHAR(50)
);

INSERT INTO detail (detail_name)
VALUES
('Рукав футболки'),
('Перед футболки'),
('Спинка футболки'),
('Одношовный рукав'),
('Воротник-стойка'),
('Манжеты'),
('Перед рубашки'),
('Спинка рубашки'),
('Полочка рубашки'),
('Передняя часть юбки'),
('Задняя часть юбки'),
('Основа для солнца'),
('Основа для брюк'),
('Передняя часть брюк'),
('Пояс для брюк'),
('Задняя часть брюк'),
('Деталь 1'),
('Деталь 2'),
('Деталь 3'),
('Деталь 4');


CREATE TABLE IF NOT EXISTS pattern_detail (
 pattern_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
 pattern_id INTEGER,
 detail_id INTEGER,
 FOREIGN KEY (pattern_id) REFERENCES pattern (pattern_id) ON DELETE CASCADE,
 FOREIGN KEY (detail_id) REFERENCES detail (detail_id) ON DELETE CASCADE
);

INSERT INTO pattern_detail (pattern_id, detail_id)
VALUES
(1, 1), (1, 2), (1, 3),
(2, 1), (2, 2), (2, 3),
(3, 1), (3, 2), (3, 3),
(4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),
(5, 7), (5, 8),
(6, 10), (6, 11),
(7, 12),
(8, 13),
(9, 14), (9, 15),
(10, 14), (10, 15),
(11, 14), (11, 15), (11, 16),
(12, 17), (12, 18), (12, 19), (12, 20);


CREATE TABLE IF NOT EXISTS measure (
 measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
 measure_name VARCHAR(10),
 measure_full_name VARCHAR(50)
);

INSERT INTO measure (measure_name, measure_full_name)
VALUES
('ОПл', 'Обхват плеча'),
('ОТ', 'Обхват талии'),
('ОБ', 'Обхват бедер'),
('ОШ', 'Обхват шеи'),
('ДР', 'Длина рукава'),
('ДПдТ', 'Длина переда до талии'),
('ДСдТ', 'Длина спины до талии'), 
('ДИпС', 'Длина изделия по спинке'),
('ДПл', 'Длина плеча'),
('ШПр', 'Ширина проймы'),
('ШС', 'Ширина спины'),
('ШГ', 'Ширина груди'),
('ВПлПК', 'Высота плеча переда косая'),
('ВПлК', 'Высота плеча косая'),
('ГП', 'Глубина проймы'),
('ОЗ', 'Обхват запястья'),
('ОГ', 'Длина горловины'),
('ВБ', 'Высота бедер'),
('ДИ', 'Длина изделия'),
('ВГ', 'Высота груди');

CREATE TABLE IF NOT EXISTS detail_measure (
 detail_measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
 detail_id INTEGER,
 measure_id INTEGER,
 FOREIGN KEY (detail_id) REFERENCES detail (detail_id) ON DELETE CASCADE,
 FOREIGN KEY (measure_id) REFERENCES measure (measure_id) ON DELETE CASCADE
);

INSERT INTO detail_measure (detail_id, measure_id)
VALUES
(1, 1), (1, 5),
(2, 4), (2, 9), (2, 13), (2, 10), (2, 12), (2, 6), (2, 2), (2, 3),
(3, 4), (3, 9), (3, 14), (3, 10), (3, 11), (3, 2), (3, 3), (3, 15), (3, 7), (3, 8),
(4, 5), (4, 1), (4, 15),
(5, 17),
(6, 16),
(7, 15), (7, 18), (7, 7), (7, 10), (7, 11), (7, 19), (7, 12),
(8, 4), (8, 14), (8, 9),
(9, 6), (9, 4), (9, 20), (9, 12), (9, 13), (9, 9),
(10, 2), (10, 3), (10, 18), (10, 19),
(11, 2), (11, 3), (11, 18), (11, 19),
(12, 2), (12, 19),
(13, 3), (13, 18), (13, 19),
(14, 3), (14, 18), (14, 19),
(15, 2),
(16, 3), (16, 18), (16, 19),
(17, 1), (17, 2), (17, 5), (17, 8), (17, 10), (17, 12),
(18, 1), (18, 4), (18, 7), (18, 10), (18, 11), (18, 12), (18, 13), (18, 15), (18, 16), (18, 17), (18, 18), (18, 19),
(19, 1), (19, 4), (19, 6), (19, 8), (19, 9), (19, 10), (19, 13), (19, 14), (19, 16), (19, 18), (19, 19), (19, 20),
(20, 1), (20, 7);


CREATE TABLE IF NOT EXISTS users (
 users_id INTEGER PRIMARY KEY AUTOINCREMENT,
 users_login VARCHAR(30),
 users_password VARCHAR(30)
);

INSERT INTO users (users_login, users_password)
VALUES
('srf_adlr','qwertyasdfg');


CREATE TABLE IF NOT EXISTS param (
 param_id INTEGER PRIMARY KEY AUTOINCREMENT,
 param_name VARCHAR(10),
 param_full_name VARCHAR(50),
 param_value INTEGER
);

INSERT INTO param (param_name, param_full_name)
VALUES
('ОПл', 'Обхват плеча'),
('ОТ', 'Обхват талии'),
('ОБ', 'Обхват бедер'),
('ОШ', 'Обхват шеи'),
('ДПдТ', 'Длина переда до талии'),
('ДСдТ', 'Длина спины до талии'), 
('ДПл', 'Длина плеча'),
('ШПр', 'Ширина проймы'),
('ШС', 'Ширина спины'),
('ШГ', 'Ширина груди'),
('ВПлПК', 'Высота плеча переда косая'),
('ВПлК', 'Высота плеча косая'),
('ОЗ', 'Обхват запястья'),
('ВБ', 'Высота бедер'),
('ВГ', 'Высота груди');


CREATE TABLE IF NOT EXISTS user_param (
 user_param_id INTEGER PRIMARY KEY AUTOINCREMENT,
 param_value INTEGER,
 user_id INTEGER,
 param_id INTEGER,
 FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
 FOREIGN KEY (param_id) REFERENCES param (param_id) ON DELETE CASCADE
);

INSERT INTO user_param (user_id, param_id, param_value)
VALUES
(1, 1, 28), (1, 2, 68), (1, 3, 94), (1, 4, 23), (1, 5, 48), 
(1, 6, 72), (1, 7, 75), (1, 8, 80), (1, 9, 56), (1, 10, 103), 
(1, 11, 132), (1, 12, 88), (1, 13, 97), (1, 14, 48), (1, 15, 14);
''')

# сохраняем информацию в базе данных
con.commit()
