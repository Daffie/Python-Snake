import os
import pygame
import constants

# Food class

class Food(pygame.sprite.Sprite):
	DIRECTORY = os.path.join("Sprites", "map sprites")
	SPRITE_IMAGE = "rock.png"

	def __init__(self, location):
		# Call the parent's constructor
		pygame.sprite.Sprite.__init__(self)
		# Set height, width
		self.image = pygame.image.load(os.path.join(self.DIRECTORY, self.SPRITE_IMAGE)).convert_alpha()
		self.image = pygame.transform.scale(self.image, (constants.SEGMENT_WIDTH, constants.SEGMENT_HEIGHT))
		
		# Make our top-left corner the passed-in location
		self.rect = self.image.get_rect()
		self.rect.move_ip(location)

	def get_location(self):
		return self.rect.topleft
