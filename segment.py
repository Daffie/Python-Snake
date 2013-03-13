import os
import pygame
import constants
# Segment classes

class Segment(pygame.sprite.Sprite):
	DIRECTORY = os.path.join("Sprites", "PNG sprites")
	SPRITE_IMAGE = ""
	def __init__(self, location, orientation):
		# Call the parent's constructor
		pygame.sprite.Sprite.__init__(self)
		# Save variables
		self.orientation = orientation
		# Set height, width
		self.image = pygame.image.load(os.path.join(self.DIRECTORY, self.SPRITE_IMAGE)).convert_alpha()
		self.image = pygame.transform.scale(self.image, (constants.SEGMENT_WIDTH, constants.SEGMENT_HEIGHT))

		# Flip according to orientation
		self.image = pygame.transform.rotate(self.image, self.get_angle())
		self.image = pygame.transform.flip(self.image, 0, self.get_flip())		
		
		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.move_ip(location)

	def get_angle(self):
		return self.get_direction() * 90
		
	def get_flip(self):
		return 0

	def update(self, new_location, new_orientation):
		self.location = new_location
		self.orientation = new_orientation

	def get_location(self):
		return self.rect.topleft

	def get_orientation(self):
		return self.orientation
	
	def get_direction(self):
		return self.orientation[0]

class HeadSegment(Segment):
	SPRITE_IMAGE = "Head Red.png"

class TailSegment(Segment):
	SPRITE_IMAGE = "Tail Red.png"

class BodySegment(Segment):
	SPRITE_IMAGE = "Body Red.png"

class CornerSegment(Segment):
	SPRITE_IMAGE = "Corner Red.png"

	def get_flip(self):
			# Difference between next and previous direction
		difference = self.get_orientation()[0] - self.get_orientation()[1]
		
		# If difference is -3 or 3, it is either 1 or -1
		if ((difference == -3) or (difference == 3)):
			difference = -difference/3
			
		# Now calculate the turning angle:
		if (difference == 1):
			return False
		else: 
			return True
	
	def get_angle(self):
		# Difference between next and previous direction
		difference = self.get_orientation()[0] - self.get_orientation()[1]
		
		# If difference is -3 or 3, it is either 1 or -1
		if ((difference == -3) or (difference == 3)):
			difference = -difference/3
			
		# Now calculate the turning angle:
		if (difference == 1):
			return self.get_orientation()[1] * 90
		else: 
			return self.get_orientation()[1] * -90
