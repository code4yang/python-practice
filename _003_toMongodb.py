"""
write 200 ticket to mongodb by using pymongo
"""
import uuid

from pymongo import MongoClient


def write2mongo(count):
    """
    写入count数量的ticket到mongodb中
    :param count: 写入数量
    :return:
    """
    con = MongoClient('localhost', 27017)  # 连接mongodb
    db = con['python']  #
    collection = db['ticket']
    for i in range(1, count):
        id = uuid.uuid1().__str__()
        data = {'ticket': id}
        collection.insert_one(data)

write2mongo(3)