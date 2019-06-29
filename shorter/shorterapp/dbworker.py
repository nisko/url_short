import sqlite3
from shorter.shorterapp import worker


def url_handle(url):
    conn = sqlite3.connect("urldb.db")
    cursor = conn.cursor()
    res = check_in_db(cursor, url)
    if len(res) > 0:
        short = res[0][1]
    else:
        short = add_url(cursor, url)
        conn.commit()
    cursor.close()
    conn.close()
    return short


def check_in_db(cursor, url):
    cursor.execute('CREATE TABLE if not exists urls\n'
                   '                      (longurl text, shorturl text)\n'
                   '                   ')
    cursor.execute('SELECT * FROM urls WHERE longurl=?', [url])
    return cursor.fetchall()


def add_url(cursor, url):
    num = get_url_count(cursor)
    short = worker.gen_short(num)
    cursor.execute('insert into urls values (?,?)', (url, short))
    return short


def get_url_count(cursor):
    cursor.execute('SELECT COUNT(*) FROM urls')
    return cursor.fetchall()[0][0]
