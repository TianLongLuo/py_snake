import pygame
from pygame.locals import *
from sys import exit
import time
import random
#定义颜色
pinkColor = pygame.Color(255,182,193)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)

#游戏结束函数
def gameover():
    pygame.quit()
    exit()

#定义游戏入口函数
def main():
    pygame.init()
    time_clock = pygame.time.Clock()

    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption('贪吃蛇')
    # 定义蛇的初始化变量
    snakePosition = [100,100]
    snakeSegments = [[100,100],[80,100],[60,100],[40,100],[20,100]]
    foodPosition = [300,300]
    foodTotal = 1
    direction = 'right'
    changeDirection = direction
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == K_a:
                    changeDirection = 'left'
                if event.key == K_UP or event.key == K_w:
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == K_s:
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20
        snakeSegments.insert(0,list(snakePosition))
        if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
            foodTotal = 0
        else:
            snakeSegments.pop()

        if foodTotal == 0:
            x = random.randrange(1,32)
            y = random.randrange(1,24)
            foodPosition = [int(x*20),int(y*20)]
            foodTotal = 1

        #开始绘制
        screen.fill(blackColor)

        for position in snakeSegments:
            pygame.draw.rect(screen,pinkColor,Rect(position[0],position[1],20,20))
            pygame.draw.rect(screen,whiteColor,Rect(foodPosition[0],foodPosition[1],20,20))
        pygame.display.flip()

        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameover()
        elif snakePosition[1] >460 or snakePosition[1] < 0:
            gameover()

        for body in snakeSegments[1:]:
            if snakePosition[0] == body[0] and snakePosition[1] == body[1]:
                gameover()
        time_clock.tick(5)
if __name__ == '__main__':
    main()