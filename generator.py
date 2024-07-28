def my_generator(n):
    value=0
    while value<n:
        yield value
        value+=1
for value in my_generator(10):
            print(value)


def demo():
    n=1
    while n<20:
        val=n*n
        yield val
        n+=1
a=demo()
for i in a:
    print(i)
