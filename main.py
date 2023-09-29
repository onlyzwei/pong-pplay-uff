import pygame
from pplay.window import *
from pplay.sprite import *
from pplay.keyboard import *
from Objects import *

# Configuração da janela
window_width, window_height = 800, 600
janela = Window(window_width, window_height)
janela.set_title("Pong Game")
janela.background = Background("assets/background.jpg", window_width, window_height)

# Velocidades ajustadas
ball_speedX = 300
ball_speedY = 400
paddle_speed = 500

# Objetos do jogo
paddle_width, paddle_height = 15, 80
ball = Ball("assets/ball.png", window_width / 2, window_height / 2, ball_speedX, ball_speedY)
left_paddle = Paddle("assets/paddle.png", 10, (window_height / 2) - (Paddle.HEIGHT / 2), paddle_speed)
right_paddle = Paddle("assets/paddle.png", window_width - Paddle.WIDTH - 10, (window_height / 2) - (Paddle.HEIGHT / 2),
                      paddle_speed)
key = Keyboard()

# Pontuação
score_rendererX, score_rendererY = window_width / 2 - 20, 10

# Fonte
pygame.font.init()
fonte = pygame.font.Font(None, 35)

# ScoreRenderer
score_renderer = ScoreRenderer()


def main():
    while True:
        delta_time = janela.delta_time()

        # Movimento da bola e colisões
        ball.move(delta_time)
        if ball.check_left_wall_collision(left_paddle, right_paddle):
            score_renderer.add_score_right()
        if ball.check_right_wall_collision(window_width, left_paddle, right_paddle):
            score_renderer.add_score_right()
        ball.check_roof_collision(window_height)
        ball.check_paddle_collision(left_paddle, right_paddle)

        # Movimento das raquetes
        if key.key_pressed("W") and left_paddle.sprite.y >= 0:
            left_paddle.move_up(delta_time)
        if key.key_pressed("S") and left_paddle.sprite.y <= window_height - Paddle.HEIGHT:
            left_paddle.move_down(delta_time)
        if key.key_pressed("UP") and right_paddle.sprite.y >= 0:
            right_paddle.move_up(delta_time)
        if key.key_pressed("DOWN") and right_paddle.sprite.y <= window_height - Paddle.HEIGHT:
            right_paddle.move_down(delta_time)

        # Desenhar elementos
        janela.background.draw()
        ball.draw()
        left_paddle.sprite.draw()
        right_paddle.sprite.draw()
        score_renderer.renderizar(janela.screen, score_rendererX, score_rendererY)
        janela.update()


if __name__ == "__main__":
    main()
