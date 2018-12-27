#brief example of "yield from"
def gen():
    yield from 'ABC'
    yield from range(1,3)

print(list(gen()))

#practical usage of yield from:Chaining iterables with +yield from +
def chain(*iterables):
    for it in iterables:
        yield from it

s='ABC'
t = tuple(range(3))

print(list(chain(s,t)))
