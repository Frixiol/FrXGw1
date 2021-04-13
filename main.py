
# Commencer le 13/04/2021 pour Frixiol vs Gwen 1, fais en moins 27 heure, 21h>0h

import pygame
from pygame import mixer
import math
import random
import sys

white, black, blue, red  = (230, 230, 230), (20, 20, 20), (0, 154, 255), (230, 0, 0)
width, height = 800, 800

pygame.init()
pygame.display.set_caption("FrXGw")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
background = pygame.image.load('assets/2773642.jpg')
background = pygame.transform.scale(background,(width, height))
main_background = pygame.image.load('assets/1630800.jpg')
main_background = pygame.transform.scale(main_background,(width, height))
end_background = pygame.image.load('assets/2773742.jpg')
end_background = pygame.transform.scale(end_background,(width, height))
mixer.music.load('assets/BeepBox-Song.wav')
mixer.music.play(-1)

menu_run = True
fps = 60
chrono = 0
mouse_pos=[0,0]
speed = 15
accelerationx,accelerationy = 10,10
bullets = []
enemies = []
pygame.mouse.set_visible(False)


font = pygame.font.Font(pygame.font.get_default_font(), 36)
font_round = pygame.font.Font(pygame.font.get_default_font(), 50)

class Player(pygame.sprite.Sprite):

    def __init__(self,px,py,state):
        super().__init__()
        self.player_posx = px
        self.player_posy = py
        self.state = state
        self.multishoot = False
        self.image = pygame.image.load('assets/pixil-frame-0(1).png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(100,100))


    def get_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.dx = mouse_x - player.player_posx
        self.dy = mouse_y - player.player_posy
        if -speed < self.dx < speed and -speed < self.dy < speed:
            pass
        else:
            player.player_move(mouse_x, mouse_y)


    def player_move(self,x,y):
        self.dx = x - self.player_posx
        self.dy = y - self.player_posy
        distance = math.sqrt(self.dx * self.dx + self.dy * self.dy)
        self.dx /= distance
        self.dy /= distance
        self.dx *= speed
        self.dy *= speed
        self.player_posx += self.dx
        self.player_posy += self.dy
        return self.player_posx, self.player_posy

    def create_bullet(self,shoot,number):
        self.multishoot = shoot
        self.bullets_shoot = number
        self.bullet_time = chrono
        bullet = Bullet(self.player_posx,self.player_posy,self.state)
        pygame.sprite.Group.add(bullet)
        return bullet

    def change_state(self,direction):
        if direction == "right":
            self.state = (self.state%4)+1
            self.image = pygame.transform.rotate(self.image, -90)
        else:
            self.state = (self.state-1)
            if self.state == 0:
                self.state = 4
            self.image = pygame.transform.rotate(self.image, 90)


class Bullet():

    def __init__(self,x,y,state):
        self.bullet_posx = x
        self.bullet_posy = y
        self.state = state
        self.image = pygame.image.load('assets/pixil-frame-0(3).png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 100))
        if self.state == 2:
            self.image = pygame.transform.rotate(self.image, -90)
        if self.state == 3:
            self.image = pygame.transform.rotate(self.image, 180)
        if self.state == 4:
            self.image = pygame.transform.rotate(self.image, 90)

    def update(self):
        if self.state == 1:
            self.bullet_posy -= speed
        elif self.state == 2:
            self.bullet_posx += speed
        elif self.state == 3:
            self.bullet_posy += speed
        elif self.state == 4:
            self.bullet_posx -= speed


class Enemy(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.enemy_posx = x
        self.enemy_posy = y
        self.enemy_health = 3
        self.image = pygame.image.load('assets/pixil-frame-0(2).png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 100))

    def enemy_move(self,x,y):
        self.dx = x - self.enemy_posx
        self.dy = y - self.enemy_posy
        distance = math.sqrt(self.dx * self.dx + self.dy * self.dy)
        self.dx /= distance
        self.dy /= distance
        self.dx *= speed/5
        self.dy *= speed/5
        self.enemy_posx += self.dx
        self.enemy_posy += self.dy
        return self.enemy_posx, self.enemy_posy

    def hitted(self):
        self.enemy_health -= 1

class Round():

    def __init__(self):
        self.round_count = 0
        self.time_count = chrono

    def create_enemy(self):
        if random.randint(0,1) == 1:
            enemy_x = random.randint(0,width)
            if random.randint(0,1) == 1:
                enemy_y = height
            else:
                enemy_y = 0
        else:
            enemy_y = random.randint(0,height)
            if random.randint(0,1) == 1:
                enemy_x = width
            else:
                enemy_x = 0
        enemies.append(Enemy(enemy_x,enemy_y))

def render():
    screen.blit(background, dest=(0, 0))

    screen.blit(player.image, (player.player_posx - 50, player.player_posy - 50))
    text_x = pygame.font.Font.render(font, str(math.floor(chrono)), True, white)
    screen.blit(text_x, dest=(0, 0))
    text_x = pygame.font.Font.render(font, str(round.round_count), True, white)
    screen.blit(text_x, dest=(width / 2, 0))


player = Player(width/2,height/2,1)
round = Round()


def main_menu():
    global menu_run
    while menu_run == True:
        clock.tick(fps)
        screen.blit(main_background, dest=(0, 0))
        text_x = pygame.font.Font.render(font_round, "Frixiol Game", True, white)
        screen.blit(text_x, dest=(width / 3.2, height / 6))
        text_x = pygame.font.Font.render(font_round, "Menu", True, black)
        screen.blit(text_x, dest=(width /2.4, height / 3 ))
        text_x = pygame.font.Font.render(font_round, "Press Space to start", True, black)
        screen.blit(text_x, dest=(width /5, height / 2 - 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     menu_run = False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        pygame.display.update()

def end_menu():
    while True:
        clock.tick(fps)
        screen.blit(end_background, dest=(0, 0))
        text_x = pygame.font.Font.render(font_round, "YOU DIED", True, white)
        screen.blit(text_x, dest=(width /2.8, height / 3.5 ))
        text_x = pygame.font.Font.render(font_round, "Round lived:", True, white)
        screen.blit(text_x, dest=(width /3.7, height / 2.5))
        text_x = pygame.font.Font.render(font_round, str(round.round_count), True, white)
        screen.blit(text_x, dest=(width /1.5, height / 2.5))
        text_x = pygame.font.Font.render(font_round, "Timer:", True, white)
        screen.blit(text_x, dest=(width / 2.7, height / 2.2))
        text_x = pygame.font.Font.render(font_round, str(math.floor(chrono)), True, white)
        screen.blit(text_x, dest=(width / 1.7, height / 2.2))
        text_x = pygame.font.Font.render(font_round, "Press Space to quit", True, white)
        screen.blit(text_x, dest=(width / 5, height / 1.5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     sys.exit()

        pygame.display.update()

main_menu()

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(player.create_bullet(True,0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.change_state("right")
            if event.key == pygame.K_q:
                player.change_state("left")
            if event.key == pygame.K_ESCAPE:
                run = False
                sys.exit()
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    player.get_mouse()
    render()

    if player.multishoot == True:
        if chrono - player.bullet_time >= 0.1:
            if player.bullets_shoot < 2:
                player.bullets_shoot += 1
                bullets.append(player.create_bullet(player.multishoot, player.bullets_shoot))
                shoot_sound = mixer.Sound('assets/shoot.wav')
                shoot_sound.play()
            else:
                player.bullets_shoot = 0
                player.multishoot = False

    if len(enemies) == 0:
        if chrono - round.time_count >= 3:
            round.round_count += 1
            for n in range(round.round_count):
                round.create_enemy()
        else:
            text_x = pygame.font.Font.render(font_round, "ROUND:", True, white)
            screen.blit(text_x, dest=(width/3, height/2-40))
            text_x = pygame.font.Font.render(font_round,str(round.round_count+1), True, white)
            screen.blit(text_x, dest=(width/1.7, height / 2 - 40))


    for enemy in enemies:
        enemy.enemy_move(player.player_posx,player.player_posy)
        screen.blit(enemy.image, (enemy.enemy_posx - 50, enemy.enemy_posy - 50))
        if enemy.enemy_health <= 0:
            enemies.pop(enemies.index(enemy))
            enemy_sound = mixer.Sound('assets/enemy_explosion.wav')
            enemy_sound.play()
            if len(enemies) == 0:
                round.time_count = chrono
            continue
        if enemy.enemy_posx - 50 < player.player_posx < enemy.enemy_posx + 50:
            if enemy.enemy_posy - 50 < player.player_posy < enemy.enemy_posy + 50:
                player_sound = mixer.Sound('assets/player_explosion.wav')
                player_sound.play()
                end_menu()

    for bullet in bullets:
        bullet.update()
        screen.blit(bullet.image, (bullet.bullet_posx - 50, bullet.bullet_posy - 50))
        if len(enemies)>0:
            for enemy in enemies:
                if enemy.enemy_posx-50 <bullet.bullet_posx < enemy.enemy_posx+50:
                    if enemy.enemy_posy-50 <bullet.bullet_posy < enemy.enemy_posy+50:
                        bullets.pop(bullets.index(bullet))
                        enemy.hitted()
                        break
        elif width < bullet.bullet_posx or bullet.bullet_posx < 0:
            bullets.pop(bullets.index(bullet))
        elif height < bullet.bullet_posy or bullet.bullet_posy < 0:
            bullets.pop(bullets.index(bullet))

    chrono += 1/fps

    pygame.display.update()

pygame.quit()
