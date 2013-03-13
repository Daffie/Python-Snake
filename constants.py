# Game Constants

import os

# The width and height of each snake segment
SEGMENT_WIDTH = 16
SEGMENT_HEIGHT = 16

# Margin between each segment
SEGMENT_MARGIN = 0

MAPS_PATH = os.path.join("Maps")
MAP_SPRITES_PATH = os.path.join("Sprites", "map sprites")

# Images and functions used in the map:
MAP_IMAGES = {
	"bx": "border_bottom.png",
	"bz": "border_bottomleft.png",
	"bc": "border_bottomright.png",
	"ba": "border_left.png",
	"bd": "border_right.png",
	"bw": "border_top.png",
	"bq": "border_topleft.png",
	"be": "border_topright.png",

	"cq": "corner_topleft.png",
	"ce": "corner_topright.png",

	"wa": "water.png",
	"wx": "water_bottom.png",
	"wc": "water_bottomright.png",
	"wz": "water_bottomleft.png",
	"ww": "water_top.png",
	"we": "water_topright.png",
	"wq": "water_topleft.png",
	"wd": "water_right.png",
	"wa": "water_left.png",
	
	"gr": "grass.png",
	"ro": "rock.png"
}

ITEM_SPRITES = {
	"bu": "bush.png",
	"fl": "flower.png",
	"ho": "hole.png",
	"pl": "plant.png",
	"po": "poles.png",
	"si": "sign.png",
	"l1": "streetlight_bottom.png",
	"l2": "streetlight_top.png"
}

BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
