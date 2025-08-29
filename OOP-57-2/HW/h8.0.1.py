import sqlite3


connect = sqlite3.connect("users2.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCHAR(100) NOT NULL,
        grade INTEGER NOT NULL,
        userid INTEGER,
        FOREIGN KEY (userid) REFERENCES users(user_id)
    )
''')
connect.commit()


def add_user(name: str, age: int):
    cursor.execute(
        'INSERT INTO users(name, age) VALUES (?,?)',
        (name, age)
    )
    connect.commit()
    print(f"{name} - Добавили")

add_user("user", 14)
add_user("user2", 19)
add_user("user3", 22)
add_user("user4", 33)



def add_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id, subject, grade)
    )
    connect.commit()
    print("Оценка за урок добавлена!!")



def get_user_and_grade():
    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade
        FROM users
        FULL OUTER JOIN grades ON users.user_id = grades.userid
    ''')
    users = cursor.fetchall()
    for i in users:
        print(f"name: {i[0]}, subject: {i[1]}, grade: {i[2]}")

# add_grade(0,"math", 5)
# add_grade(1,"math", 5)
add_grade(2,"math", 5)
add_grade(3,"physics", 4)
add_grade(4,"programming", 2)

def create_view_test():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS view_test AS
        SELECT users.name, users.age, grades.subject, grades.grade
        FROM users
        FULL OUTER JOIN grades ON users.user_id = grades.userid
        WHERE age = 19
    ''')
    connect.commit()
    print('Представление создано!!')


def get_user_age_19():
    cursor.execute('SELECT * FROM view_test')
    print(cursor.fetchone())

# get_user_age_19()

def users_and_grades():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
        SELECT users.name, users.age, grades.subject, grades.grade
        FROM users
        FULL OUTER JOIN grades ON users.user_id = grades.userid
        WHERE age > 21
    ''')
    connect.commit()
    print("Представление my_view создано!")


def get_from_view():
    cursor.execute("SELECT * FROM my_view")
    for row in cursor.fetchall():
        print(row)

users_and_grades()
get_from_view()