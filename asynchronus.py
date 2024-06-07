# example asynchronus

import asyncio
from datetime import datetime


async def task_1():
    await asyncio.sleep(3)
    print("Task 1 completed")


async def task_2():
    await asyncio.sleep(2)
    print("Task 2 completed")
    await task_1()


async def task_3():
    await asyncio.sleep(4)
    print("Task 3 completed")


async def task_4():
    await asyncio.sleep(1)
    print("Task 4 completed")
    await task_3()


async def main():
    await asyncio.gather(task_1(), task_2(), task_3(), task_4())


if __name__ == "__main__":
    print(datetime.now())
    asyncio.run(main())
    print(datetime.now())

"""
Asosiy Afzalliklar va Kamchiliklar
Asinxron Afzalliklari:
Samarali resurslardan foydalanish, yuqori tezlik, parallel vazifalarni bajarish.
Asinxron Kamchiliklari:
Murakkab kod, nosozliklarni boshqarish qiyinroq, debugg qilish qiyinroq.

"""
