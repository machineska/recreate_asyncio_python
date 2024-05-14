import jacobio


async def task1():
    for _ in range(2):
        print('Task 1')
        await jacobio.sleep(1)


async def task2():
    for _ in range(3):
        print('Task 2')
        await jacobio.sleep(0)


async def main():
    one = jacobio.create_task(task1())
    two = jacobio.create_task(task2())

    await one
    await two

    print('done')



if __name__ == '__main__':
    jacobio.run(main())
