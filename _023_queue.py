#!/usr/bin/env python
import multiprocessing as mp
from multiprocessing import Queue
from random import Random


def producer(que, lock):
    while True:
        x = Random().randint(1, 100)
        print('produce :' + str(x))
        que.put(x)


def customer(que, lock):
    while True:
        print('custom :' + str(que.get()))


def main():
    print('start:')
    q = Queue()
    lock = mp.Lock()
    p1 = mp.Process(target=producer, args=(q, lock))
    p2 = mp.Process(target=customer, args=(q, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
