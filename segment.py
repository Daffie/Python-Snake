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
                # Set height, width
                self.image = pygame.image.load(os.path.join(self.DIRECTORY, self.SPRITE_IMAGE)).convert()
                self.image = pygame.transform.scale(self.image, (constants.SEGMENT_WIDTH, constants.SEGMENT_HEIGHT))
                self.image = pygame.transform.rotate(self.image, orientation * 90)
                # Make our top-left corner the passed-in location.
                self.rect = self.image.get_rect()
                self.rect.move_ip(location)
                self.orientation = orientation

        def update(self, new_location, new_orientation):
                self.location = new_location
                self.orientation = new_orientation

        def get_location(self):
                return self.rect.top_left

        def get_orientation(self):
                return self.orientation

        def hide(self):
                self.image = None

class HeadSegment(Segment):
        SPRITE_IMAGE = "Head Red.png"

class TailSegment(Segment):
        SPRITE_IMAGE = "Tail Red.png"

class BodySegment(Segment):
        SPRITE_IMAGE = "Body Red.png"

class CornerSegment(Segment):
        SPRITE_IMAGE = "Corner Red.png"
