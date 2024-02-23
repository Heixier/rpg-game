import pygame
from pathlib import Path

# This part is for my Black formatter extension don't worry about it
# fmt: off

#menu background
menubackground_img = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/menubackground.png')}")

options_background = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/option.jpg')}")
credits_background = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/space.png')}")
char_create_background = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/grunge.jpg')}")

#background image
background_img = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/throne.png')}")

#panel image
panel_img = pygame.image.load(f"{Path('test_zone/resources2/images/backgrounds/parchment.png')}")

#load image
#load victory and defeat images
victory_img = pygame.image.load(f"{Path('test_zone/resources2/images/ui_elements/victory.png')}")
victory_img = pygame.transform.scale(victory_img, (600,500))

defeat_img = pygame.image.load(f"{Path('test_zone/resources2/images/ui_elements/defeat.png')}")
defeat_img = pygame.transform.scale(defeat_img, (600,500))


player_target = pygame.image.load(f"{Path('test_zone/resources2/images/ui_elements/player_target.png')}")
player_target = pygame.transform.scale(player_target, (192, 192))

enemy_target = pygame.image.load(f"{Path('test_zone/resources2/images/ui_elements/enemy_target.png')}")
enemy_target = pygame.transform.scale(enemy_target, (192, 192))
