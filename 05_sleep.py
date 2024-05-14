import time


def sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        yield


def task1():
    while True:
        print('Task 1')
        yield from sleep(1)


def task2():
    while True:
        print('Task 2')
        yield from sleep(5)


event_loop = [task1(), task2()]

while True:
    for task in event_loop:
        next(task)

