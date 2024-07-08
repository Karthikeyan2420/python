# import turtle
# s=turtle.Turtle()
# s.pensize(10)
# s.circle(100)
# s.seth(180)
# turtle.done()



# import turtle
# s=turtle.Turtle()
# s.forward(100)
# s.backward(50)
# s.right(90)
# s.dot()
# s.forward(100)
# s.home()
# s.goto(100,-60)
# s.shape("circle")
# s.left(750)
# turtle.done()

import turtle
import random
screen = turtle.Screen()
screen.title("Real-Time Graphics with Turtle")
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed(1)
def move_and_turn():
    pen.forward(100)
    pen.right(90)
def change_color():
    red = random.random()
    green = random.random()
    blue = random.random()
    pen.color(red, green, blue)
screen.onkeypress(move_and_turn, "space")
screen.onkeypress(change_color, "c")
screen.listen()
while True:
    move_and_turn()

    change_color()

    screen.update()
screen.mainloop() 



# import calendar
# import datetime
# # Display the calendar for a specific year and month
# year = 2024
# month = 1  # January
# print(calendar.month(year, month))
# # Get the current date and time

# current_datetime = datetime.datetime.now()

# print("Current date and time:", current_datetime)

# # Get the current date
# current_date = datetime.date.today()

# print("Current date:", current_date)

# # Create a specific date
# specific_date = datetime.date(2024, 1, 30)
# print("Specific date:", specific_date)  




# """ import pandas as pd
# #
# mydataset = {
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3, 7, 2]
# }
# print(mydataset)
# myvar = pd.DataFrame(mydataset)
# print(myvar)  """


# """ import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# a=[]
# print(type(a))
# print(type(arr)) """


# #
# """ import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(xpoints, ypoints)

# plt.title("title")
# plt.xlabel("number")
# plt.ylabel("mark")
# plt.show()  """



# """ import numpy as np
# from scipy.sparse import csr_matrix

# arr = np.array([0, 0, 0, 0, 3, 1, 1, 0, 2])

# print(csr_matrix(arr))  """

# """ import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# class SimpleApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Simple PyQt Example')

#         # Create label
#         self.label = QLabel('Initial Text')

#         # Create button
#         self.button = QPushButton('Click Me')
#         self.button.clicked.connect(self.onButtonClick)

#         # Create layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.button)

#         self.setLayout(layout)

#     def onButtonClick(self):
#         self.label.setText('Button Clicked')


# app = QApplication(sys.argv)
# window = SimpleApp()
# window.setGeometry(100, 100, 300, 200)
# window.show()
# sys.exit(app.exec_()) """

# """ print('Welcome to AskPython Quiz')
# answer=input('Are you ready to play the Quiz ? (yes/no) :')
# score=0
# total_questions=3
 
# if answer.lower()=='yes':
#     answer=input('Question 1: What is your Favourite programming language?')
#     if answer.lower()=='python':
#         score += 1
#         print('correct')
#     else:
#         print('Wrong Answer :(')
 
 
#     answer=input('Question 2: Do you follow any author on AskPython? ')
#     if answer.lower()=='yes':
#         score += 1
#         print('correct')
#     else:
#         print('Wrong Answer :(')
 
#     answer=input('Question 3: What is the name of your favourite website for learning Python?')
#     if answer.lower()=='askpython':
#         score += 1
#         print('correct')
#     else:
#         print('Wrong Answer :(')
 
# print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
# mark=(score/total_questions)*100
# print('Marks obtained:',mark)
# print('BYE!')  """

# import pygame
# import sys

#  # Initialize Pygame
# pygame.init()

# # Set up the window
# window_width = 800
# window_height = 600
# window = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("Simple Pygame Example")

# # Set up colors
# BLUE = (0, 0, 255)

# # Main game loop
# running = True
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Fill the window with blue color
#     window.fill(BLUE)

#     # Update the display
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()
# sys.exit()  



import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Jumping Ball")

# Set up colors  
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the ball
ball_radius = 20
ball_x = window_width // 2
ball_y = window_height - ball_radius
ball_dy = 0
gravity = 0.5
jump_strength = -10
on_ground = True

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                ball_dy = jump_strength
                on_ground = False

    # Update ball position
    ball_y += ball_dy
    ball_dy += gravity

    # Check for collision with ground
    if ball_y >= window_height - ball_radius:
        ball_y = window_height - ball_radius
        ball_dy = 0
        on_ground = True

    # Fill the window with white color
    window.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(window, BLUE, (ball_x, int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()  

#  """

# """ import requests
# from bs4 import BeautifulSoup

# # URL of the webpage to scrape
# url = 'https://en.wikipedia.org/wiki/Main_Page'

# # Send a GET request to the webpage
# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find and print the title of the webpage
# title = soup.title
# print("Title of the webpage:", title.text)

# print(soup.li) """