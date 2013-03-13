# Board classes

from snake import Snake
import constants
from food import Food
import random
import pygame

class Board(object):
	"""Class for basic boar behaviour"""
	def __init__(self, map = None, snakes = []):
		self.snakes = snakes
		self.map = map
		self.foods = pygame.sprite.Group()

	def add_snake(self, snake):
		self.snakes.append(snake)
		
	def add_map(self, map):
		self.map = map

	def add_food(self, food):
		self.foods.add(food)
		
	def draw(self, screen):
		# Draw map
		self.map.draw(screen)

		self.foods.draw(screen)
		
		# Draw snakes
		for snake in self.snakes:
			snake.draw(screen)

	def next_location(self, location, direction):
		"""Calculate new location based on previous location and current direction"""
		(dx, dy) = (0, 0)
		if (direction == 0):
			dx = (constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN)
		elif (direction == 1):
			dy = -(constants.SEGMENT_HEIGHT + constants.SEGMENT_MARGIN)
		elif (direction == 2):
			dx = -(constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN)
		else:
			dy = (constants.SEGMENT_HEIGHT + constants.SEGMENT_MARGIN)

		return (location[0] + dx, location[1] + dy)
		
	def move_snake(self, snake, direction):
		# Check if snake is already dead
		if (snake.is_dead()):
			if (snake.get_timeout() >= 5):
				self.snakes.remove(snake)
			return

		# Get current head location and calculate next location with direction
		location = snake.get_head_segment().get_location()
		next_location = self.next_location(location, direction)

		# Check if location is not occupied
		if (self.is_valid_location(next_location)):
			# Check if location contains food
			for food in self.foods:
				# If the location is equal to the next location, update length and update food
				if (food.get_location() == next_location):
					self.foods.remove(food)
					snake.set_new_length(snake.get_length() + 1)
					snake.move(direction, next_location)

					# Add new food
					self.spawn_food()
				else:
					snake.move(direction, next_location)
					

		else:
			# Die
			self.kill_snake(snake)
		
	def is_valid_location(self, location):
		# Check if the location is within the map borders
		if ((0 <= location[0] < self.map.get_size()[0]) and (0 <= location[1] < self.map.get_size()[1])):
			# If the location on the map contains a solid entry
			if (self.map.contains_solid_entry(location)):
				return False

			# Check wether the location coincides with a snake segment
			for snake in self.snakes:
				try:
					index = snake.get_locations().index(location)
					return False
				except:
					pass

			# If location is correct, return True
			return True

		else:
			return False

	def kill_snake(self, snake):
		# Kill the snake
		snake.kill()

	def has_snakes(self):
		# Check whether there are still snakes on the board
		if (len(self.snakes) > 0):
			return True
		else:
			return False

	def spawn_food(self):
		# Get maximum dimension
		map_size = self.map.get_size()
		max_x = map_size[0]
		max_y = map_size[1]

		# Get random location for x and y
		correct_point = False
		while (correct_point == False):
			# Get random values for x and y
			x = random.randint(0, max_x)
			y = random.randint(0, max_y)

			# Transform into correct locations:
			x = round(x / (constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN)) * (constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN)
			y = round(x / (constants.SEGMENT_HEIGHT + constants.SEGMENT_MARGIN)) * (constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN)

			location = (x, y)

			# Now check if we have a valid location for food
			if (self.is_valid_location(location)):
				correct_point = True

		# We have attained a correct value for the food, now add it
		self.add_food(Food(location))
