import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)  # Цвет бревна

# Размеры экрана
WIDTH = 800
HEIGHT = 550

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лодочная переправа")
background = pygame.image.load("images/background.png")

# Загрузка изображений лодки и островов
boat_image = pygame.image.load("images/boat.png").convert()  # Замените "boat_image.png" на путь к вашему файлу изображения лодки
island_image = pygame.image.load("images/island.png").convert()  # Замените "island_image.png" на путь к вашему файлу изображения острова

# Класс острова
class Island(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = island_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Класс лодки
class Boat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = boat_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 1.5-30, HEIGHT // 1.5)
        self.speed = 7

    def move(self, dx, dy):
        # Проверяем, не выходит ли лодка за пределы экрана
        if 0 <= self.rect.x + dx <= WIDTH - self.rect.width:
            self.rect.x += dx
        if 0 <= self.rect.y + dy <= HEIGHT - self.rect.height:
            self.rect.y += dy

# Класс человека
class Person(pygame.sprite.Sprite):
    def __init__(self, island):
        super().__init__()
        # Загрузка изображения человека
        self.image = pygame.image.load("images/man.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.island = island
        self.rect.center = self.island.rect.center

    def board(self, boat):
        if pygame.sprite.collide_rect(self, boat):
            self.rect.center = boat.rect.center

    def leave(self, island):
        self.island = island
        self.rect.center = self.island.rect.center

# Загрузка изображения моста
bridge_image = pygame.image.load("images/suret.png").convert_alpha()  

# Класс моста (бревна)
class Bridge(pygame.sprite.Sprite):
    def __init__(self, island1, island2):
        super().__init__()
        self.image = bridge_image
        self.rect = self.image.get_rect()
        # Находим центры каждого острова
        center_x1, center_y1 = island1.rect.center
        center_x2, center_y2 = island2.rect.center
        # Устанавливаем позицию моста между островами
        self.rect.centerx = (center_x1 + center_x2) // 2
        self.rect.centery = (center_y1 + center_y2) // 2
        self.direction = 1  # Направление движения моста: 1 - вперед, -1 - назад

    def move(self):
        # Проверяем, не выходит ли мост за пределы экрана
        if self.rect.y <= 0:
            self.direction = 1  # Изменяем направление на вперед, если мост достиг верхней границы
        elif self.rect.y >= HEIGHT - self.rect.height:
            self.direction = -1  # Изменяем направление на назад, если мост достиг нижней границы
        self.rect.y += self.direction * 1.8 # Изменяем положение моста в зависимости от направления

# Создание островов
island1 = Island(100, 200)
island2 = Island(600, 400)

# Создание лодки
boat = Boat()

# Создание групп спрайтов
all_sprites = pygame.sprite.Group()
all_sprites.add(island1, island2, boat)

# Создание группы людей
people = pygame.sprite.Group()

# Создание группы мостов (бревен)
bridges = pygame.sprite.Group()


# Функция для создания рандомного количества людей на острове
def create_people(island):
    num_people = random.randint(5, 10)  # Генерируем случайное количество людей от 5 до 10
    for _ in range(num_people):
        person = Person(island)
        people.add(person)
        all_sprites.add(person)  # Добавляем в группу всех спрайтов


# Создание оград между островами
def create_bridges(island1, island2):
    num_bridges = random.randint(1, 3)  # Генерируем случайное количество оград от 1 до 3
    for _ in range(num_bridges):
        bridge = Bridge(island1, island2)
        bridges.add(bridge)
        all_sprites.add(bridge)

# Генерация людей на островах
create_people(island1)
create_people(island2)

# Генерация оград между островами
create_bridges(island1, island2)

# Счетчики для каждого острова и времени игры
font = pygame.font.Font(None, 36)
text_color = WHITE

# Инициализация времени перед началом основного цикла
start_time = pygame.time.get_ticks() 

# Главный игровой цикл
reached_island = False  # Флаг для отслеживания достижения острова

# Переменная для отслеживания времени в секундах
current_time = 0

# Инициализация времени перед началом основного цикла
start_time = pygame.time.get_ticks() 

# Главный игровой цикл
# Главный игровой цикл
running = True
while running:
    # Подсчет прошедшего времени в секундах
    current_time = (pygame.time.get_ticks() - start_time) // 1000

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Проверяем, прибыла ли лодка к какому-либо острову
                if pygame.sprite.collide_rect(boat, island1):
                    for person in people:
                        if person.island == island1:
                            # Обновляем местоположение человека на острове, к которому прибыла лодка
                            person.leave(island2)
                elif pygame.sprite.collide_rect(boat, island2):
                    for person in people:
                        if person.island == island2:
                            # Обновляем местоположение человека на острове, к которому прибыла лодка
                            person.leave(island1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        boat.move(-boat.speed, 0)
    if keys[pygame.K_RIGHT]:
        boat.move(boat.speed, 0)
    if keys[pygame.K_UP]:
        boat.move(0, -boat.speed)
    if keys[pygame.K_DOWN]:
        boat.move(0, boat.speed)

    # Движение моста
    for bridge in bridges:
        bridge.move()

    # Проверка столкновения между лодкой и островами
    if pygame.sprite.collide_rect(boat, island1):
        for person in people:
            if person.island == island1:
                person.board(boat)
    if pygame.sprite.collide_rect(boat, island2):
        for person in people:
            if person.island == island2:
                person.board(boat)

    # Люди покидают лодку, если она находится рядом с островом
    for person in people:
        if pygame.sprite.collide_rect(boat, person):
            person.board(boat)

    # Проверка столкновения лодки с мостом
    if pygame.sprite.spritecollideany(boat, bridges):
        running = False  # Завершаем игру, если лодка коснулась моста

    # Отображение всех спрайтов
    all_sprites.draw(screen)

    # Отображение счетчиков для каждого острова
    text_island1 = font.render(f"Island 1: {len([p for p in people if p.island == island1])}", True, text_color)
    text_island2 = font.render(f"Island 2: {len([p for p in people if p.island == island2])}", True, text_color)
    screen.blit(text_island1, (10, 10))
    screen.blit(text_island2, (WIDTH - 140, 10))

    # Отображение времени
    text_time = font.render(f"Time: {current_time} sec", True, text_color)
    screen.blit(text_time, (10, 50))

    # Отображение надписи в центре экрана
    text_climate = font.render("Current climate in West Kazakhstan", True, text_color)
    text_climate_rect = text_climate.get_rect(center=(WIDTH // 2, 10))
    screen.blit(text_climate, text_climate_rect)


    # Обновление экрана
    pygame.display.flip()

# Вывод сообщения "Game finished"
screen.fill(BLACK)
text_game_finished = font.render("Game finished", True, WHITE)
text_rect = text_game_finished.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(text_game_finished, text_rect)
pygame.display.flip()

# Задержка перед завершением
pygame.time.delay(2000)

# Завершение Pygame
pygame.quit()

