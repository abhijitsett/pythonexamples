def count():
    for i in range(1,5):
        yield i

gen = count()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def infinite_ids():
    i = 0
    while True:
        yield i
        i += 1

gen1 = infinite_ids()
print(next(gen1))
print(next(gen1))