from direction import Direction
import pygame

class Pikachu:
    def __init__(self,):
        self.direction = Direction.Down
        self.moving = False
        self.frame_index = 0
        self.x = 0
        self.y = 0
        self.spriteSheet = "sprites/pikachu.png"
        self.loadSprites(self.spriteSheet)
        self.sprite = self.getSprite(self.direction, self.moving)

    def loadSprites(self,spriteSheetPath):
        spriteSheet = pygame.image.load(spriteSheetPath).convert_alpha()
        frames = []
        NUM_FRAMES_IN_SPRITE_SHEET = 6
        for i in range(NUM_FRAMES_IN_SPRITE_SHEET):
            frames.append(self.getFrame(spriteSheet, i))
        self.idle_down = frames[0]
        self.idle_up = frames[1]
        self.idle_left = frames[2]
        self.idle_right = pygame.transform.flip(self.idle_left, True, False)
        self.walk_down = [frames[3], pygame.transform.flip(frames[3], True, False)]
        self.walk_up = [frames[4], pygame.transform.flip(frames[4], True, False)]
        self.walk_left = [frames[5], self.idle_left]
        self.walk_right = [pygame.transform.flip(frames[5], True, False), self.idle_right]

    def getFrame(self,sheet,row,width=16,height=16):
        frame = pygame.Surface((width, height), pygame.SRCALPHA)
        frame.blit(sheet, (0,0),(0, row*height, width, height))
        return frame

    def getSprite(self, direction, moving):
        if not moving:
            return self.idle_down
        else:
            return self.walk_down[0]
