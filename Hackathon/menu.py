import pygame,time
from cdbh import start1
from main import start2
from boatgame import start3
pygame.init()
location = "menu"
screen = pygame.display.set_mode((800, 550))
menu = pygame.image.load("images/main_menu.png")
menu = pygame.transform.scale(menu, (800, 550))
player_image = pygame.image.load('images/Arnur.png')
player_image = pygame.transform.scale(player_image, (50, 50))
door1 = pygame.Rect(283,251,10,10)
door2 = pygame.Rect(359,260,10,10)
door3 = pygame.Rect(440,261,10,10)
player = pygame.Rect(355, 390, 50, 50)
speed = 1
game1=True
game2=True
game3=True
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    screen.blit(menu, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    if player.colliderect(door1) and game1:
        game1=False
        game2=True
        game3=True
        start1()  
    if player.colliderect(door2) and game2:
        game1=True
        game2=False
        game3=True
        start2() 
    if player.colliderect(door3) and game3:
        game1=True
        game2=True
        game3=False
        start3()  
    screen.blit(player_image, player)
    pygame.display.update()
pygame.quit()
