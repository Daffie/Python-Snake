# Board classes

from snake import Snake
import constants
import food

class Board(object):
	"""Class for basic boar behaviour"""
	def __init__(self, map = None, snakes = [], food = []):
		self.snakes = snakes
		self.map = map
		self.food = food

	def add_snake(self, snake):
		self.snakes.append(snake)
		
	def add_map(self, map):
		self.map = map

	def add_food(self, food):
                self.food.append(food)
		
	def draw(self, screen):
		self.map.draw(screen)
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
		
	def move_snake(self, snake, direction, length):
		location = snake.get_head_segment().get_location()
		next_location = self.next_location(location, direction)
		snake.move(direction, length, next_location)
		
	def is_valid_location(self, location):
		if ((location[0] < self.map.get_size()[0]) and (location[1] < self.map.get_size()[1])):
			return True
		else:
			return False
