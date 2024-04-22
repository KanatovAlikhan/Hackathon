import sys
import random
import pygame
def start2():
    pygame.init()

    size = width, height = 800, 550
    screen = pygame.display.set_mode(size)
    speed = [0, 0]

    background = pygame.image.load("images/back1.jpg")
    background1 = pygame.image.load("images/2nd.png")
    background2 = pygame.image.load("images/3rd.png")
    background = pygame.transform.scale(background, (800, 550))
    bg_y_pos = 0
    bg_2_y_pos = background.get_height()

    ticks_since_last_enemy = 0
    time_to_next_enemy = 1000
    main_clock = pygame.time.Clock()
    score = 0

    class MainCharacter(pygame.sprite.Sprite):
        is_player_alive = True

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("images/spaceship.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect()
            self.rect.center = (250, 250)
            self.totalLives = 1
            self.lastHit = 0

        def update(self):
            self.lastHit = pygame.time.get_ticks()
            self.totalLives -= 1
            if self.totalLives <= 0:
                MainCharacter.is_player_alive = False

    class BadGuy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("images/gold-removebg-preview (2).png")
            self.image = pygame.transform.scale(self.image, (32, 32))
            self.rect = self.image.get_rect()
            enemy_type = random.choice([1, 2, 3, 4, 5])
            self.badSpeed = [0, 0]
            self.rect.center = (0, 0)
            
            if enemy_type == 1:
                self.badSpeed = [0, 4]
                self.rect.center = (random.randint(0, width), 0)
            elif enemy_type == 2:
                self.badSpeed = [3, 3]
                self.rect.center = (0, random.randint(int(height / 4), int(3 * height / 4)))
            elif enemy_type == 3:
                self.badSpeed = [-3, 3]
                self.rect.center = (width, random.randint(int(height / 4), int(3 * height / 4)))
            elif enemy_type == 4:
                self.badSpeed = [4, 0]
                self.rect.center = (0, random.randint(int(height / 4), int(3 * height / 4)))
            elif enemy_type == 5:
                self.badSpeed = [-4, 0]
                self.rect.center = (width, random.randint(int(height / 4), int(3 * height / 4)))

        def update(self):
            self.rect = self.rect.move(self.badSpeed)
            
            if self.rect.top > height:
                self.remove(bad_sprites)
            
            if self.badSpeed[0] > 6:
                self.badSpeed[0] -= 0.5
            if self.badSpeed[0] < -6:
                self.badSpeed[0] += 0.5
            if self.badSpeed[1] > 6:
                self.badSpeed[1] -= 0.5
            if self.badSpeed[1] < -6:
                self.badSpeed[1] += 0.5

    class StrongBadGuy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("images/loook.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(0, width), 0)
            self.speed = [0, 6]
            self.lives = 3

        def update(self):
            self.rect = self.rect.move(self.speed)
            
            if self.rect.top > height:
                self.remove(strong_bad_sprites)

            if self.speed[0] > 8:
                self.speed[0] -= 0.5
            if self.speed[0] < -8:
                self.speed[0] += 0.5

            if self.speed[1] > 8:
                self.speed[1] -= 0.5
            if self.speed[1] < -8:
                self.speed[1] += 0.5

    main = MainCharacter()
    main_sprite = pygame.sprite.Group()
    main_sprite.add(main)

    bad_sprites = pygame.sprite.Group()
    strong_bad_sprites = pygame.sprite.Group()

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        bg_y_pos -= 5
        bg_2_y_pos -= 5

        if bg_y_pos < -1 * background.get_height():
            bg_y_pos = background.get_height()
        if bg_2_y_pos < -1 * background.get_height():
            bg_2_y_pos = background.get_height()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()

        if not MainCharacter.is_player_alive:
            title_font = pygame.font.SysFont("Times New Roman", 50)
            game_over_text_1 = title_font.render("GAME OVER", 1, (250, 250, 250))
            screen.blit(game_over_text_1, (120, 100))
            
            my_font = pygame.font.SysFont("Times New Roman", 25)
            if score < 200:
                score_text = my_font.render("Your score was: " + str(score) + " Level 1", 1, (0, 0, 0))
                screen.blit(score_text, (150, 180))
            elif score >= 200 and score < 500:
                score_text = my_font.render("Your score was: " + str(score) + " Level 2", 1, (0, 0, 0))
                screen.blit(score_text, (150, 180))
            exit_text = my_font.render("Press space to exit", 1, (0, 0, 0))
            screen.blit(exit_text, (150, 220))
            
            if key[pygame.K_SPACE]:
                pygame.quit()
                sys.exit()

        else:
            if score < 200:
                screen.blit(background, (0, bg_y_pos))
                screen.blit(background, (0, bg_2_y_pos))
            elif score >= 200 and score <= 500:
                screen.blit(background1, (0, bg_y_pos))
                screen.blit(background1, (0, bg_2_y_pos))
            else:
                screen.blit(background2, (0, bg_y_pos))
                screen.blit(background2, (0, bg_2_y_pos))

            if key[pygame.K_a]:
                if speed[0] > -20:
                    speed[0] -= 1.5
            if key[pygame.K_d]:
                if speed[0] < 20:
                    speed[0] += 1.5
            if key[pygame.K_w]:
                if speed[1] > -20:
                    speed[1] -= 1.5
            if key[pygame.K_s]:
                if speed[1] < 20:
                    speed[1] += 1.5

            if speed[0] > 0:
                speed[0] -= 0.5
            elif speed[0] < 0:
                speed[0] += 0.5

            if speed[1] > 0:
                speed[1] -= 0.5
            elif speed[1] < 0:
                speed[1] += 0.5

            if main.rect.left < 0 or main.rect.right > width:
                speed[0] = -speed[0] * 1.5
            if main.rect.top < 0 or main.rect.bottom > height:
                speed[1] = -speed[1] * 1.5

            ticks_since_last_enemy += main_clock.tick()
            
            if ticks_since_last_enemy >= time_to_next_enemy:
                ticks_since_last_enemy = 0
                bad_sprites.add(BadGuy())
                time_to_next_enemy = max(time_to_next_enemy - 10, 100)

                # Добавляем сильного врага каждые 500 очков
                if score % 40 == 0 and score != 0:
                    strong_bad_sprites.add(StrongBadGuy())
            
            main.rect = main.rect.move(speed)
            bad_sprites.update()
            strong_bad_sprites.update()

            # Проверка столкновений с обычными врагами
            collisions = pygame.sprite.spritecollide(main, bad_sprites, True)
            if collisions:
                score += 20

            # Проверка столкновений с сильными врагами
            collisions = pygame.sprite.spritecollide(main, strong_bad_sprites, True)
            if collisions:
                MainCharacter.is_player_alive = False  # Установка флага завершения игры

            main_sprite.draw(screen)
            bad_sprites.draw(screen)
            strong_bad_sprites.draw(screen)

            my_font = pygame.font.SysFont("Times New Roman", 18)
            if score < 200:
                score_text = my_font.render("Score: " + str(score) + " Level 1", 1, (0, 0, 0))
                screen.blit(score_text, (30, 30))
            elif score >= 200 and score < 500:
                score_text = my_font.render("Score: " + str(score) + " Level 2", 1, (0, 0, 0))
                screen.blit(score_text, (30, 30))
            elif score > 500 and score < 700:
                score_text = my_font.render("Score: " + str(score) + " Level 3", 1, (0, 0, 0))
                screen.blit(score_text, (30, 30))
                
            if score >= 500:
                title_font = pygame.font.SysFont("Times New Roman", 50)
                win_text = title_font.render("You won!", 1, (0, 0, 0))
                screen.blit(win_text, (250, 250))
                pygame.display.flip()
                pygame.time.wait(2000)  # Ждем 2 секунды перед завершением игры
                pygame.quit()
                sys.exit()


        pygame.display.flip()
