
def hello():
    n=1
    while n<14:
        val=n*n
        yield val
        n+=3
a=hello()
for i in a:
    print(i)

