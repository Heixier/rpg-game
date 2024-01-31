import pygame
import random
import screen as sc
import damagetext as dt
import font
import gamelog

pygame.init()

class fighter():
    def __init__(self,x,y,name,namepic,max_hp,strength,defence):
        self.name = name 
        self.namepic = namepic
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.defence = defence
        self.alive = True
        self.animationlist= []
        self.frame_index = 0
        self.action = 0 #0:idle, 1:attack , 2:hurt , 3:dead , 4Ldefence
        self.update_time = pygame.time.get_ticks()

        #load image
        temp_list = []
        for i in range(1,5):
            img = pygame.image.load(f'picture/{self.namepic}/idle/{i}.png')
            self.image = pygame.transform.scale(img, (img.get_width()*3 ,img.get_height()*3))
            temp_list.append(self.image)
        self.animationlist.append(temp_list) #list of list

        #load attack
        temp_list = []
        for i in range(1,10):
            if {self.namepic} == "knightpic" :
                img = pygame.image.load(f'picture/{self.namepic}/attack/{i}.png')
                self.image = pygame.transform.scale(img, (img.get_width()*6 ,img.get_height()*6))
        
            else:
                img = pygame.image.load(f'picture/{self.namepic}/attack/{i}.png')
                self.image = pygame.transform.scale(img, (img.get_width()*3 ,img.get_height()*3))
            temp_list.append(self.image)
        self.animationlist.append(temp_list)

        #load hurt image
        temp_list = []
        for i in range(1,3):
            img = pygame.image.load(f'picture/{self.namepic}/hurt/{i}.png')
            self.image = pygame.transform.scale(img, (img.get_width()*3 ,img.get_height()*3))
            temp_list.append(self.image)
        self.animationlist.append(temp_list)

        #load dead image
        temp_list = []
        for i in range(1,9):
            img = pygame.image.load(f'picture/{self.namepic}/death/{i}.png')
            self.image = pygame.transform.scale(img, (img.get_width()*3 ,img.get_height()*3))
            temp_list.append(self.image)
        self.animationlist.append(temp_list)

        self.image = self.animationlist[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def update(self):
        animation_cooldown = 100
        #handle animation
        #update image
        self.image = self.animationlist[self.action][self.frame_index]
        #check if enought time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1 
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animationlist[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animationlist[self.action]) - 1
            else:
                self.idle()

    def idle(self):
        #set variable to idle
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def attack(self, target):
        #deal damage to the enemy
        rand = random.randint(-5, 5)
        damage = (self.strength + rand) - (self.defence + rand)
        target.hp -= damage 
        #run enemy animation
        target.hurt()
        #check is target died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        damage_text = dt.DamageText(target.rect.centerx, target.rect.y, str(damage), font.RED)
        damage_text_group.add(damage_text)
        #the names for game log (-haarith, needs work not showing name of the user)
        gamelog.game_logs.append(f'{self.name} attacked {target.name} for {damage} damage')
        gamelog.game_logs.append(f'{target.name} blocked {(target.defence + rand)} damage from {self.name}')

        

        #set variable to attack
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        #set variable to hurt
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        #set variable to dead
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        sc.screen.blit(self.image, self.rect)
        sc.draw_text(self.name, font.hp_font, font.RED, self.rect.centerx - 30, self.rect.y - 20)
    

damage_text_group = pygame.sprite.Group()


