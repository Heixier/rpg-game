import pygame

import gui.screen as scr

from scenes.scene import Scene
from scenes.action import Action
from scenes.end import GameOver
from scenes.gamelog import GameLog
from gui import ui_functions
import resources.images as images

from classes import class_functions as cf

from scenes.options import Options


class Play(Scene):
    def __init__(self, game):
        super().__init__(game)
        pygame.mixer.music.load(self.game.audio_handler.battle_bgm_path)
        pygame.mixer.music.play(-1, 0, 1000)

        self.stat_guis = pygame.sprite.Group()

        self.background = images.background_img
        self.ui_sprites = pygame.sprite.Group()
        self.pointer = 1

        # self.crazy_guy = cf.create_unit("William", "Reaper", "enemy", self.game)
        # self.crazy_guy.dx, self.crazy_guy.dy = 5, 5

        # testing coordinates
        self.player_positions = [
            (self.xc - 250, self.yc - 150),
            (self.xc - 375, self.yc),
            (self.xc - 500, self.yc + 150),
        ]

        self.enemy_positions = [
            (self.xc + 250, self.yc - 150),
            (self.xc + 375, self.yc),
            (self.xc + 500, self.yc + 150),
        ]
        cf.set_positions(self.player_positions, self.game.players)
        cf.set_positions(self.enemy_positions, self.game.enemies)

        # Move sprites off-screen (due to how rubbish this 1 am code is, only low multiples of 10 will work)
        for sprite in self.game.players:
            sprite.rect.center = sprite.rect.center[0] - 200, sprite.rect.center[1]
            sprite.dx = 20

        for sprite in self.game.enemies:
            sprite.rect.center = sprite.rect.center[0] + 200, sprite.rect.center[1]
            sprite.dx = -20

        # The reason why there is a dictionary and a list is because the list gets changed during game iteration
        # While the alive dictionary needs to be fixed with keys so it doesn't keep appending
        # Since it needs to be updated every loop

        self.selected_unit = self.game.players.sprites()[0]

        # Add pointer sprite
        self.ui_sprites.add(ui_functions.TargetImage(self, images.player_target))

        self.button_dict = self.create_dict(self.button_sprites)
        self.text_dict = self.create_dict(self.text_sprites)

        ui_functions.create_info_guis(self.game)

    def update(self, actions):
        self.update_alive_dict()

        # No idea why I didn't have to do .sprites()
        for sprite in self.game.all_units:
            rectx, recty = sprite.rect.center

            # The random is just to shuffle them a bit so they eventually fall into the range and stop
            if rectx > scr.SCREEN_WIDTH:
                sprite.rect.center = 0, recty
            elif rectx < 0:
                sprite.rect.center = scr.SCREEN_WIDTH, recty

            if sprite.position[0] - 5 < rectx < sprite.position[0] + 5:
                sprite.dx = 0

        if not self.alive_player_dict:
            victor = "enemy"
            next_scene = GameOver(self.game, victor)
            next_scene.start_scene()
            self.game.event_log.append(f"{victor.capitalize()} TEAM HAS WON!\n")
            return

        if not self.alive_enemy_dict:
            victor = "player"
            next_scene = GameOver(self.game, victor)
            next_scene.start_scene()
            self.game.event_log.append(f"{victor.capitalize()} TEAM HAS WON!\n")
            return

        for sprite in self.game.all_units.sprites():
            sprite.selected = False

        for sprite in self.ui_sprites.sprites():
            sprite.selected = True

        self.pointer = self.pointer % len(self.alive_player_dict)

        self.selected_unit = list(self.alive_player_dict.values())[self.pointer]

        if actions['space']:
            next_scene = GameLog(self.game)
            next_scene.start_scene()

        if actions["escape"]:
            next_scene = Options(self.game)
            next_scene.start_scene()

        if actions["down"]:
            self.pointer += 1

        if actions["up"]:
            self.pointer -= 1

        if actions["enter"]:

            # Create an anchor as well using self because we will be referencing this scene in the other menu scenes
            next_scene = Action(self.game, self.selected_unit, self)

            for sprite in self.ui_sprites:
                sprite.selected = False
            next_scene.start_scene()

        self.ui_sprites.update()
        self.game.stat_guis.update()
        self.game.all_units.update()

        self.game.reset_keys()

    def render(self, screen):
        screen.blit(
            pygame.transform.scale(
                self.background, (self.game.screen_width, self.game.screen_height)
            ),
            (0, 0),
        )

        # Rendering order (last to render = on top)
        self.game.all_units.draw(screen)
        self.ui_sprites.draw(screen)
        self.game.stat_guis.draw(screen)

        # for group in self.custom_groups:
        #     group.draw(screen)
