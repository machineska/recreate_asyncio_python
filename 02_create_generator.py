def generator():
    yield 'hello'
    yield 'world'

iterator = generator()

print(next(iterator))  # Output: hello
print(next(iterator))  # Output: world

