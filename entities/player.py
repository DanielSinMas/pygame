import pygame
from Constants import *
from Utilities.SpriteSheet import SpriteSheet


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.sprite_sheet = SpriteSheet("images/isaac.png")
        self.walking_frames_right = []
        self.walking_frames_left = []
        self.walking_frames_up = []
        self.walking_frames_bottom = []
        self.__createFrames__()
        self.last_update = 0
        self.image_position = 0
        self.image = self.walking_frames_bottom[self.image_position]
        self.direction = 2

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -PLAYER_SPEED
            self.direction = 3
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = PLAYER_SPEED
            self.direction = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vy = -PLAYER_SPEED
            self.direction = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = PLAYER_SPEED
            self.direction = 2

        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

        if self.vx == 0 and self.vy == 0:
            self.image_position = 0

    def collide_with_walls(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x

        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.image_position += 1
            self.last_update = now
            if self.image_position == 6:
                self.image_position = 0
            frames = self.__get_frames()
            self.image = frames[self.image_position]

    def __get_frames(self):
        if self.direction == 0:
            return self.walking_frames_up
        elif self.direction == 1:
            return self.walking_frames_right
        elif self.direction == 2:
            return self.walking_frames_bottom
        elif self.direction == 3:
            return self.walking_frames_left

    def __createFrames__(self):
        image = self.sprite_sheet.get_image(0, 0, 32, 32)
        self.walking_frames_bottom.append(image)
        image = self.sprite_sheet.get_image(34, 0, 32, 32)
        self.walking_frames_bottom.append(image)
        image = self.sprite_sheet.get_image(68, 0, 32, 32)
        self.walking_frames_bottom.append(image)
        image = self.sprite_sheet.get_image(102, 0, 32, 32)
        self.walking_frames_bottom.append(image)
        image = self.sprite_sheet.get_image(134, 0, 32, 32)
        self.walking_frames_bottom.append(image)
        image = self.sprite_sheet.get_image(170, 0, 32, 32)
        self.walking_frames_bottom.append(image)

        image = self.sprite_sheet.get_image(0, 68, 32, 32)
        self.walking_frames_right.append(image)
        image = self.sprite_sheet.get_image(34, 68, 32, 32)
        self.walking_frames_right.append(image)
        image = self.sprite_sheet.get_image(68, 68, 32, 32)
        self.walking_frames_right.append(image)
        image = self.sprite_sheet.get_image(102, 68, 32, 32)
        self.walking_frames_right.append(image)
        image = self.sprite_sheet.get_image(134, 68, 32, 32)
        self.walking_frames_right.append(image)
        image = self.sprite_sheet.get_image(170, 68, 32, 32)
        self.walking_frames_right.append(image)

        image = self.sprite_sheet.get_image(0, 134, 32, 32)
        self.walking_frames_up.append(image)
        image = self.sprite_sheet.get_image(34, 134, 32, 32)
        self.walking_frames_up.append(image)
        image = self.sprite_sheet.get_image(68, 134, 32, 32)
        self.walking_frames_up.append(image)
        image = self.sprite_sheet.get_image(102, 134, 32, 32)
        self.walking_frames_up.append(image)
        image = self.sprite_sheet.get_image(134, 134, 32, 32)
        self.walking_frames_up.append(image)
        image = self.sprite_sheet.get_image(170, 134, 32, 32)
        self.walking_frames_up.append(image)

        image = self.sprite_sheet.get_image(0, 68, 32, 32)
        image = pygame.transform.flip(image, 32, 0)
        self.walking_frames_left.append(image)
        image = self.sprite_sheet.get_image(34, 68, 32, 32)
        image = pygame.transform.flip(image, 32, 0)
        self.walking_frames_left.append(image)
        image = self.sprite_sheet.get_image(68, 68, 32, 32)
        image = pygame.transform.flip(image, 32, 0)
        self.walking_frames_left.append(image)
        image = self.sprite_sheet.get_image(102, 68, 32, 32)
        image = pygame.transform.flip(image, 32, 0)
        self.walking_frames_left.append(image)
        image = self.sprite_sheet.get_image(134, 68, 32, 32)
        image = pygame.transform.flip(image, 32, 0)
        self.walking_frames_left.append(image)
        image = self.sprite_sheet.get_image(170, 68, 32, 32)
        image = pygame.transform.flip(image, 32, 0)
        self.walking_frames_left.append(image)

    def action_pressed(self):
        object_selected_x = int(self.x / TILESIZE)
        object_selected_y = int(self.y / TILESIZE)
        print("Player:" + str(object_selected_x), str(object_selected_y))
        if self.direction == 0:
            object_selected_y += - 1
        if self.direction == 1:
            object_selected_x += 1
        if self.direction == 2:
            object_selected_y += 1
        if self.direction == 3:
            object_selected_x += -1

        print("Object:" + str(object_selected_x), str(object_selected_y) + "\n")

        for col, item in enumerate(self.game.processor.map_data[object_selected_y]):
            if col == object_selected_x:
                entity = self.__get_item_at__(object_selected_x, object_selected_y)
                if entity is not None:
                    entity.player_interaction()
                pass

    def __get_item_at__(self, x, y):
        for entity in self.game.walls:
            if entity.x == x and entity.y == y:
                return entity
