import pygame, sys
from pygame.locals import *
import time
from pikachu import Pikachu

# Constants
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
PLAYER_HEIGHT = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
mainClock = pygame.time.Clock()
FPS = 60
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('pikachu!')

# Players 
# Note! must do this after pygame.init because the Pikachu class relies on the display being
# initialized already.
player = Pikachu()

#main loop
while True:
      # listen for events
      for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()

      # Do some math

      # redraw everything
      windowSurface.fill(WHITE)
      windowSurface.blit(player.sprite, (player.x, player.y))

      # update your window
      pygame.display.update()
      
      mainClock.tick(FPS)
