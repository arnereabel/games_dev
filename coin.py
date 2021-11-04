# PYGAMEZERO is code die voor ons is geschreven (modules) om te helpen onze game te schrijven.
# hiervoor zijn 3 grote delen nodig : 1 de sandwich import pgzrun [importeert pygamezero) en onderaan pgzrun.go() (die roept de functie aan om de game te runnen
#                                     2 de draw functie die onze player, coin, vijanden op het scherm tekent
#                                     3 de update functie die kijkt of er veranderingen zijn aangebracht door middel van bijv inputs in het spel (met spatiebar springen)
# de update en draw functie werken samen om het spel te spelen


# importeer de game modules

import pgzrun
from PIL import Image
from random import randint

# verklein de foto en geef ze de juste naam om te gebruikennin het spel

# image = Image.open("images/coin1.png")
# image = image.resize((15, 25), Image.ANTIALIAS)
# image.save("images/coin.png")
#
# image = Image.open("images/player1.png")
# image = image.resize((50, 75), Image.ANTIALIAS)
# image.save("images/player.png")
#
# image = Image.open("images/enemy1.png")
# image = image.resize((100, 150), Image.ANTIALIAS)
# image.save("images/enemy.png")

# create the GAME WINDOW
# omdat we het game van niets opbouwen wil dit zeggen dat we ook het scherm moeten bouwen waarin het game getoond word
# 2 constanten  breedte en hoogte worden hiervoor gedefineerd (we zeggen dit zijn constanten  omdat ze doorheen het spel hetzelfde blijven)
# je kan ze natuurlijk wel veranderen voordat je het game runt om het aan te passen aan je voorkeur
from pgzero.actor import Actor


BREEDTE = 1200      # WIDTH
HOOGTE = 900        # HEIGHT


# maak een variabele om de score en tijd op te slagen, (variable veranderen tijdens het spelverloop, bv score = 0  je maakt een punt en score is dan score = 1 )
# maak ook een variabele van het type BOOLEAN die aangeeft of het spel nog bezig is of dat je verloren hebt
SCORE = 0
TIJD = 10          # de tijd variabele loopt af
GAME_OVER = False  # BOOLEAN waardes kunnen alleen True of False zijn    (oftewel waarde 1 = True , waarde 0 = False)


# create actors and starting positions  (actors zijn bv je personage waarmee je speelt, je vijanden of de coins die je moet verzamelen)
# je geeft ze ook een  startpositie mee in het spel , bv x = 150 en y = 100 om de positie te bepalen in het spelscherm)
player = Actor("player")          # creër de player actor met referentie naar je player.png image die in het spel je personage representeert
player.pos = 100, 100             # startpositie voor de speler

coin = Actor("coin")
coin.pos = 200, 200

enemy = Actor('enemy')
enemy.pos = 500, 500

# DRAW the game # creër de draw functie die pgzero gebruikt om het spel te tekenen op het scherm
def draw():                     # hier moet de functie 2 dingen doen 1/ de achtergrond opvullen met een kleur  2/ de twee Actors (player, coin) op het scherm tekenen
    screen.fill('black')        # .fill vult het scherm met een kleur
    player.draw()               # .draw tekent de player.png op het scherm
    coin.draw()                 # .draw tekent de coin.png op het scherm
    enemy.draw()
    # draw the score
    screen.draw.text("Score : " + str(SCORE), topleft=(10,10), fontsize= 25)   # screen (op het scherm) draw (teken) text (letters of cijfers) "SCORE" de waarde in de variabele SCORE // tekent een 0 op het scherm

    # draw TIMER (tijdklok)
    screen.draw.text("Timer: " + str(round(TIJD)), topright=(790,10), fontsize = 25)

    if GAME_OVER :               # if GAME_OVER == True:    hier verkort als  if GAME_OVER:
        screen.fill('white')
        screen.draw.text("GAME OVER     your Score = " + str(SCORE), topleft=(10,10), fontsize= 50, color='black')


# plaats de coins in verchillende willekeurige plaatsen
def place_coin():
    coin.x = randint(150, 800)        #binnen het scherm van pygame plaats deze functie de coins willekeurige op het scherm   (150, (BREEDTE - 150))  (HOOGTE - 150))
    coin.y = randint(150, 600)

# runs when time reaches 0
def time_up():
    global GAME_OVER
    GAME_OVER = True



# UPDATE the game # kijkt of er veranderingen zijn aangebracht en dan de nieuwe situatie laat weten aan draw die het dan weer tekent op je scherm met de veranderingen.
def update(delta):             # add a parameter delta inside of the update function parentheses   delta is builtin in python that keeps track of how much time has passed
    global SCORE               # GLOBAL is een keyword in python dat je toelaat om een eerder toegewezen variable buiten de FUNCTIE te veranderen.  (indien je dit niet doet kun je het wel gebruiken maar niet veranderen
    global TIJD

    #updates the timer
    TIJD -= delta
    if TIJD <= 0:
        time_up()

# we kijken hier of de speler de coin raakt of niet # colliderect is een interne functie van de pygame module die checkt of 2 boundries elkaar raken
    if player.colliderect(coin): # in python is er een onzichtbaar vierkant dat rondom de verschillende Actors word getekend die toelaat om te checken of 2 veschillende Actors elkaar raken en dan mogelijk een actie veroorzaken
        SCORE += 10              # telt 10 punten op bij de player score variable SCORE         ( SCORE = 0  ---> ( SCORE = SCORE + 10) ---> SCORE = 10)
        TIJD += 1
        place_coin()              # we roepen hier de functie place_coin op die nadat we met de player sprite  de coin sprite aanraken erna de coin op een willekeurige positie op het scherm zet

    if player.colliderect(enemy):
        time_up()

    if keyboard.left and player.x > 0:           # in pygame kun je gebruik maken van het keyboard door het te refereren[keyboard) en en de te gebruiken toets erna te typen met een .  bv .left  dan checkt pygame of je de linkse pijltjestoets indrukt
        player.x -= 4           # met de linkse pijltjestoets indrukt ga je -4 pixels naar links op de x as van het scherm    - x +     - x is dus links naar het scherm

    if keyboard.right and player.x < BREEDTE:
        player.x += 4

    if keyboard.up and player.y < HOOGTE:
        player.y -= 4

    if keyboard.down and player.y > 0:
        player.y += 4


    # laat de enemy de player volgen
    if enemy.x < player.x:
        enemy.x += 1

    if enemy.x > player.x:
        enemy.x -= 1

    if enemy.y < player.y:
        enemy.y += 1

    if enemy.y > player.y:
        enemy.y -= 1




# plaats hier de random place_coin functie  om aan het begin van het spel de coin telkens op een andere plaats te zetten
place_coin()


# laat de code werken met pgzrun.go()   RUN the CODE
pgzrun.go()