import pygame
from map import Map, MapParser
from board import Board
from snake import Snake
import constants
import sys

# Define title:
TITLE = "Python-Snake | Score: "

# Call this function so the Pygame library can initialize itself
pygame.init()

# Get the dimensions of the map
(entries, lines, entry_list) = MapParser.parse_mapfile("test_map2.txt")
width = entries * (constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN)
height = lines * (constants.SEGMENT_HEIGHT + constants.SEGMENT_MARGIN)

screen = pygame.display.set_mode((width, height))
# Set the title of the window
pygame.display.set_caption('Python-Snake')

# Create a board
board = Board()

# Snake parameters:
length = 3
direction = 0
location = (160, 96)
locations = []
directions = []

# Calculate a set of locations
for i in range(length):
	location = board.next_location(location, direction)
	locations.insert(0, location)
	directions.append(direction)

# Create a map
map = Map(entries, lines, entry_list)
# Create a snake
snake = Snake(locations, directions)
board.add_map(map)
board.add_snake(snake)
board.spawn_food()

clock = pygame.time.Clock()
done = False

# Clear screen
board.draw(screen)
# Flip screen
pygame.display.flip()
# Pause
clock.tick(5)

# Play game
while ((done == False) and board.has_snakes()):
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
			if (event.key == pygame.K_ESCAPE):
				done = True

	# Move snake
	board.move_snake(snake, direction)
	# Update caption
	pygame.display.set_caption(TITLE + str((snake.get_length() - 3) * 10))
	# Draw screen
	board.draw(screen)
	# Flip screen
	pygame.display.flip()
	# Pause
	clock.tick(5)

# Show credits
screen.fill(constants.BACKGROUND_COLOR)
font1 = pygame.font.SysFont("arial", 50)
font2 = pygame.font.SysFont("arial", 25)
text_surface1 = font1.render("GAME OVER", True, constants.TEXT_COLOR)
text_surface2 = font2.render("Score: " + str((snake.get_length() - 3) * 10), True, constants.TEXT_COLOR)
location1 = ((width - text_surface1.get_width())/2, (height - text_surface1.get_height())/2)
location2 = ((width - text_surface2.get_width())/2, location1[1] + text_surface1.get_height() / 2 + 20)
screen.blit(text_surface1, location1)
screen.blit(text_surface2, location2)
pygame.display.flip()

done = False
while (done == False):
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			done = True
		if (event.type == pygame.KEYDOWN):
				done = True
	clock.tick(5)

pygame.quit()
sys.exit()
