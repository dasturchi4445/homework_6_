# example synchronus

import time
from datetime import datetime


def task_1():
    time.sleep(2)
    print("Task 1 completed")


def task_2():
    time.sleep(2)
    print("Task 2 completed")
    task_1()


def task_3():
    time.sleep(2)
    print("Task 3 completed")


def task_4():
    time.sleep(2)
    print("Task 4 completed")
    task_5()


def task_5():
    time.sleep(2)
    print("Task 5 completed")


def task_6():
    time.sleep(2)
    print("Task 6 completed")


def task_7():
    time.sleep(2)
    print("Task 7 completed")


def task_8():
    time.sleep(2)
    print("Task 8 completed")
    task_7()


def task():
    print(datetime.now())
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    print(datetime.now())


if __name__ == "__main__":
    task()

"""
Asosiy Afzalliklar va Kamchiliklar
Sinxron Afzalliklari:
Soddaroq kod, tushunish osonroq, ketma-ket bajarish.
Sinxron Kamchiliklari:
Bloklovchi operatsiyalar, samaradorlik past bo'lishi mumkin.

"""
