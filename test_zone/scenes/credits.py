import pygame
import sys

import gui2.ui_functions as ui_functions
from scenes.scene import Scene
import gui2.screen as scr
import resources2.images

credit_section = [50, None, "yellow"]
credit_title = [40, None, "white"]
credit_desc = [40, None, "green"]
credit_name = [35, "segoeuiemoji", "white"]

class Credits(Scene):
    def __init__(self, game: object):
        super().__init__(game)
        self.background = resources2.images.credits_background
        self.credits = pygame.sprite.Group()
        
        # Can't go below integer so use fps to slow it down below 1
        self.game.fps = 60
        self.falling_speed = (0, -1)

        self.credits_header = [
            ('[ Credits ]', *credit_section, True, scr.SCREEN_HEIGHT - 50),
            ('PSB INTRODUCTION TO PROGRAMMING ASSIGNMENT', *credit_desc, True, scr.SCREEN_HEIGHT),
            ('GAME CREATED BY (GROUP A1) ', *credit_desc, True, scr.SCREEN_HEIGHT + 50)
            ]

        self.credits_body = [
            ('[ Members ]', *credit_section, True, scr.SCREEN_HEIGHT + 300),
            
            ('Group Leader', *credit_title, True, scr.SCREEN_HEIGHT + 350),
            ('Desmond Foo Fong Yoong 👑', *credit_name, True, scr.SCREEN_HEIGHT + 400),
            ('Group Members', *credit_title, True, scr.SCREEN_HEIGHT + 550),
            ('Haarith Bin Naguri Ibrahim', *credit_name, True, scr.SCREEN_HEIGHT + 600),
            
            ('IMPORTANT: IF YOU SEE YOUR NAME BELOW', *credit_desc, True, scr.SCREEN_HEIGHT + 800),
            ('PLEASE CHANGE IT BEFORE THE DEADLINE', *credit_desc, True, scr.SCREEN_HEIGHT + 850),
            ('(because at least you bothered to run the game and check)', 30, None, "grey", True, scr.SCREEN_HEIGHT + 900),
            ('THANKS — RZ', *credit_desc, True, scr.SCREEN_HEIGHT + 950),
            ('he\'s so nice he wanted to give everyone the same grade', 25, "segoeuiemoji", "grey", True, scr.SCREEN_HEIGHT + 1150),
            ('...but I\'m not that nice 😊', 25, "segoeuiemoji", "grey", True, scr.SCREEN_HEIGHT + 1175),
            ('this is what you get for not contributing 👻', 25, "segoeuiemoji", "crimson", True, scr.SCREEN_HEIGHT + 1225),

            ('0 GitHub Commits', *credit_section, True, scr.SCREEN_HEIGHT + 1600),
            ('Haohong Luo ', *credit_name, True, scr.SCREEN_HEIGHT + 1650),
            ('Xu Xiang (Ye Xuxiang) Yap ', *credit_name, True, scr.SCREEN_HEIGHT + 1700),
            ('Yi Soon Pong ', *credit_name, True, scr.SCREEN_HEIGHT + 1750),
            ('Qiao Er Kang', *credit_name, True, scr.SCREEN_HEIGHT + 1800)
            ]

        self.credits_footer = [
            ('THANKS FOR PLAYING', *credit_section, True, scr.SCREEN_HEIGHT + 2100),
            (' ', *credit_section, True, scr.SCREEN_HEIGHT + 2150) # padding
            ]

        # Add the sections you want to load into this list
        self.credits_list = [self.credits_header, self.credits_body, self.credits_footer]
                    
        for section in self.credits_list:
            for credit in section:
                credit_sprite = ui_functions.TextSprite(*credit, False, *self.falling_speed)
                self.credits.add(credit_sprite)

    def update(self, actions):
        if actions["escape"] or actions["enter"]:
            self.game.fps = 60
            self.exit_scene()
            
        self.credits.update()
        self.game.reset_keys()
        
        # Go back once credits are finished
        if len(self.credits) == 0:
            self.game.fps = 60
            self.exit_scene()
        
    def render(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.game.screen_width, self.game.screen_height)), (0, 0))
        self.credits.draw(self.game.canvas)
        