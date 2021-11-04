import pygame                                                        # import modules
import random
from pygame.locals import *

screen_width = 800                                                  # constants for screen size
screen_height = 800

class Player(pygame.sprite.Sprite):                                 # defines the Player class object that inherits the Sprite base info # inside the class parentheses (no parameters) but inheritance of a pre defined objects base info gets passed
    def __init__(self):                                             # Constructor -  constructs the object   this is the function(def) that creates this object
        super(Player, self).__init__()                              # no we tell the game and constructor to inherit the information from pygame.sprite.Sprite info to create the Player object with the basic information from Sprite with the keyword SUPER
        self.surface = pygame.image.load('images/player.png')       # self here is the object we are creating as we are in the class that defines it, like you are a class and self refers to yourself wich is the class here
        self.rect = self.surface.get_rect()                            # sets the rectangle box around the image


pygame.init()                                                       # intiialze all imported pygame modules

clock = pygame.time.Clock()                                         # set the clock for use with frame rate etc

screen = pygame.display.set_mode((screen_width, screen_height))     #  create the screen object

player = Player()                                                   # creates the player  aka it creates an object from the Player class and stores it in the player variable

all_sprites = pygame.sprite.Group()                                 # create groups to hold our objects/sprites
all_sprites.add(player)                                             # with the .add function we can add objects to our group

keeprunning = True                                                  # set a variable as boolean  to keep the main loop alive

while keeprunning:                                                  # while keeprunning == True
    for event in pygame.event.get():                                # check every event in the game
        if event.type == QUIT:                                      # if the close window x is clicked call the quit function
            pygame.quit()

    for entity in all_sprites:                                      # for every object/sprite in the all_sprites variable
        screen.blit(entity.surface, entity.rect)                    # with the .blit() function builtin function of pygame we draw each sprite/object in the all_sprites variable

    pygame.display.flip()                                           # updates screen