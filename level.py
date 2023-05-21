import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
from random import choice
from weapeon import Weapon
from ui import UI

class Level:
    def __init__(self):
        #Define the display surface
        self.display_surface = pygame.display.get_surface()

        #Sprite group setup
        self.obstacles_sprites = pygame.sprite.Group()
        self.visible_sprites = YSortCameraGroup()

        #Attack sprite
        self.current_attack = None

        #Sprite setup
        self.create_map()

        #user interface (UI)
        self.ui = UI()
    
    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('map/game_Collisions.csv'),
            'obj1': import_csv_layout('map/game_Ground 4 (decorations wh).csv'),
            'obj2': import_csv_layout('map/game_Ground 6 (trees).csv'),
        }

        graphics = {
            'obj1': import_folder('images/obj1'),
            'obj2': import_folder('images/obj2'),
        }

        positions = {
            'obj1': get_pos('images/obj1'),
            'obj2': get_pos('images/obj2'),
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index*tile_size
                        y = row_index*tile_size
                        if style == 'boundary':
                            Tile((x, y), [self.obstacles_sprites], 'invisible')
                        if style == 'obj1':
                            #Create the objects tiles
                            if int(col) < 10:
                                file_name = f'0{col}.png'
                            else:
                                file_name = f'{col}.png'
                            file_list = positions['obj1']
                            file_index = file_list.index(file_name)
                            surface = graphics['obj1'][file_index]
                            Tile((x, y), [self.visible_sprites], 'obj1', surface)
                        if style == 'obj2':
                            #Create the second object tiles
                            if int(col) < 10:
                                file_name = f'0{col}.png'
                            else:
                                file_name = f'{col}.png'
                            file_list = positions['obj2']
                            file_index = file_list.index(file_name)
                            surface = graphics['obj2'][file_index]
                            Tile((x, y), [self.visible_sprites], 'obj2', surface)

        self.player = Player(
            (4500, 5000), 
            [self.visible_sprites], 
            self.obstacles_sprites, 
            self.create_attack, 
            self.destroy_attack, 
            self.create_magic
        )

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def destroy_attack(self):
        if self.current_attack:
            print(self.current_attack)
            self.current_attack.kill()
            print(self.current_attack)
        self.current_attack = None
    
    def create_magic(self, style, strength, cost):
        print(style)
        print(strength)
        print(cost)

    def run(self):
        #update and run the game
        self.visible_sprites.update()
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #General setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #Creating the floor
        self.floor_surface = pygame.image.load('images/main/map.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0, 0))
    
    def custom_draw(self, player):

        #We get the offset to center the camera of the player
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #Drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)