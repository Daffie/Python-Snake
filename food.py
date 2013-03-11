import os
import pygame
import constants

#Food class

class food(pygame.sprite.Sprite):
    DIRECTORY = os.path.join("Sprites", "map sprites")
    def __init__(self, rocklocation):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        rocklocation = (32, 32)
	# Set height, width
        self.image = pygame.image.load(os.path.join(self.DIRECTORY, self.SPRITE_IMAGE)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.SEGMENT_WIDTH, constants.SEGMENT_HEIGHT))
        SPRITE_IMAGE = "rock.png"

    def draw(self, screen):
        self.sprites.draw(screen)
