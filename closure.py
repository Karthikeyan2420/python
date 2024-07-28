def greet(name):
    def diplay_name():
        print("hi",name)
    diplay_name()
greet("bavi")

def greet():
    name='kathir'
    return lambda:"hi "+name
message=greet()
print(message())


