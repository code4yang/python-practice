import pymysql
import uuid

con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='python')
print(con)
cur = con.cursor()
for i in range(1,201):
    uid = uuid.uuid1()
    cur.execute('insert into ticket(id) VALUES("'+uid.__str__()+'")')
cur.close()
print('done')
