import pygame
from snake import Snake
import constants
# --- Globals ---
# Colors
black = (0,0,0)
white = (255,255,255)

# Call this function so the Pygame library can initialize itself
pygame.init()
# Create an 640x480 sized screenz
screen = pygame.display.set_mode([640, 480])
# Set the title of the window
pygame.display.set_caption('Python-Snake')
length = 3
direction = 0
locations = []
directions = []

snake = Snake((250, 90), length, direction)

clock = pygame.time.Clock()
done = False

# Clear screen
screen.fill(white)
snake.draw(screen)
# Flip screen
pygame.display.flip()
# Pause
clock.tick(5)

while done == False:
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			done = True
		if (event.type == pygame.KEYDOWN):
			if (event.key == pygame.K_LEFT):
				direction = 2
			if (event.key == pygame.K_RIGHT):
				direction = 0
			if (event.key == pygame.K_UP):
				direction = 1
			if (event.key == pygame.K_DOWN):
				direction = 3
			if (event.key == pygame.K_SPACE):
				length += 1

	snake.move(direction, length)

	# Clear screen
	screen.fill(white)
	snake.draw(screen)
	# Flip screen
	pygame.display.flip()
	# Pause
	clock.tick(5)

pygame.quit()
