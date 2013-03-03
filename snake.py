# Snake classes

from segment import HeadSegment, TailSegment, BodySegment, CornerSegment
import constants
import pygame

class Snake(object):
	"""Snake class"""

	def __init__(self, location, length, direction):
		# Create a group of sprites ... 
		self.sprites = pygame.sprite.Group()
		# ... and a (ordered) list of segments
		self.segments = []
		
		# Add head segment
		self.add_segment(0, HeadSegment(location, (direction, direction)))

		# Add body segments
		for i in range(1, length - 1):
			location = self.next_location(location, direction, True)
			self.add_segment(i, BodySegment(location, (direction, direction)))
		
		# Add tail segment
		location = self.next_location(location, direction, True)
		self.add_segment(length - 1, TailSegment(location, (direction, direction)))
	
	def add_segment(self, i, segment):
		self.segments.insert(i, segment)
		self.sprites.add(segment)
		
	def next_location(self, location, direction, inverted = False):
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

		if (inverted):
			(dx, dy) = (-dx, -dy)

		return (location[0] + dx, location[1] + dy)
			
	def remove_segment(self, segment):
		self.segments.remove(segment)
		self.sprites.remove(segment)
		
	def move(self, new_direction, new_length):
		# Clear previous head segment and remove it
		head_segment = self.get_head_segment()
		self.remove_segment(head_segment)
		
		# Calculate next location for head, and add new head and body segments
		next_location = self.next_location(head_segment.get_location(), new_direction)
		self.add_segment(0, HeadSegment(next_location, (new_direction, new_direction)))
		if (head_segment.get_direction() != new_direction):
			self.add_segment(1, CornerSegment(head_segment.get_location(), (new_direction, head_segment.get_direction())))
		else:
			self.add_segment(1, BodySegment(head_segment.get_location(), (new_direction, head_segment.get_direction())))

		# If new length is smaller than self.length, remove segments until correct
		if (new_length < self.get_length()):
			# Remove body segments
			while new_length < self.get_length():
				last_segment = self.get_last_body_segment()
				self.remove_segment(last_segment)
			
			# Reallocate tail segment
			self.remove_segment(self.get_tail_segment())
			self.add_segment(new_length - 1, TailSegment(last_segment.get_location(), last_segment.get_orientation()))

	def get_length(self):
		return len(self.segments)
			
	def get_head_segment(self):
		return self.segments[0]

	def get_last_body_segment(self):
		return self.segments[self.get_length() - 2]

	def get_tail_segment(self):
		return self.segments[self.get_length() - 1]
		
	def draw(self, screen):
		self.sprites.draw(screen)