"""
test sqlite

"""
import sqlite3


def test():
    conn = sqlite3.connect('db/test.db')
    conn.execute("""create table person(
    name varchar2(15),
    id NUMBER(16) PRIMARY KEY ,
    age NUMBER(3)
    )""")
    conn.execute('insert into person values("jack",123321123321,23)')
    conn.commit()


def query():
    conn = sqlite3.connect('test.db')
    cursor = conn.execute('select * from person')
    result = cursor.fetchone()
    while result is not None:
        print(result)
        result = cursor.fetchone()


if __name__ == '__main__':
    query()
