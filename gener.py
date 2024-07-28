#Generator is use to generate a iterator
#Create Spcial iter
#Keyword : Yield


# def my_generator(n):
#     # initialize counter
#     value = 0
#     # loop until counter is less than n
#     while value < n:
#         # produce the current value of the counter
#         yield value
#         # increment the counter
#         value += 2
# # iterate over the generator object produced by my_generator
# for value in my_generator(10):
#     # print each value produced by generator
#     print(value)




def demo():
    n=1
    while n<10:
        val=n*n;
        yield val
        n+=1
a=demo()
for i in a:
    print(i)
