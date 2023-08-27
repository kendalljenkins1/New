import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Размер экрана
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Инициализация игровых переменных
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
                 random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

# Инициализация скорости и таймера
speed = 15
fps_controller = pygame.time.Clock()

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Обработка нажатий клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                
    # Изменение направления движения змейки
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
        
    # Обновление позиции змейки
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
        
    # Добавление нового элемента к змейке
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawn = False
    else:
        snake_body.pop()
        
    if not food_spawn:
        food_position = [random.randrange(1, (SCREEN_WIDTH//10)) * 10,
                         random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
    food_spawn = True
    
    # Отрисовка элементов на экране
    screen.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(
        food_position[0], food_position[1], 10, 10))
    
    # Обновление экрана
    pygame.display.update()
    
    # Ограничение скорости
    fps_controller.tick(speed)
