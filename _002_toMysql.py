import pymysql
import uuid


def write2mysql(count):
    """
    写入count数量的票ID到数据库python中
    :param count: 写入票ID的总数
    :return:
    """
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='python')
    print(con)
    cur = con.cursor()
    for i in range(1, count):
        uid = uuid.uuid1()
        cur.execute('insert into ticket(id) VALUES("' + uid.__str__() + '")')
    cur.close()
    con.commit()
    print('done')


