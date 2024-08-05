
import threading
import os
# This is process of creating multiple
def func1():
    for i in range(5):
        print("Numbers are",i)


def func2():
    for i in range(4):
        print("Numbers are",i)


def combine():
    func1()
    func2()


thread=threading.Thread(target=combine)
thread.start()