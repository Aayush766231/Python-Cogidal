import math
import random
import pygame

pygame.init()

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
pygame.display.set_caption("Space Invaders")
background = pygame.image.load("background.png")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

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
    enemyImg.append(pygame.image.load('enemy.py'))
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