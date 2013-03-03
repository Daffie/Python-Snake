# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
import pygame
from segment import BodySegment, TailSegment, HeadSegment
import constants
# --- Globals ---
# Colors
black = (0,0,0)
white = (255,255,255)
# Set the width and height of each snake segment
segment_width=constants.SEGMENT_WIDTH
segment_height=constants.SEGMENT_HEIGHT
# Margin between each segment
segment_margin=3
# Set initial speed
x_change=segment_width+segment_margin
y_change=0

# Call this function so the Pygame library can initialize itself
pygame.init()
# Create an 800x600 sized screen
screen = pygame.display.set_mode([640, 480])
# Set the title of the window
pygame.display.set_caption('Snake Example')
allspriteslist=pygame.sprite.Group()
# Create an initial snake
snake_segments=[]

x = 250 - (segment_width + segment_margin)
y = 30
segment = HeadSegment((x, y), 0)
snake_segments.append(segment)
allspriteslist.add(segment)

for i in range(2,14):
    x=250-(segment_width+segment_margin)*i
    y=30
    segment = BodySegment((x, y), 0)
    snake_segments.append( segment )
    allspriteslist.add( segment )

x = 250 - (segment_width + segment_margin) * 15
y = 30
segment = TailSegment((x, y), 0)
snake_segments.append(segment)
allspriteslist.add(segment)

clock = pygame.time.Clock()
done = False

angle = 0
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change=(segment_width+segment_margin)*-1
                y_change=0
                angle = 2
            if event.key == pygame.K_RIGHT:
                x_change=(segment_width+segment_margin)
                y_change=0
                angle = 0
            if event.key == pygame.K_UP:
                x_change=0
                y_change=(segment_height+segment_margin)*-1
                angle = 1
            if event.key == pygame.K_DOWN:
                x_change=0
                y_change=(segment_height+segment_margin)
                angle = 3
    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    tail_segment = snake_segments.pop()
    end_segment = snake_segments.pop()
    allspriteslist.remove(tail_segment)
    allspriteslist.remove(end_segment)
    segment = TailSegment((end_segment.rect.x, end_segment.rect.y), end_segment.orientation)
    snake_segments.append(segment)
    allspriteslist.add(segment)
    # Figure out where new segment will be
    allspriteslist.remove(snake_segments[0])
    snake_segments[0] = BodySegment((snake_segments[0].rect.x, snake_segments[0].rect.y), snake_segments[0].orientation)
    allspriteslist.add(snake_segments[0])
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = HeadSegment((x, y), angle)
    # Insert new segment into the list
    snake_segments.insert(0,segment)
    allspriteslist.add(segment)
    # -- Draw everything
    # Clear screen
    screen.fill(black)
    allspriteslist.draw(screen)
    # Flip screen
    pygame.display.flip()
    # Pause
    clock.tick(10)


pygame.quit()
