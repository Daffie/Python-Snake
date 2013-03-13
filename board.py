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
			if (snake.is_dead()):
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
		# Check if snake is already dead
		if snake.is_dead():
			if (snake.get_timeout() >= 10):
				self.snakes.remove(snake)
			return

		# Get current head location and calculate next location with direction
		location = snake.get_head_segment().get_location()
		next_location = self.next_location(location, direction)

		# Check if location is not occupied
		if (self.is_valid_location(next_location)):
			# Move the snake
			snake.move(direction, length, next_location)
		else:
			# Die
			self.kill_snake(snake)
		
	def is_valid_location(self, location):
		# Check if the location is within the map borders
		if ((0 < location[0] < self.map.get_size()[0]) and (0 < location[1] < self.map.get_size()[1])):
			# If the location on the map contains a solid entry
			if (map.contains_solid_entry(location)):
				return False

			# Check wether the location coincides with a snake segment
			for snake in self.snakes:
				try:
					index = snake.get_locations()[location]
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
