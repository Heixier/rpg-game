import gui.screen as sc
import pygame



def draw_menu0():
    sc.screen.fill((0, 0, 0))
    sc.draw_text ('    PROGRAMMING ASSIGNMENT', sc.font.menu_font, sc.font.TEXT_COL,160 , sc.SCREEN_HEIGHT / 2 - 120)
    sc.draw_text('TURN-BASED RPG', sc.font.menu_font, sc.font.TEXT_COL, 280, sc.SCREEN_HEIGHT / 2 - 80)
    sc.draw_text('>>> PRESS SPACEBAR TO START THE GAME <<<', sc.font.gui_font, sc.font.YELLOW , 200 , sc.SCREEN_HEIGHT/ 2 + 150)  
