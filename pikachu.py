from direction import Direction
import pygame

class Pikachu:

    CHANGE_WALKING_FRAME_CUTOFF = 300

    def __init__(self):
        self.direction = Direction.Down
        self.x = 0
        self.y = 0
        self.speed = 6
        self.walking_frame_index = 0
        self.spriteSheet = "sprites/pikachu.png"
        self.loadSprites(self.spriteSheet)
        self.last_update_time = 0
        self.sprite = self.update(0)

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

    def update(self, ticks, movingDirection=None):
        delta_ticks = ticks - self.last_update_time
        if movingDirection == None:
            self.last_update_time = ticks
            if self.direction == Direction.Left:
                self.sprite = self.idle_left
            elif self.direction == Direction.Right:
                self.sprite = self.idle_right
            elif self.direction == Direction.Up:
                self.sprite = self.idle_up
            else:
                self.sprite = self.idle_down
        else:
            if movingDirection != self.direction:
                self.last_update_time = ticks
                self.direction = movingDirection
                if self.direction == Direction.Left:
                    self.sprite = self.idle_left
                elif self.direction == Direction.Right:
                    self.sprite = self.idle_right
                elif self.direction == Direction.Up:
                    self.sprite = self.idle_up
                else:
                    self.sprite = self.idle_down
            if delta_ticks > CHANGE_WALKING_FRAME_CUTOFF:
                self.last_update_time = ticks
                self.walking_frame_index = (self.walking_frame_index + 1) % 2
            if self.direction == Direction.Left:
                self.x -= self.speed * delta_ticks
                self.sprite = self.walk_left[self.walking_frame_index]
            elif self.direction == Direction.Right:
                self.x += self.speed * delta_ticks
                self.sprite = self.walk_right[self.walking_frame_index]
            elif self.direction == Direction.Up:
                self.y -= self.speed * delta_ticks
                self.sprite = self.walk_up[self.walking_frame_index]
            else:
                self.y += self.speed * delta_ticks
                self.sprite = self.walk_down[self.walking_frame_index]
