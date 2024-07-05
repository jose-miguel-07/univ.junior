import pygame
import random


pygame.init()
pygame.display.set_caption("Tzénossauro Rex")


SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player_vel = pygame.Vector2()
jumping = False
floor = 200
player = pygame.image.load("Trex.png")
cactus = pygame.image.load("mnm.png")
player_pos = pygame.Vector2(20, floor)
cactus_pos = pygame.Vector2(800, floor)
cactus_pos2 = pygame.Vector2(1200, floor)
cactus_pos3 = pygame.Vector2(1600, floor)
FPS = 60


bg = pygame.image.load("background_trex.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()


font = pygame.font.Font(None, 36)

scroll = 0
start_time = pygame.time.get_ticks()
score = 0
game_over = False

def show_score():
    global score
    score_surface = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))

def reset_game():
    global player_pos, cactus_pos, cactus_pos2, cactus_pos3, player_vel, start_time, score, game_over, jumping
    player_pos = pygame.Vector2(20, floor)
    cactus_pos = pygame.Vector2(800, 200)
    cactus_pos2 = pygame.Vector2(1200, 200)
    cactus_pos3 = pygame.Vector2(1600, 200)
    player_vel = pygame.Vector2()
    start_time = pygame.time.get_ticks()
    score = 0
    game_over = False
    jumping = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping and not game_over:
                player_vel.y = -15.8
                jumping = True
            if event.key == pygame.K_r and game_over:
                reset_game()

    if not game_over:
        screen.fill("white")

 
        for i in range(0, 255):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll


        scroll -= 5
        if abs(scroll) > bg_width:
            scroll = 0


        cactus_pos.x -= 5
        cactus_pos2.x -= 5
        cactus_pos3.x -= 5

        if cactus_pos.x < 0:
            cactus_pos.x = 1550
        if cactus_pos2.x < 0:
            cactus_pos2.x = 1550
        if cactus_pos3.x < 0:
            cactus_pos3.x = 1550

        screen.blit(cactus, (cactus_pos.x, cactus_pos.y))
        screen.blit(cactus, (cactus_pos2.x, cactus_pos2.y))
        screen.blit(cactus, (cactus_pos3.x, cactus_pos3.y))
        screen.blit(player, (player_pos.x, player_pos.y))

        if jumping:
            player_vel.y += 0.5  
            player_pos.y += player_vel.y
            if player_pos.y >= floor:
                player_pos.y = floor
                jumping = False
                player_vel.y = 0

        score = (pygame.time.get_ticks() - start_time) // 100

    
        show_score()

   
        player_rect = pygame.Rect(player_pos.x, player_pos.y, player.get_width(), player.get_height())
        cactus_rect1 = pygame.Rect(cactus_pos.x, cactus_pos.y, cactus.get_width(), cactus.get_height())
        cactus_rect2 = pygame.Rect(cactus_pos2.x, cactus_pos2.y, cactus.get_width(), cactus.get_height())
        cactus_rect3 = pygame.Rect(cactus_pos3.x, cactus_pos3.y, cactus.get_width(), cactus.get_height())

        if player_rect.colliderect(cactus_rect1) or player_rect.colliderect(cactus_rect2) or player_rect.colliderect(cactus_rect3):
            game_over = True

    else:
        game_over_surface = font.render('Game Over! Press R to Restart', True, (255, 0, 0))
        screen.blit(game_over_surface, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()