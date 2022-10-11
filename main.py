
from cgitb import text
import pygame
from Snake import *
from Food import *

pygame.init()
pygame.font.init()
bounds = (1200,600)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake Training")
block_size = 20

snake = Snake(block_size, (400,400))
food = Food(block_size)
font = pygame.font.SysFont('comicsans',60, True)
run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.direct(Direction.left)
            elif event.key == pygame.K_RIGHT:
                snake.direct(Direction.right)
            elif event.key == pygame.K_UP:
                snake.direct(Direction.up)
            elif event.key == pygame.K_DOWN:
                snake.direct(Direction.down)
    
    
    snake.move()
    snake.distance_to_food(food)
    snake.check_for_food(food)
    if snake.check_bounds() == True or snake.check_tail_collision() == True:

        pygame.display.update()
        pygame.time.delay(1000)
        snake.respawn()



    print(snake.body)
    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), pygame.Rect(100, 100, 400, 400), 2)

    snake.draw(pygame, window)
    food.draw(pygame, window, snake.body)

    text = font.render(str(snake.length - 3) , True, (255,255,255))
    window.blit(text, (20,120))
    
    pygame.display.update()
    