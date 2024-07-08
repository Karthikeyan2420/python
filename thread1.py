""" import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)  

# print_numbers()
# print_numbers()

thread1 = threading.Thread(target=print_numbers)

thread2 = threading.Thread(target=print_numbers)
thread2.start()
thread1.start()
thread1.join()
thread2.join()   """





import threading
import time

# Function to print numbers from 1 to 5 with a delay
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)  # Simulating some time-consuming task

# Function to print letters from A to E with a delay
def print_letters():
    for char in ['A', 'B', 'C', 'D', 'E']:
        print(char)
        time.sleep(1)  # Simulating some time-consuming task

# Creating threads for the two functions
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting the threads                                                                                                                                                                                                                                                                                             
thread1.start()
thread2.start()

# Waiting for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished.") 

