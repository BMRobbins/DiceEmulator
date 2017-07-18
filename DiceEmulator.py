import pygame, sys, random, time
from pygame.locals import *

def init_display():
    global DISPLAYSURF, ONE, TWO, THREE, FOUR, FIVE, SIX, FPSCLOCK, FPS, BASICFONT
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((500,400), 0, 32)
    pygame.display.set_caption('Dice Emulator')
    FPS = 30
    FPSCLOCK = pygame.time.Clock()

def load_die_images():
    global DISPLAYSURF, ONE, TWO, THREE, FOUR, FIVE, SIX, FPSCLOCK, FPS, BASICFONT
    ONE = pygame.image.load('die1.png')
    TWO = pygame.image.load('die2.png')
    THREE = pygame.image.load('die3.png')
    FOUR = pygame.image.load('die4.png')
    FIVE = pygame.image.load('die5.png')
    SIX = pygame.image.load('die6.png')

def load_roll_button_and_dicepair():
    global ROLLBUTTON, dicepair
    ROLLBUTTON = button(pygame.image.load('roll.png'),pygame.image.load('roll2.png'),pygame.image.load('roll3.png'), 165, 245, 180, 64)
    dicepair = dice(100,50,260,50)

def set_background_and_text_fields():
    global BLUE, BLACK, fontObj, textSurfaceObj, textRectObj
    BLUE = (0, 0 , 255)
    BLACK = (0,0,0)
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Total: ' + str(dicepair.get_total()), True, BLACK, BLUE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (255, 350)

def update_and_redraw_screen():
    global DISPLAYSURF, ROLLBUTTON, textSurfaceObj, textRectObj, dicepair, FPSCLOCK
    DISPLAYSURF.fill(BLUE)
    ROLLBUTTON.draw()
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    dicepair.update()
    pygame.display.update()
    FPSCLOCK.tick(FPS)
        
def handle_events():
    global DISPLAYSURF, ONE, TWO, THREE, FOUR, FIVE, SIX, FPSCLOCK, FPS, BASICFONT, ROLLBUTTON, dicepair, BLUE, BLACK, fontObj, textSurfaceObj, textRectObj
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_r:
                    dicepair.dice_roll_animation()
                    textSurfaceObj = fontObj.render('Total: ' + str(dicepair.get_total()), True, BLACK, BLUE)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (270, 350)
            elif event.type == MOUSEMOTION:
                pos = event.pos
                if ROLLBUTTON.mouse_click_on_button(pos):
                    ROLLBUTTON.highlight_button_color()
                else:
                    ROLLBUTTON.orig_button_color()
                
            elif event.type == MOUSEBUTTONDOWN:
                pos = event.pos
                if ROLLBUTTON.mouse_click_on_button(pos):
                    ROLLBUTTON.press_button_color()

            elif event.type == MOUSEBUTTONUP:
                pos = event.pos
                if ROLLBUTTON.mouse_click_on_button(pos):
                    ROLLBUTTON.orig_button_color('update')
                    ROLLBUTTON.highlight_button_color()
                    ROLLBUTTON.draw()
                    dicepair.dice_roll_animation()
                    textSurfaceObj = fontObj.render('Total: ' + str(dicepair.get_total()), True, BLACK, BLUE)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (270, 350)
        update_and_redraw_screen()
        
    
def main():
    global DISPLAYSURF, ONE, TWO, THREE, FOUR, FIVE, SIX, FPSCLOCK, FPS, BASICFONT, ROLLBUTTON, dicepair, BLUE, BLACK, fontObj, textSurfaceObj, textRectObj
    init_display()
    load_die_images()
    load_roll_button_and_dicepair()
    set_background_and_text_fields()
    handle_events()

class dice():
    def __init__(self, x, y,x2,y2):
        self.number = 1
        self.number2 = 1
        self.total = 2
        self.x, self.y, self.x2, self.y2 = x, y, x2, y2
        self.possible = [1,2,3,4,5,6]

    def random_roll(self):
        self.number = random.choice(self.possible)
        self.number2 = random.choice(self.possible)

    def dice_roll_animation(self):
        counter = 0
        while counter < 60:
            self.random_roll()
            self.update()
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            counter += 1
        self.total = self.number + self.number2       

    def update(self):
        if self.number == 1:
            DISPLAYSURF.blit(ONE, (self.x,self.y))

        elif self.number == 2:
            DISPLAYSURF.blit(TWO, (self.x, self.y))

        elif self.number == 3:
            DISPLAYSURF.blit(THREE, (self.x, self.y))

        elif self.number == 4:
            DISPLAYSURF.blit(FOUR, (self.x,self.y))

        elif self.number == 5:
            DISPLAYSURF.blit(FIVE, (self.x,self.y))

        else:
            DISPLAYSURF.blit(SIX, (self.x,self.y))

        if self.number2 == 1:
            DISPLAYSURF.blit(ONE, (self.x2,self.y2))

        elif self.number2 == 2:
            DISPLAYSURF.blit(TWO, (self.x2, self.y2))

        elif self.number2 == 3:
            DISPLAYSURF.blit(THREE, (self.x2, self.y2))

        elif self.number2 == 4:
            DISPLAYSURF.blit(FOUR, (self.x2,self.y2))

        elif self.number2 == 5:
            DISPLAYSURF.blit(FIVE, (self.x2,self.y2))

        else:
            DISPLAYSURF.blit(SIX, (self.x2,self.y2))

    def get_total(self):
        return self.total

class button():
    def __init__(self, buttonimage, highlightimage, pressimage, x, y, width, height, sound = None):
        self.buttonimage = buttonimage
        self.highlightimage = highlightimage
        self.pressimage = pressimage
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.image = buttonimage
        self.yd = 5
        self.xd = 5
        self.sound = sound
        

    def draw(self):
        if self.sound:
            self.sound.play()
        DISPLAYSURF.blit(self.image, (self.x, self.y))

    def update_keydown(self):
        self.y += self.yd

    def update_keyup(self):
        self.y -= self.yd

    def highlight_button_color(self):
        self.image = self.highlightimage

    def orig_button_color(self,update = None):
        self.image = self.buttonimage
        if update == 'update':
            self.update_keyup()

    def press_button_color(self):
        self.image = self.pressimage
        self.update_keydown()

    def mouse_click_on_button(self, mouseclick):
        return mouseclick[0] >= self.x and mouseclick[0] <= self.x + self.width and mouseclick[1] >=  self.y and mouseclick[1] <= self.y  + self.height
    
  

        
        
        

if __name__ == '__main__':
    main()
    
