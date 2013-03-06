# Snake classes

from segment import HeadSegment, TailSegment, BodySegment, CornerSegment
import constants
import pygame

class Snake(object):
	"""Snake class"""

	def __init__(self, locations, directions):
		# Create a group of sprites ... 
		self.sprites = pygame.sprite.Group()
		# ... and a (ordered) list of segments
		self.segments = []
		length = len(locations)
		
		# Add head segment
		self.add_segment(0, HeadSegment(locations[0], (directions[0], directions[0])))

		# Add body segments
		for i in range(1, length - 1):
			self.add_segment(i, BodySegment(locations[i], (directions[i - 1], directions[i])))
		
		# Add tail segment
		self.add_segment(length - 1, TailSegment(locations[length - 1], (directions[length - 1], directions[length - 1])))
	
	def add_segment(self, i, segment):
		self.segments.insert(i, segment)
		self.sprites.add(segment)
	
	def remove_segment(self, segment):
		self.segments.remove(segment)
		self.sprites.remove(segment)
		
	def move(self, new_direction, new_length, new_location):
		# Clear previous head segment and remove it
		head_segment = self.get_head_segment()
		self.remove_segment(head_segment)
		
		# Calculate next location for head, and add new head and body segments
		self.add_segment(0, HeadSegment(new_location, (new_direction, new_direction)))
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