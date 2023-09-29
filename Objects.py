from pplay.window import *
from pplay.sprite import *
import pygame


class ScoreRenderer:
    score_left, score_right = 0, 0

    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.cor_texto = (255, 255, 255)

    def renderizar(self, surface, x, y):
        # Renderize o texto da pontuação
        score_text = self.font.render(f"{self.score_left} - {self.score_right}", True, self.cor_texto)
        # Desenhe o texto na tela na posição especificada
        surface.blit(score_text, (x, y))

    def add_score_right(self):
        self.score_right += 1

    def add_score_left(self):
        self.score_left += 1


class Background:
    def __init__(self, image_path, width, height):
        self.sprite = Sprite(image_path)
        self.sprite.image = pygame.transform.scale(self.sprite.image, (width, height))
        self.sprite.set_position(0, 0)

    def draw(self):
        self.sprite.draw()


class Ball:
    def __init__(self, image_path, initial_x, initial_y, speed_x, speed_y):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.sprite = Sprite(image_path)
        self.sprite.set_position(initial_x, initial_y)
        self.speedX = speed_x
        self.speedY = speed_y

    def move_center(self):
        self.sprite.set_position(self.initial_x, self.initial_y)
        self.speedX *= -1
        self.speedY *= -1

    def move(self, delta_time):
        Sprite.move_x(self.sprite, self.speedX * delta_time)
        Sprite.move_y(self.sprite, self.speedY * delta_time)

    def check_left_wall_collision(self, left_paddle, right_paddle):
        if self.sprite.x < 0:
            self.move_center()
            left_paddle.move_initial()
            right_paddle.move_initial()
            return True
        return False

    def check_right_wall_collision(self, window_width, left_paddle, right_paddle):
        if self.sprite.x > window_width - self.sprite.width:
            self.sprite.set_position(window_width - self.sprite.width, self.sprite.y)
            self.speedX *= -1
            self.move_center()
            left_paddle.move_initial()
            right_paddle.move_initial()
            return True
        return False

    def check_roof_collision(self, window_height):
        if self.sprite.y < 0:
            self.sprite.set_position(self.sprite.x, 0)
            self.speedY *= -1
        if self.sprite.y > window_height - self.sprite.height:
            self.sprite.set_position(self.sprite.x, window_height - self.sprite.height)
            self.speedY *= -1

    def check_paddle_collision(self, left_paddle, right_paddle):
        if self.sprite.collided(left_paddle.sprite):
            self.sprite.set_position(left_paddle.sprite.x + left_paddle.sprite.width, self.sprite.y)
            self.speedX *= -1
        if self.sprite.collided(right_paddle.sprite):
            self.sprite.set_position(right_paddle.sprite.x - self.sprite.width, self.sprite.y)
            self.speedX *= -1

    def draw(self):
        self.sprite.draw()


class Paddle:
    WIDTH, HEIGHT = 15, 80

    def __init__(self, image_path, initial_x, initial_y, speed):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.speed = speed
        self.sprite = Sprite(image_path)
        self.sprite.set_position(initial_x, initial_y)

    def move_initial(self):
        self.sprite.set_position(self.initial_x, self.initial_y)

    def move_up(self, delta_time):
        Sprite.move_y(self.sprite, -self.speed * delta_time)

    def move_down(self, delta_time):
        Sprite.move_y(self.sprite, self.speed * delta_time)
