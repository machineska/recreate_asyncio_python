import asyncio


async def task1():
    for _ in range(2):
        print('Task 1')
        await asyncio.sleep(1)


async def task2():
    for _ in range(3):
        print('Task 2')
        await asyncio.sleep(0)


async def main():
    one = asyncio.create_task(task1())
    two = asyncio.create_task(task2())
    
    await one
    await two
    
    print('done')


if __name__ == '__main__':
    asyncio.run(main())

