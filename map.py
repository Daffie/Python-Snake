# Map class

import constants
import os
import pygame

class MapParser(object):

	def parse_mapfile(mapfile):
		# Open the map file, and add a list of sprite objects
		# According to the data in the mapfile

		# Path to mapfiles
		path = os.path.join(constants.MAPS_PATH, mapfile)

		lines = 0
		entries = 0
		entry_list = []

		# Open the mapfile
		with open(path, 'r') as f:
			# Iterate over the lines in the mapfile
			for line in f:
				# Count the number of lines
				lines += 1
				entries = 0

				# Iterate over all the entries in a line
				for entry in line.split():
					# Update number of entries
					entries += 1

					# Add the entity to the entrylist
					entry_list.append(entry)

		# Return number lines, entries and the entries itself
		return (entries, lines, entry_list)

class Map(object):

	def __init__(self, entries, lines, entry_list):
		self.map_entries = pygame.sprite.Group()
		# Store the size of the map
		width = entries * (constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN)
		height = lines * (constants.SEGMENT_HEIGHT + constants.SEGMENT_MARGIN)
		self.size = (width, height)
		
		# Create the sprites according to the entry list and dimensions of the board
		current_line = 0
		current_entry = 0
		for entry in entry_list:
			# Calculate the new locations for this sprite
			x = current_entry * (constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN)
			y = current_line * (constants.SEGMENT_HEIGHT + constants.SEGMENT_MARGIN)
					
			# Find where the image is located
			path = os.path.join(constants.MAP_SPRITES_PATH, constants.MAP_IMAGES[entry])

			if (entry == "gr" or entry == "bw"):
				# If the sprite is a grass entry, it is not solid
				self.map_entries.add(MapEntry(path, (x, y), False))
			else:
				# Otherwise, the sprite is solid
				self.map_entries.add(MapEntry(path, (x, y), True))

			# Update the current entry and line				
			current_entry += 1

			if (current_entry == entries):
				current_line += 1
				current_entry = 0

	def draw(self, screen):
		self.map_entries.draw(screen)
		
	def get_size(self):
		return self.size

	def contains_solid_entry(self, location):
		# Check if location on map contains solid MapEntry
		for map_entry in self.map_entries:
			# Store entry location
			entry_location = map_entry.get_location()
			entry_next_location = (entry_location[0] + constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN, entry_location[1] + constants.SEGMENT_HEIGHT + constants.SEGMENT_MARGIN)

			if ((entry_location[0] <= location[0] < entry_next_location[0]) and (entry_location[1] <= location[1] < entry_next_location[1])):
				# The sprite is on this MapEntry, check if solid
				if (map_entry.is_solid()):
					return True

		# Else return false
		return False
				
				
class MapEntry(pygame.sprite.Sprite):

	def __init__(self, image_path, location, solid):
		# Call the parent's constructor
		pygame.sprite.Sprite.__init__(self)
		# Save variables
		self.solid = solid
		# Set height, width
		self.image = pygame.image.load(image_path).convert()
		correct_size = (constants.SEGMENT_WIDTH + constants.SEGMENT_MARGIN, constants.SEGMENT_HEIGHT + constants.SEGMENT_MARGIN)
		self.image = pygame.transform.scale(self.image, correct_size)
		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.move_ip(location)
		
	def is_solid(self):
		return self.solid

	def get_location(self):
		return self.rect.topleft
