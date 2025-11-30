from direction import Direction
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
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.SCALED)
pygame.display.set_caption('pikachu!')

# Players 
# Note! must do this after pygame.init because the Pikachu class relies on the display being
# initialized already.
player = Pikachu()

#main loop
playerInput = []
while True:
    # listen for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                playerInput.append(Direction.Left)
            if event.key == K_w:
                playerInput.append(Direction.Up)
            if event.key == K_s:
                playerInput.append(Direction.Down)
            if event.key == K_d:
                playerInput.append(Direction.Right)
        if event.type == KEYUP:
            try:
                if event.key == K_a:
                    playerInput.remove(Direction.Left)
                if event.key == K_w:
                    playerInput.remove(Direction.Up)
                if event.key == K_s:
                    playerInput.remove(Direction.Down)
                if event.key == K_d:
                    playerInput.remove(Direction.Right)
            except Exception as e:
                continue
    
    # tick the clock
    dt = mainClock.tick(FPS)
    
    # redraw everything
    windowSurface.fill(WHITE)
    player.update(dt, playerInput[0] if len(playerInput) > 0 else None);
    windowSurface.blit(player.sprite, (player.x, player.y))
    
    # update your window
    pygame.display.update()
    
