import pygame
# initialize pygame
pygame.init()

# define width of screen
width = 1000
# define height of screen
height = 600
screen_res = (width, height)

pygame.display.set_caption("GRS Bouncing game")
screen = pygame.display.set_mode(screen_res)

# define colors
red = (255, 0, 0)
green=(0,255,0)
blue=(0,0,255)
redgreen=(255,255,0)
redblue=(255,0,255)
black = (255,255,255)

# define ball
ball_obj = pygame.draw.circle(surface=screen, color=red, center=[100, 100], radius=20) 
ball_obj1= pygame.draw.circle(surface=screen, color=blue, center=[100,100],radius=20)
ball_obj2= pygame.draw.circle(surface=screen, color=green, center=[100,100],radius=20)
ball_obj3= pygame.draw.circle(surface=screen, color=redgreen, center=[100,100],radius=20)
ball_obj4= pygame.draw.circle(surface=screen, color=redblue, center=[100,100],radius=20)
# define speed of ball
# speed = [X direction speed, Y direction speed]
speed = [1, 1] 
speed1 = [2, 2]
speed2= [3,3]
speed3=[4,4]
speed4=[5,5]

# game loop
while True:
	# event loop
	for event in pygame.event.get():
		# check if a user wants to exit the game or not
		if event.type == pygame.QUIT:
			exit()

	# fill black color on screen
	screen.fill(black)

	# move the ball
	# Let center of the ball is (100,100) and the speed is (1,1)
	ball_obj = ball_obj.move(speed) 
	ball_obj1=ball_obj1.move(speed1)
	ball_obj2=ball_obj2.move(speed2)
	ball_obj3=ball_obj3.move(speed3)
	ball_obj4=ball_obj4.move(speed4)
	# Now center of the ball is (101,101)
	# In this way our wall will move

	# if ball goes out of screen then change direction of movement
	if ball_obj.left <= 0 or ball_obj.right >= width:
		speed[0] = -speed[0]
	if ball_obj.top <= 0 or ball_obj.bottom >= height:
		speed[1] = -speed[1]
		
	if ball_obj1.left <= 0 or ball_obj1.right >= width:
		speed1[0] =- speed1[0]
	if ball_obj1.top <= 0 or ball_obj1.bottom >= height:
		speed1[1] =- speed1[1] 
		

	if ball_obj2.left <= 0 or ball_obj2.right >= width:
		speed2[0] =- speed2[0]
	if ball_obj2.top <= 0 or ball_obj2.bottom >= height:
		speed2[1] =- speed2[1] 
	
	if ball_obj3.left <= 0 or ball_obj3.right >= width:
		speed3[0] =- speed3[0]
	if ball_obj3.top <= 0 or ball_obj3.bottom >= height:
		speed3[1] =- speed3[1] 
		
	if ball_obj4.left <= 0 or ball_obj4.right >= width:
		speed4[0] =- speed4[0]
	if ball_obj4.top <= 0 or ball_obj4.bottom >= height:
		speed4[1] =- speed4[1] 
		
    


	# draw ball at new centers that are obtained after moving ball_obj
	pygame.draw.circle(surface=screen, color=red,center=ball_obj.center, radius=30)
	pygame.draw.circle(surface=screen,color=blue,center=ball_obj1.center,radius=30)
	pygame.draw.circle(surface=screen,color=green,center=ball_obj2.center,radius=30)
	pygame.draw.circle(surface=screen,color=redgreen,center=ball_obj3.center,radius=30)
	pygame.draw.circle(surface=screen,color=redblue,center=ball_obj4.center,radius=30)
	
	



	# update screen
	pygame.display.flip()
