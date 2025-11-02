import math
import random
import pygame
import time

pygame.init()
pygame.mixer.init()

#constants
screenWidth = 800
screenHeight = 500
playerX = 370
playerY = 380
enemyMaxY = 150
enemyMinY = 50
enemySpeedX = 4
enemySpeedY = 40
bulletSpeed = 10
collisionDistance = 27

#screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Space Invaders With Music")
background = pygame.image.load("background.png")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
fps = pygame.time.Clock()
pygame.mixer.music.load("spaceInvadersBGMusic.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.5)

#player
playerImg = pygame.image.load('player.png')
playerChange = 0

def player(x, y):
    screen.blit(playerImg, (x, y))
#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyChangeX = []
enemyChangeY = []
numEnemies = 6

for i in range(numEnemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, screenWidth - 64))
    enemyY.append(random.randint(enemyMinY, enemyMaxY))
    enemyChangeX.append(enemySpeedX)
    enemyChangeY.append(enemySpeedY)
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
#bullet
bulletImage = pygame.image.load('bullet.png')
bulletX = playerX
bulletChangeX = 0
bulletY = playerY
bulletChange = bulletSpeed
bulletState = "ready"

def fireBullet(x, y):
    laserSound = pygame.mixer.Sound("laser.mp3")
    laserSound.play()
    laserSound.set_volume(0.25)
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))
#score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def showScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))
#game over
overFont = pygame.font.Font('freesansbold.ttf', 64)

def gameOverText():
    overText = overFont.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(overText, (200, 250))
#collision check between enemy and bullet
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    return distance < collisionDistance
#game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange -= 5
            if event.key == pygame.K_RIGHT:
                playerChange += 5
            if event.key == pygame.K_SPACE and bulletState == "ready":
                bulletX = playerX
                fireBullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
            playerChange = 0
    #player movement
    playerX += playerChange
    playerX = max(0, min(playerX, screenWidth - 64))
    #enemy movement
    for i in range(numEnemies):
        if enemyY[i] > 340:
            for j in range(numEnemies):
                enemyY[j] = 2000
            gameOverText()
            break
        enemyX[i] += enemyChangeX[i]
        if enemyX[i] <= 0 or enemyX[i] >= screenWidth - 64:
            enemyChangeX[i] *= -1
            enemyY[i] += enemyChangeY[i]
        #collision check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = playerY
            bulletState = 'ready'
            scoreValue += 1
            enemyX[i] = random.randint(0, screenWidth - 64)
            enemyY[i] = random.randint(enemyMinY, enemyMaxY)
        enemy(enemyX[i], enemyY[i], i)
    #bullet movement
    if bulletY <= 0:
        bulletY = playerY
        bulletState = 'ready'
    elif bulletState == 'fire':
        fireBullet(bulletX, bulletY)
        bulletY -= bulletChange
    #updates screen
    player(playerX, playerY)
    showScore(textX, textY)
    fps.tick(90)
    pygame.display.update()

pygame.quit()