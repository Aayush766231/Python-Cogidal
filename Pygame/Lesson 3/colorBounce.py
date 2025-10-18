import pygame
import random

pygame.init()

spriteColorChange = pygame.USEREVENT + 1
bgColorChange = pygame.USEREVENT + 2

#sprite colors
white = pygame.Color("white")
yellow = pygame.Color("yellow")
magenta = pygame.Color("magenta")
orange = pygame.Color("orange")
spriteColor = pygame.Color(random.choice([0, 255]), random.choice([0, 255]), 0)
#background colors
blue = pygame.Color("blue")
lightBlue = pygame.Color('lightblue')
darkBlue = pygame.Color("darkblue")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #rectangle
        self.rect = self.image.get_rect()
        #velocity
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        #movement
        self.rect.move_ip(self.velocity)
        #boundary hit?
        boundaryHit = False
        #check for collision
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundaryHit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundaryHit = True
        #calls on event to change colors
        if boundaryHit:
            pygame.event.post(pygame.event.Event(spriteColorChange))
            pygame.event.post(pygame.event.Event(bgColorChange))
    #changes sprite color
    def colorChange(self):
        self.image.fill(random.choice([yellow, orange, magenta, white]))
#background color changing
def changeBackgroundColor():
    global bgColor
    bgColor = random.choice([blue, lightBlue, darkBlue])

#sprite group
allSpritesList = pygame.sprite.Group()
#creation of sprite
sp1 = Sprite(white, 20, 30)
#random sprite position
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
#add sprite to group
allSpritesList.add(sp1)

#window
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Screen Bounce")
bgColor = blue
screen.fill(bgColor)

#loop control
running = True
clock = pygame.time.Clock()

#game loop
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == spriteColorChange:
            sp1.colorChange()
        elif event.type == bgColorChange:
            changeBackgroundColor()

    #update list based on changing sprite
    allSpritesList.update()
    #changes screen color
    screen.fill(bgColor)
    #sprites onto screen after everything is checked
    allSpritesList.draw(screen)

    #screen refresh
    pygame.display.flip()
    #240 fps
    clock.tick(240)

pygame.quit()