my=("kia","mahindra","hyundai","toyota","suzuki")
nk=iter(my)
print(next(nk))
print(next(nk))
print(next(nk))
print(next(nk))
print(next(nk))

def nk(n):
    value=0
    while value <n:
        yield value
        value +=2
for value in nk(10):
        print(value)
