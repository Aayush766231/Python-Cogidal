import pygame

def game():
    pygame.init()

    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("My first screen")
    color = (0, 0, 0)
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        screen.fill((255, 255, 255))
        if pressed[pygame.K_LEFT]:
            pygame.draw.rect(screen, color, pygame.Rect(213, 200, 213, 80))
            pygame.draw.polygon(screen, color, ((640//4, 240), (213, 180), (213, 300)))
            text = pygame.font.Font(None, 36).render("Pressing left", True, pygame.Color("black"))
            textRect = text.get_rect(center=(640 // 2, 480 // 2 + 110))
            screen.blit(text, textRect)
        elif pressed[pygame.K_RIGHT]:
            pygame.draw.rect(screen, color, pygame.Rect(213, 200, 213, 80))
            pygame.draw.polygon(screen, color, ((640*3//4, 240), (416, 180), (416, 300)))
            text = pygame.font.Font(None, 36).render("Pressing right", True, pygame.Color("black"))
            textRect = text.get_rect(center=(640 // 2, 480 // 2 + 110))
            screen.blit(text, textRect)
        elif pressed[pygame.K_UP]:
            pygame.draw.rect(screen, color, pygame.Rect(280, 160, 80, 160))
            pygame.draw.polygon(screen, color, ((240, 160), (320, 120), (400, 160)))
            text = pygame.font.Font(None, 36).render("Pressing up", True, pygame.Color("black"))
            textRect = text.get_rect(center=(640 // 2, 480 // 2 + 110))
            screen.blit(text, textRect)
        elif pressed[pygame.K_DOWN]:
            pygame.draw.rect(screen, color, pygame.Rect(280, 120, 80, 160))
            pygame.draw.polygon(screen, color, ((240, 280), (320, 320), (400, 280)))
            text = pygame.font.Font(None, 36).render("Pressing down", True, pygame.Color("black"))
            textRect = text.get_rect(center=(640 // 2, 480 // 2 + 110))
            screen.blit(text, textRect)
        pygame.display.flip()

if __name__ == "__main__":
    game()