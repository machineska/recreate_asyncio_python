def generator():
    yield 'hello'

def another_generator():
    yield from generator()

iterable = another_generator()
print(next(iterable))
