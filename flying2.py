import pygame                                                        # import modules
import random

import self as self
from pygame.locals import *

screen_width = 800                                                  # constants for screen size
screen_height = 800

class Player(pygame.sprite.Sprite):                                 # defines the Player class object that inherits the Sprite base info # inside the class parentheses (no parameters) but inheritance of a pre defined objects base info gets passed
    def __init__(self):                                             # Constructor -  constructs the object   this is the function(def) that creates this object
        super(Player, self).__init__()                              # no we tell the game and constructor to inherit the information from pygame.sprite.Sprite info to create the Player object with the basic information from Sprite with the keyword SUPER
        self.surface = pygame.image.load('assets/jet.png')          # self here is the object we are creating as we are in the class that defines it, like you are a class and self refers to yourself wich is the class here
        self.rect = self.surface.get_rect()                         # sets the rectangle box around the image

    def update(self, pressed_keys):                                 # move the sprite based on keyboard input ... parameters in the fucntion are   self wich refers to the player class .. pressed_keys for the keyboard input


        if pressed_keys[K_UP]:                                      # checks wich key is pressed
            self.rect.move_ip(0,-5)                                 #  object/self gets grabbed by its boundary rectangle and moved in place where (x parameter, y parameter)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # keeps the objects on the screen
        if self.rect.left < 0:                                      # checks if the left boundrie of the rectangle around the object is less then 0 on the x axis
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 800:
            self.rect.bottom = 800



class Enemy(pygame.sprite.Sprite):                                 # enemy object based on extending the pygame Sprite
    def __init__(self):                                            # we are creating our self here inside the class  // based on the Sprite info and additional
        super(Enemy, self).__init__()
        self.surface = pygame.image.load('assets/missile.png')

        self.rect = self.surface.get_rect(
            center = (
                random.randint(screen_width + 20, screen_width + 100),         # x value   give an x value so that the missile spawns offscreen so anything above 800 as that is the width of the screen
                random.randint(10, screen_height - 10)                         # y value
            )
        )

        self.speed = random.randint(5,20)

    def update(self):                                                          # this function moves the missele and then removes them once they go offscreen or x < 0
        self.rect.move_ip(-self.speed, 0)                                      # update the missile so that it moves to the left

        if self.rect.right < 0:
            self.kill()                                                         # when the missile goes ofscreen remove the missile so we do need to track its position offsdcreen by the pc








pygame.init()                                                       # intiialze all imported pygame modules

clock = pygame.time.Clock()                                         # set the clock for use with frame rate etc

screen = pygame.display.set_mode((screen_width, screen_height))     #  create the screen object

Addenemy = pygame.USEREVENT + 1                                     # custom event for adding a new enemy   every time we add an enemy we add a user event
pygame.time.set_timer(Addenemy, 250)                               # set how many missele are spawned,  here its value used is in ms   so 1000ms  is  one missile a second


player = Player()                                                   # creates the player  aka it creates an object from the Player class and stores it in the player variable

enemies = pygame.sprite.Group()                                     # creates the enemy object goup to uptdate all the enemies at once


all_sprites = pygame.sprite.Group()                                 # create groups to hold our objects/sprites
all_sprites.add(player)                                             # with the .add function we can add objects to our group

keeprunning = True                                                  # set a variable as boolean  to keep the main loop alive


# main loop
while keeprunning:                                                  # while keeprunning == True
    for event in pygame.event.get():                                # check every event in the game
        if event.type == QUIT:                                      # if the close window x is clicked call the quit function
            pygame.quit()

        elif event.type == Addenemy:                                # check for the event type Addenemy
            new_enemy = Enemy()                                     # using the Enemy class , create a new sprite and store it in new_enemy, then add your new created enemy in the all_sprites group
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # get the set of keys pressed and check for user input and move the jet
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # update the enemy position
    enemies.update()

    # fill the screen
    screen.fill((136,205,249))                                         # 2 parentheses / 1 for parameter of color and 1 for the holding opthe color fill the screen with a blue collor according to rgb standard   this also eliminated the previously drawn objects by coloring them



    for entity in all_sprites:                                      # runs for every object/sprite in the all_sprites variable
        screen.blit(entity.surface, entity.rect)                    # with the .blit() function builtin function of pygame we draw each sprite/object in the all_sprites variable

    pygame.display.flip()                                           # updates screen

    clock.tick(30)                                                  # sets the clock at 30 fps    so the update runs 1/30 sec