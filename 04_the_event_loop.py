def task1():
    while True:
        print('Task 1')
        yield


def task2():
    while True:
        print('Task 2')
        yield

event_loop = [task1(), task2()]

while True:
    for task in event_loop:
        next(task)
