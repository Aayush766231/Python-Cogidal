import pygame
#Setting up everything
pygame.init()
screenWidth, screenHeight = 500, 500
#screen
displayScreen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Adding image + background image")
#2 images
backgroundImage = pygame.transform.scale(
    pygame.image.load('background.png').convert(),(screenWidth, screenHeight))
penguinImage = pygame.transform.scale(
    pygame.image.load('hello penguin.png').convert_alpha(), (200, 200))
penguinRect = penguinImage.get_rect(center= (screenWidth//2, screenHeight // 2 - 30))
#TEXT
text = pygame.font.Font(None, 36).render("Hello World", True, pygame.Color("black"))
textRect = text.get_rect(center=(screenWidth // 2, screenHeight // 2 + 110))
#actual screen
def gameLoop():
    #time
    clock = pygame.time.Clock()
    #while loop for screen
    running = True
    while running:
        #checks for exitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #displayes the images + text
        displayScreen.blit(backgroundImage, (0, 0))
        displayScreen.blit(penguinImage, penguinRect)
        displayScreen.blit(text, textRect)
        #updates screen at 30 fps
        pygame.display.flip()
        clock.tick(30)
    #quits function after clicked
    pygame.quit()

if __name__ == "__main__":
    gameLoop()