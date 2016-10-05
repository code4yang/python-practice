"""
生产者消费者问题
"""
import multiprocessing
from multiprocessing import Process, Pool


def produce(que):
    while True:
        que.put('product')
        print('put a production')


def consum(que):
    while True:
        product = que.get()
        print('get:' + product)


if __name__ == '__main__':
    que = multiprocessing.Queue(10)
    producer = Process(target=produce, args=(que,))
    consumer = Process(target=consum, args=(que,))
    p = Pool(5)
    p.apply_async(produce, args=(que,))
    p.apply_async(produce, args=(que,))
    p.apply_async(produce, args=(que,))
    p.apply_async(produce, args=(que,))
    p.apply_async(produce, args=(que,))
    p.close()
    p.join()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    produce(que)
