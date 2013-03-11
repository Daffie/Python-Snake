import pygame
from map import Map, MapParser
from board import Board
from snake import Snake
import food
import constants

# Call this function so the Pygame library can initialize itself
pygame.init()

# Get the dimensions of the map
(entries, lines, entry_list) = MapParser.parse_mapfile("test_map.txt")
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
location = (240, 96)
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
board.add_food(food)

clock = pygame.time.Clock()
done = False

# Clear screen
board.draw(screen)
# Flip screen
pygame.display.flip()
# Pause
clock.tick(1)

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

	board.move_snake(snake, direction, length)
	# Draw screen
	board.draw(screen)
	# Flip screen
	pygame.display.flip()
	# Pause
	clock.tick(1)

pygame.quit()
