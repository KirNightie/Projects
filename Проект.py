#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:39:19 2023

@author: nikitazaleskij
"""

import pygame
import random 
from random import randint

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 1430
HEIGHT = 800

'''
self.r = 20 + 5 * self.level
'''



class Hero:
    def __init__(self, orient, screen):
        self.screen = screen
        self.color = GREEN
        self.x = 80
        self.y = 400
        self.vx = 5
        self.vy = 5
        self.score = 0
        self.level = 1
        self.r = 17
        self.orient = orient
    def drive(self, direction):
        if direction == 'left' and self.x > 20:
            self.x-=self.vx
        elif direction == 'right' and self.x < 1400:
            self.x+=self.vx
        elif direction == 'up' and self.y < 760:
            self.y+=self.vy
        elif direction == 'down' and self. y > 20:
            self.y-=self.vy
      
    def level_up(self):
        if self.score >= 1313:
            self.level = 27
        elif self.score >= 1219:
            self.level = 26
        elif self.score >= 1128:
            self.level = 25
        elif self.score >= 1041:
            self.level = 24
        elif self.score >= 957:
            self.level = 23
        elif self.score >= 877:
            self.level = 22
        elif self.score >= 800:
            self.level = 21
        elif self.score >= 727:
            self.level = 20
        elif self.score >= 657:
            self.level = 19
        elif self.score >= 591:
            self.level = 18
        elif self.score >= 528:
            self.level = 17
        elif self.score >= 469:
            self.level = 16
        elif self.score >= 413:
            self.level = 15
        elif self.score >= 361:
            self.level = 14
        elif self.score >= 312:
            self.level = 13
        elif self.score >= 267:
            self.level = 12
        elif self.score >= 225:
            self.level = 11
        elif self.score >= 187:
            self.level = 10
        elif self.score >= 152:
            self.level = 9
        elif self.score >= 121:
            self.level = 8
        elif self.score >= 93:
            self.level = 7
        elif self.score >= 69:
            self.level = 6
        elif self.score >= 48:
            self.level = 5
        elif self.score >= 31:
            self.level = 4
        elif self.score >= 17:
            self.level = 3
        elif self.score >= 7:
            self.level = 2
        else:
            self.level = 1
        
    def hittest(self, Target):
        if (Target.x - self.x) ** 2 + (Target.y - self.y) ** 2 < (self.r+Target.r) ** 2:
            return True
        else:
            return False


class Target:
    def __init__(self, y, screen: pygame.Surface):
        self.screen = screen
        self.x = 1470
        if hero.level == 1:
            self.level = random.randint(1, 3)
        if hero.level == 2:
            self.level = random.randint(1,4)
        if hero.level >= 3:
            self.level = random.randint(hero.level-2, hero.level+2)
        self.r = 17
        self.new_target()
        self.y = y
        if hero.level > 18:
            self.vx = random.random() + 1 + 1 // 9
        else:
            self.vx = random.random() + 1 + hero.level // 9

    def new_target(self):
        self.x = 1470
        self.r = 17
        self.color = RED
        if hero.level == 1:
            self.level = random.randint(1, 3)
        if hero.level == 2:
            self.level = random.randint(1,4)
        if hero.level >= 3:
            self.level = random.randint(hero.level-2, hero.level+2)
            
    
    def move(self):
        self.x -= self.vx

        




pygame.init()
skin_1_right = pygame.image.load('ryba_1_pravaya.png')
skin_1_right = pygame.transform.scale(skin_1_right, (100, 40))
skin_1_left = pygame.image.load('ryba_1_levaya.png')
skin_1_left = pygame.transform.scale(skin_1_left, (100, 40))

skin_2_right = pygame.image.load('ryba_2_pravaya.png')
skin_2_right = pygame.transform.scale(skin_2_right, (100, 40))
skin_2_left = pygame.image.load('ryba_2_levaya.png')
skin_2_left = pygame.transform.scale(skin_2_left, (100, 40))

skin_3_right = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_3_pravaya.png')
skin_3_right = pygame.transform.scale(skin_3_right, (100, 40))
skin_3_left = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_3_levaya.png')
skin_3_left = pygame.transform.scale(skin_3_left, (100, 40))

skin_4_right = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_4_pravaya.png')
skin_4_right = pygame.transform.scale(skin_4_right, (100, 40))
skin_4_left = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_4_levaya.png')
skin_4_left = pygame.transform.scale(skin_4_left, (100, 40))

skin_5_right = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_5_pravaya.png')
skin_5_right = pygame.transform.scale(skin_5_right, (100, 40))
skin_5_left = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_5_levaya.png')
skin_5_left = pygame.transform.scale(skin_5_left, (100, 40))

skin_6_right = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_6_pravaya.png')
skin_6_right = pygame.transform.scale(skin_6_right, (100, 40))
skin_6_left = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_6_levaya.png')
skin_6_left = pygame.transform.scale(skin_6_left, (100, 40))

skin_7_right = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_7_pravaya.png')
skin_7_right = pygame.transform.scale(skin_7_right, (100, 40))
skin_7_left = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_7_levaya.png')
skin_7_left = pygame.transform.scale(skin_7_left, (100, 40))

skin_8_right = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_8_pravaya.png')
skin_8_right = pygame.transform.scale(skin_8_right, (100, 40))
skin_8_left = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_8_levaya.png')
skin_8_left = pygame.transform.scale(skin_8_left, (100, 40))

skin_9_right = pygame.image.load('/Users/kirillatmazitov/Downloads/ryba_9_pravaya.png')
skin_9_right = pygame.transform.scale(skin_9_right, (100, 40))
skin_9_left = pygame.image.load('//Users/kirillatmazitov/Downloads/ryba_9_levaya.png')
skin_9_left = pygame.transform.scale(skin_9_left, (100, 40))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Игра "Рыбка"')
bg = pygame.image.load('/Users/kirillatmazitov/Documents/Программирование/Практика/Проект/Fon_rybka.jpg')
bg = pygame.transform.scale(bg, (1430, 800))
bg_begin = pygame.image.load('/Users/kirillatmazitov/Downloads/Задний фон.jpeg')
bg_begin = pygame.transform.scale(bg_begin, (1430, 800))
finished = False
f1 = pygame.font.Font(None, 36)
while not finished:
    end = False
    menu = False
    gamed = False
    win = True
    while not menu:
        hero = Hero(1, screen)
        target_1 = Target(randint(10, 60), screen)
        target_2 = Target(randint(110, 150), screen)
        target_3 = Target(randint(200, 240), screen)
        target_4 = Target(randint(290, 330), screen)
        target_5 = Target(randint(380, 420), screen)
        target_6 = Target(randint(470, 510), screen)
        target_7 = Target(randint(560, 600), screen)
        target_8 = Target(randint(650, 690), screen)
        target_9 = Target(randint(740, 780), screen)
        target_10 = Target(randint(830, 870), screen)
        
        end = False
        gamed = False
        screen.blit(bg_begin, (0, 0))
        text_begin = f1.render('Press (P) to play the game or (E) to exit', True , (180, 0, 0), YELLOW)
        screen.blit(text_begin, (500,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = True
                gamed = True
                finished = True
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    menu = True 
                if event.key == pygame.K_e:
                    menu = True 
                    gamed = True
                    finished = True
                    end = True
        pygame.display.update()
    while not gamed:
        screen.blit(bg, (0, 0))
        text_score = f1.render('Score:'f'{hero.score}', True , (0, 0, 0), GREY)
        screen.blit(text_score, (0, 0))
        if hero.orient == 1 and hero.level >= 1 and hero.level <= 3:
            screen.blit(skin_1_right, (hero.x - 60, hero.y - 20))
        elif hero.orient == 2 and hero.level >= 1 and hero.level <= 3:
            screen.blit(skin_1_left, (hero.x - 40, hero.y - 20))
        elif hero.orient == 1 and hero.level >= 4 and hero.level <= 6:
            screen.blit(skin_2_right, (hero.x - 60, hero.y - 20))
        elif hero.orient == 2 and hero.level >= 4 and hero.level <= 6:
            screen.blit(skin_2_left, (hero.x - 40, hero.y - 20))
        elif hero.orient == 1 and hero.level >= 7 and hero.level <= 9:
            screen.blit(skin_3_right, (hero.x - 60, hero.y - 20))
        elif hero.orient == 2 and hero.level >= 7 and hero.level <= 9:
            screen.blit(skin_3_left, (hero.x - 40, hero.y - 20))  
        elif hero.orient == 1 and hero.level >= 10 and hero.level <= 12:
            screen.blit(skin_4_right, (hero.x - 60, hero.y - 20))
        elif hero.orient == 2 and hero.level >= 10 and hero.level <= 12:
            screen.blit(skin_4_left, (hero.x - 40, hero.y - 20))        
        elif hero.orient == 1 and hero.level >= 13 and hero.level <= 15:
            screen.blit(skin_5_right, (hero.x - 60, hero.y - 20))
        elif hero.orient == 2 and hero.level >= 13 and hero.level <= 15:
            screen.blit(skin_5_left, (hero.x - 40, hero.y - 20))            
        elif hero.orient == 1 and hero.level >= 16 and hero.level <= 18:
            screen.blit(skin_6_right, (hero.x - 60, hero.y - 20))
        elif hero.orient == 2 and hero.level >= 16 and hero.level <= 18:
            screen.blit(skin_6_left, (hero.x - 40, hero.y - 20))            
        elif hero.orient == 1 and hero.level >= 19 and hero.level <= 21:
            screen.blit(skin_7_right, (hero.x - 60, hero.y - 20))
        elif hero.orient == 2 and hero.level >= 19 and hero.level <= 21:
            screen.blit(skin_7_left, (hero.x - 40, hero.y - 20))            
        elif hero.orient == 1 and hero.level >= 22 and hero.level <= 24:
            screen.blit(skin_8_right, (hero.x - 60, hero.y - 20))
        elif hero.orient == 2 and hero.level >= 22 and hero.level <= 24:
            screen.blit(skin_8_left, (hero.x - 40, hero.y - 20))            
        elif hero.orient == 1 and hero.level >= 25 and hero.level < 27:
            screen.blit(skin_9_right, (hero.x - 60, hero.y - 20))
        elif hero.orient == 2 and hero.level >= 25 and hero.level < 27:
            screen.blit(skin_9_left, (hero.x - 40, hero.y - 20))
        elif hero.level == 27:
            gamed = True
            win = False
      
        if target_1.level >= 1 and target_1.level <= 3:
            screen.blit(skin_1_left, (target_1.x - 40, target_1.y - 20))
        elif target_1.level >= 4 and target_1.level <= 6:
            screen.blit(skin_2_left, (target_1.x - 40, target_1.y - 20))
        elif target_1.level >= 7 and target_1.level <= 9:
            screen.blit(skin_3_left, (target_1.x - 40, target_1.y - 20))
        elif target_1.level >= 10 and target_1.level  <= 12:
            screen.blit(skin_4_left, (target_1.x - 40, target_1.y - 20))       
        elif target_1.level >= 13 and target_1.level  <= 15:
            screen.blit(skin_5_left, (target_1.x - 40, target_1.y - 20))  
        elif target_1.level >= 16 and target_1.level <= 18:
            screen.blit(skin_6_left, (target_1.x - 40, target_1.y - 20))          
        elif target_1.level >= 19 and target_1.level <= 21:
            screen.blit(skin_7_left, (target_1.x - 40, target_1.y - 20))         
        elif target_1.level >= 22 and target_1.level <= 24:
            screen.blit(skin_8_left, (target_1.x - 40, target_1.y - 20))  
        elif target_1.level >= 25 and target_1.level <= 27:
            screen.blit(skin_9_left, (target_1.x - 40, target_1.y - 20))
        
        if target_2.level >= 1 and target_2.level <= 3:
            screen.blit(skin_1_left, (target_2.x - 40, target_2.y - 20))
        elif target_2.level >= 4 and target_2.level <= 6:
            screen.blit(skin_2_left, (target_2.x - 40, target_2.y - 20))
        elif target_2.level >= 7 and target_2.level <= 9:
            screen.blit(skin_3_left, (target_2.x - 40, target_2.y - 20))
        elif target_2.level >= 10 and target_2.level  <= 12:
            screen.blit(skin_4_left, (target_2.x - 40, target_2.y - 20))       
        elif target_2.level >= 13 and target_2.level  <= 15:
            screen.blit(skin_5_left, (target_2.x - 40, target_2.y - 20))  
        elif target_2.level >= 16 and target_2.level <= 18:
            screen.blit(skin_6_left, (target_2.x - 40, target_2.y - 20))          
        elif target_2.level >= 19 and target_2.level <= 21:
            screen.blit(skin_7_left, (target_2.x - 40, target_2.y - 20))         
        elif target_2.level >= 22 and target_2.level <= 24:
            screen.blit(skin_8_left, (target_2.x - 40, target_2.y - 20))  
        elif target_2.level >= 25 and target_2.level <= 27:
            screen.blit(skin_9_left, (target_2.x - 40, target_2.y - 20))
            
        if target_3.level >= 1 and target_3.level <= 3:
            screen.blit(skin_1_left, (target_3.x - 40, target_3.y - 20))
        elif target_3.level >= 4 and target_3.level <= 6:
            screen.blit(skin_2_left, (target_3.x - 40, target_3.y - 20))
        elif target_3.level >= 7 and target_3.level <= 9:
            screen.blit(skin_3_left, (target_3.x - 40, target_3.y - 20))
        elif target_3.level >= 10 and target_3.level  <= 12:
            screen.blit(skin_4_left, (target_3.x - 40, target_3.y - 20))       
        elif target_3.level >= 13 and target_3.level  <= 15:
            screen.blit(skin_5_left, (target_3.x - 40, target_3.y - 20))  
        elif target_3.level >= 16 and target_3.level <= 18:
            screen.blit(skin_6_left, (target_3.x - 40, target_3.y - 20))          
        elif target_3.level >= 19 and target_3.level <= 21:
            screen.blit(skin_7_left, (target_3.x - 40, target_3.y - 20))         
        elif target_3.level >= 22 and target_3.level <= 24:
            screen.blit(skin_8_left, (target_3.x - 40, target_3.y - 20))  
        elif target_3.level >= 25 and target_3.level <= 27:
            screen.blit(skin_9_left, (target_3.x - 40, target_3.y - 20))
            
        if target_4.level >= 1 and target_4.level <= 3:
            screen.blit(skin_1_left, (target_4.x - 40, target_4.y - 20))
        elif target_4.level >= 4 and target_4.level <= 6:
            screen.blit(skin_2_left, (target_4.x - 40, target_4.y - 20))
        elif target_4.level >= 7 and target_4.level <= 9:
            screen.blit(skin_3_left, (target_4.x - 40, target_4.y - 20))
        elif target_4.level >= 10 and target_4.level  <= 12:
            screen.blit(skin_4_left, (target_4.x - 40, target_4.y - 20))       
        elif target_4.level >= 13 and target_4.level  <= 15:
            screen.blit(skin_5_left, (target_4.x - 40, target_4.y - 20))  
        elif target_4.level >= 16 and target_4.level <= 18:
            screen.blit(skin_6_left, (target_4.x - 40, target_4.y - 20))          
        elif target_4.level >= 19 and target_4.level <= 21:
            screen.blit(skin_7_left, (target_4.x - 40, target_4.y - 20))         
        elif target_4.level >= 22 and target_4.level <= 24:
            screen.blit(skin_8_left, (target_4.x - 40, target_4.y - 20))  
        elif target_4.level >= 25 and target_4.level <= 27:
            screen.blit(skin_9_left, (target_4.x - 40, target_4.y - 20))
        
        if target_5.level >= 1 and target_5.level <= 3:
            screen.blit(skin_1_left, (target_5.x - 40, target_5.y - 20))
        elif target_5.level >= 4 and target_5.level <= 6:
            screen.blit(skin_2_left, (target_5.x - 40, target_5.y - 20))
        elif target_5.level >= 7 and target_5.level <= 9:
            screen.blit(skin_3_left, (target_5.x - 40, target_5.y - 20))
        elif target_5.level >= 10 and target_5.level  <= 12:
            screen.blit(skin_4_left, (target_5.x - 40, target_5.y - 20))       
        elif target_5.level >= 13 and target_5.level  <= 15:
            screen.blit(skin_5_left, (target_5.x - 40, target_5.y - 20))  
        elif target_5.level >= 16 and target_5.level <= 18:
            screen.blit(skin_6_left, (target_5.x - 40, target_5.y - 20))          
        elif target_5.level >= 19 and target_5.level <= 21:
            screen.blit(skin_7_left, (target_5.x - 40, target_5.y - 20))         
        elif target_5.level >= 22 and target_5.level <= 24:
            screen.blit(skin_8_left, (target_5.x - 40, target_5.y - 20))  
        elif target_5.level >= 25 and target_5.level <= 27:
            screen.blit(skin_9_left, (target_5.x - 40, target_5.y - 20))
            
        if target_6.level >= 1 and target_6.level <= 3:
            screen.blit(skin_1_left, (target_6.x - 40, target_6.y - 20))
        elif target_6.level >= 4 and target_6.level <= 6:
            screen.blit(skin_2_left, (target_6.x - 40, target_6.y - 20))
        elif target_6.level >= 7 and target_6.level <= 9:
            screen.blit(skin_3_left, (target_6.x - 40, target_6.y - 20))
        elif target_6.level >= 10 and target_6.level  <= 12:
            screen.blit(skin_4_left, (target_6.x - 40, target_6.y - 20))       
        elif target_6.level >= 13 and target_6.level  <= 15:
            screen.blit(skin_5_left, (target_6.x - 40, target_6.y - 20))  
        elif target_6.level >= 16 and target_6.level <= 18:
            screen.blit(skin_6_left, (target_6.x - 40, target_6.y - 20))          
        elif target_6.level >= 19 and target_6.level <= 21:
            screen.blit(skin_7_left, (target_6.x - 40, target_6.y - 20))         
        elif target_6.level >= 22 and target_6.level <= 24:
            screen.blit(skin_8_left, (target_6.x - 40, target_6.y - 20))  
        elif target_6.level >= 25 and target_6.level <= 27:
            screen.blit(skin_9_left, (target_6.x - 40, target_6.y - 20))
            
        if target_7.level >= 1 and target_7.level <= 3:
            screen.blit(skin_1_left, (target_7.x - 40, target_7.y - 20))
        elif target_7.level >= 4 and target_7.level <= 6:
            screen.blit(skin_2_left, (target_7.x - 40, target_7.y - 20))
        elif target_7.level >= 7 and target_7.level <= 9:
            screen.blit(skin_3_left, (target_7.x - 40, target_7.y - 20))
        elif target_7.level >= 10 and target_7.level  <= 12:
            screen.blit(skin_4_left, (target_7.x - 40, target_7.y - 20))       
        elif target_7.level >= 13 and target_7.level  <= 15:
            screen.blit(skin_5_left, (target_7.x - 40, target_7.y - 20))  
        elif target_7.level >= 16 and target_7.level <= 18:
            screen.blit(skin_6_left, (target_7.x - 40, target_7.y - 20))          
        elif target_7.level >= 19 and target_7.level <= 21:
            screen.blit(skin_7_left, (target_7.x - 40, target_7.y - 20))         
        elif target_7.level >= 22 and target_7.level <= 24:
            screen.blit(skin_8_left, (target_7.x - 40, target_7.y - 20))  
        elif target_7.level >= 25 and target_7.level <= 27:
            screen.blit(skin_9_left, (target_7.x - 40, target_7.y - 20))
            
        if target_8.level >= 1 and target_8.level <= 3:
            screen.blit(skin_1_left, (target_8.x - 40, target_8.y - 20))
        elif target_8.level >= 4 and target_8.level <= 6:
            screen.blit(skin_2_left, (target_8.x - 40, target_8.y - 20))
        elif target_8.level >= 7 and target_8.level <= 9:
            screen.blit(skin_3_left, (target_8.x - 40, target_8.y - 20))
        elif target_8.level >= 10 and target_8.level  <= 12:
            screen.blit(skin_4_left, (target_8.x - 40, target_8.y - 20))       
        elif target_8.level >= 13 and target_8.level  <= 15:
            screen.blit(skin_5_left, (target_8.x - 40, target_8.y - 20))  
        elif target_8.level >= 16 and target_8.level <= 18:
            screen.blit(skin_6_left, (target_8.x - 40, target_8.y - 20))          
        elif target_8.level >= 19 and target_8.level <= 21:
            screen.blit(skin_7_left, (target_8.x - 40, target_8.y - 20))         
        elif target_8.level >= 22 and target_8.level <= 24:
            screen.blit(skin_8_left, (target_8.x - 40, target_8.y - 20))  
        elif target_8.level >= 25 and target_8.level <= 27:
            screen.blit(skin_9_left, (target_8.x - 40, target_8.y - 20))
            
        if target_9.level >= 1 and target_9.level <= 3:
            screen.blit(skin_1_left, (target_9.x - 40, target_9.y - 20))
        elif target_9.level >= 4 and target_9.level <= 6:
            screen.blit(skin_2_left, (target_9.x - 40, target_9.y - 20))
        elif target_9.level >= 7 and target_9.level <= 9:
            screen.blit(skin_3_left, (target_9.x - 40, target_9.y - 20))
        elif target_9.level >= 10 and target_9.level  <= 12:
            screen.blit(skin_4_left, (target_9.x - 40, target_9.y - 20))       
        elif target_9.level >= 13 and target_9.level  <= 15:
            screen.blit(skin_5_left, (target_9.x - 40, target_9.y - 20))  
        elif target_9.level >= 16 and target_9.level <= 18:
            screen.blit(skin_6_left, (target_9.x - 40, target_9.y - 20))          
        elif target_9.level >= 19 and target_9.level <= 21:
            screen.blit(skin_7_left, (target_9.x - 40, target_9.y - 20))         
        elif target_9.level >= 22 and target_9.level <= 24:
            screen.blit(skin_8_left, (target_9.x - 40, target_9.y - 20))  
        elif target_9.level >= 25 and target_9.level <= 27:
            screen.blit(skin_9_left, (target_9.x - 40, target_9.y - 20))
            
        if target_10.level >= 1 and target_10.level <= 3:
            screen.blit(skin_1_left, (target_10.x - 40, target_10.y - 20))
        elif target_10.level >= 4 and target_10.level <= 6:
            screen.blit(skin_2_left, (target_10.x - 40, target_10.y - 20))
        elif target_10.level >= 7 and target_10.level <= 9:
            screen.blit(skin_3_left, (target_10.x - 40, target_10.y - 20))
        elif target_10.level >= 10 and target_10.level  <= 12:
            screen.blit(skin_4_left, (target_10.x - 40, target_10.y - 20))       
        elif target_10.level >= 13 and target_10.level  <= 15:
            screen.blit(skin_5_left, (target_10.x - 40, target_10.y - 20))  
        elif target_10.level >= 16 and target_10.level <= 18:
            screen.blit(skin_6_left, (target_10.x - 40, target_10.y - 20))          
        elif target_10.level >= 19 and target_10.level <= 21:
            screen.blit(skin_7_left, (target_10.x - 40, target_10.y - 20))         
        elif target_10.level >= 22 and target_10.level <= 24:
            screen.blit(skin_8_left, (target_10.x - 40, target_10.y - 20))  
        elif target_10.level >= 25 and target_10.level <= 27:
            screen.blit(skin_9_left, (target_10.x - 40, target_10.y - 20))
            
        
        
        
        
        
        text1 = f1.render(f'{hero.level}', True , (0, 0, 0), GREY)
        text2 = f1.render(f'{target_1.level}', True , (0, 0, 0), GREY)
        text3 = f1.render(f'{target_2.level}', True , (0, 0, 0), GREY)
        text4 = f1.render(f'{target_3.level}', True , (0, 0, 0), GREY)
        text5 = f1.render(f'{target_4.level}', True , (0, 0, 0), GREY)
        text6 = f1.render(f'{target_5.level}', True , (0, 0, 0), GREY)
        text7 = f1.render(f'{target_6.level}', True , (0, 0, 0), GREY)
        text8 = f1.render(f'{target_7.level}', True , (0, 0, 0), GREY)
        text9 = f1.render(f'{target_8.level}', True , (0, 0, 0), GREY)
        text10 = f1.render(f'{target_9.level}', True , (0, 0, 0), GREY)
        text11 = f1.render(f'{target_10.level}', True , (0, 0, 0), GREY)
        screen.blit(text1, (hero.x - 8, hero.y - 8))
        screen.blit(text2, (target_1.x - 8, target_1.y - 8))
        screen.blit(text3, (target_2.x - 8, target_2.y - 8))
        screen.blit(text4, (target_3.x - 8, target_3.y - 8))
        screen.blit(text5, (target_4.x - 8, target_4.y - 8))
        screen.blit(text6, (target_5.x - 8, target_5.y - 8))
        screen.blit(text7, (target_6.x - 8, target_6.y - 8))
        screen.blit(text8, (target_7.x - 8, target_7.y - 8))
        screen.blit(text9, (target_8.x - 8, target_8.y - 8))
        screen.blit(text10, (target_9.x - 8, target_9.y - 8))
        screen.blit(text11, (target_10.x - 8, target_10.y - 8))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if not False in keys: print(keys)
        if keys[1073741906]: 
            hero.drive('down')
        elif keys[1073741905]: 
            hero.drive('up')
        elif keys[1073741903]: 
            hero.drive('right')
            hero.orient = 1
        elif keys[1073741904]: 
            hero.drive('left')
            hero.orient = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                gamed = True  
                end = True
        if hero.hittest(target_1):
            if target_1.level <= hero.level:
                hero.score += target_1.level
                target_1.new_target()
                hero.level_up()
            else:
                gamed = True
        if hero.hittest(target_2):
            if target_2.level <= hero.level:
                hero.score += target_2.level
                target_2.new_target()
                hero.level_up()
            else:
                gamed = True
        if hero.hittest(target_3):
            if target_3.level <= hero.level:
                hero.score += target_3.level
                target_3.new_target()
                hero.level_up()
            else:
                gamed = True
        if hero.hittest(target_4):
            if target_4.level <= hero.level:
                hero.score += target_4.level
                target_4.new_target()
                hero.level_up()
            else:
                gamed = True
        if hero.hittest(target_5):
            if target_5.level <= hero.level:
                hero.score += target_5.level
                target_5.new_target()
                hero.level_up()
            else:
                gamed = True
        if hero.hittest(target_6):
            if target_6.level <= hero.level:
                hero.score += target_6.level
                target_6.new_target()
                hero.level_up()
            else:
                gamed = True
        if hero.hittest(target_7):
           if target_7.level <= hero.level:
               hero.score += target_7.level
               target_7.new_target()
               hero.level_up()
           else:
               gamed = True
        if hero.hittest(target_8):
           if target_8.level <= hero.level:
               hero.score += target_8.level
               target_8.new_target()
               hero.level_up()
           else:
               gamed = True
        if hero.hittest(target_9):
           if target_9.level <= hero.level:
               hero.score += target_9.level
               target_9.new_target()
               hero.level_up()
           else:
               gamed = True
        if hero.hittest(target_10):
           if target_10.level <= hero.level:
               hero.score += target_10.level
               target_10.new_target()
               hero.level_up()
           else:
               gamed = True 
        target_1.move()
        target_2.move()
        target_3.move()
        target_4.move()
        target_5.move()
        target_6.move()
        target_7.move()
        target_8.move()
        target_9.move()
        target_10.move()
        
        if target_1.x < -40:
            target_1.new_target()
        if target_2.x < -40:
            target_2.new_target()
        if target_3.x < -40:
            target_3.new_target()
        if target_4.x < -40:
            target_4.new_target()
        if target_5.x < -40:
            target_5.new_target()
        if target_6.x < -40:
            target_6.new_target()
        if target_7.x < -40:
            target_7.new_target()
        if target_8.x < -40:
            target_8.new_target()
        if target_9.x < -40:
            target_9.new_target()
        if target_10.x < -40:
            target_10.new_target()
    while not win:
        screen.blit(bg, (0, 0))
        text_end = f1.render('Congratulations, you win. Press (M) to go to main menu', True , (180, 0, 0), YELLOW)
        screen.blit(text_end, (400,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                gamed = True
                finished = True
                menu = True
                win = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    end = True 
                    win = True
        pygame.display.update()
    while not end:
        screen.blit(bg, (0, 0))
        text_end = f1.render('Game over. Press (M) to go to main menu', True , (180, 0, 0), YELLOW)
        screen.blit(text_end, (500,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                gamed = True
                finished = True
                menu = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    end = True 
        pygame.display.update()
pygame.quit()