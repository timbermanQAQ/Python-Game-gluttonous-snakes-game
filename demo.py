# 导入必要的模块
import pygame, sys, random
from pygame.locals import *

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 读取历史最高分
try:
    with open('high_score.txt', 'r') as f:
        high_score = int(f.read())
except FileNotFoundError:
    high_score = 0

# 定义得分
score = 0

# 定义游戏区域大小
width = 800
height = 600

# 定义蛇的大小
snake_size = 10

# 初始化pygame
pygame.init()

#初始化pygame混音模块
pygame.mixer.init()

#加载背景音乐
pygame.mixer.music.load(r"D:\QQ file\3361246314\FileRecv\三亩地 - 城南花已开.flac")

#加载吃到食物的音效
eat_sound = pygame.mixer.Sound(r"C:\Users\timberman\Downloads\test.ogg")

#调整游戏音量
pygame.mixer.music.set_volume(0.1)

#开始播放背景音乐
pygame.mixer.music.play()

# 创建游戏区域
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('贪吃蛇')

# 定义蛇的初始位置
snake_x = width / 2
snake_y = height / 2

# 定义蛇的初始移动方向
snake_direction = 'right'

# 定义蛇的初始长度
snake_length = 1

# 定义蛇的身体
snake_body = []

# 定义食物的初始位置
food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

# 定义游戏结束的标志
game_over = False

# 定义游戏循环
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'
            elif event.key == K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == K_DOWN and snake_direction != 'up':
                snake_direction = 'down'

    # 移动蛇的身体
    if snake_direction == 'right':
        snake_x += snake_size
    elif snake_direction == 'left':
        snake_x -= snake_size
    elif snake_direction == 'up':
        snake_y -= snake_size
    elif snake_direction == 'down':
        snake_y += snake_size

    # 判断蛇是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        # 生成新的食物位置
        food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
        # 增加蛇的长度
        snake_length += 1
        # 增加分数
        score += 10
        # 播放吃到食物的音效
        eat_sound.play()

    # 更新蛇的身体
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    # 判断蛇是否撞到自己
    for block in snake_body[:-1]:
        if block == snake_head:
            game_over = True

    # 绘制游戏区域
    screen.fill(black)

    # 绘制蛇的身体
    for block in snake_body:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_size, snake_size])

    # 绘制食物
    pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])

    # 判断蛇是否撞到边界
    if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
        game_over = True

    # 判断是否更新历史最高分
    if score> high_score:
        high_score = score

    # 保存历史最高分
    with open('high_score.txt', 'w') as f:
        f.write(str(high_score))

    

    # 创建一个字体对象
    font = pygame.font.Font(None, 36)

    # 创建一个文本对象
    score_text = font.render("Score: " + str(score), 1, white)
    high_score_text = font.render("High Score: " + str(high_score), 1, white)

    # 绘制文本对象
    screen.blit(score_text, (width/2 - score_text.get_width()/2, height/2 - score_text.get_height()))
    screen.blit(high_score_text, (width/2 - high_score_text.get_width()/2, height/2))



    # 更新屏幕
    pygame.display.update()
    
    # 控制游戏速度
    pygame.time.Clock().tick(20)




# 退出游戏
pygame.quit()
sys.exit()