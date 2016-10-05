import multiprocessing
import os
import random
from multiprocessing import Process

# 子进程要执行的代码
import time


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    print('Child process end.')


def run(name):
    print(name)
    print('Child process end.')


def get_que(que, lock):
    while True:
        val = que.get()
        lock.acquire()
        print('get :' + str(val))
        lock.release()
        time.sleep(1)


def put_que(que, lock):
    while True:
        val = random.randint(1, 101)
        lock.acquire()
        print('put :' + str(val))
        lock.release()
        que.put(val)
        time.sleep(3)


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    que = manager.Queue()
    que.put(1)
    # lock = manager.Lock()
    lock = multiprocessing.Lock()
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    p2 = Process(target=run, args=([1, 2, 3, 4, 5, 6],))
    p3 = Process(target=get_que, args=(que, lock,))
    p4 = Process(target=put_que, args=(que, lock,))
    print('Child process will start.')
    p.start()
    p2.start()
    p3.start()
    p4.start()
    p.join()
    p2.join()
    p3.join()
    p4.join()
