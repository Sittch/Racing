import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("CarCrash.wav")
pygame.mixer.music.load("IntotheSunset.wav")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0, 200, 0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

car_width = 75
car_height = 75

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game Title Here')
clock = pygame.time.Clock()

carIMG = pygame.image.load('racecar.png')
caricon = pygame.image.load('caricon.png')
pygame.display.set_icon(caricon)

pause = False
#crash = False

def things_dodged(count):
    font = pygame.font.SysFont('comicsansms', 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, block_color, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carIMG,(x,y))

def text_objects(text, font):
    textSurface= font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('comicsansms',115)
    TextSurface, TextRectangle = text_objects(text, largeText)
    TextRectangle.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurface, TextRectangle)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    
    largeText = pygame.font.SysFont('comicsansms',115)
    TextSurface, TextRectangle = text_objects("You Crashed", largeText)
    TextRectangle.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurface, TextRectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)


        button("Play Again",150,450,100,50,green,bright_green, game_loop)
        button("Quit",550,450,100,50,red,bright_red, quitgame)

        
        mouse = pygame.mouse.get_pos()

        
        pygame.display.update()
        clock.tick(15)


def button(msg,x,y,w,h,ic,ac,action=None):
    #i(nactive color), a(ctive color)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
                
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont('comicsansms',20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont('comicsansms',115)
    TextSurface, TextRectangle = text_objects("Paused", largeText)
    TextRectangle.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurface, TextRectangle)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)


        button("Continue",150,450,100,50,green,bright_green, unpause)
        button("Quit",550,450,100,50,red,bright_red, quitgame)

        
        mouse = pygame.mouse.get_pos()

        
        pygame.display.update()
        clock.tick(15)



def game_intro():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms',115)
        TextSurface, TextRectangle = text_objects("Game Title Here", largeText)
        TextRectangle.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurface, TextRectangle)

        button("GO!",150,450,100,50,green,bright_green, game_loop)
        button("Quit",550,450,100,50,red,bright_red, quitgame)

        
        mouse = pygame.mouse.get_pos()

        
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change
        gameDisplay.fill(white)
        
        #things(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x< 0:
            gameExit = True

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width+= (dodged * 1.2)


        if y < thing_starty+thing_height:

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx:
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
