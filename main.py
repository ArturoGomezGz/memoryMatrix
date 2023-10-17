import pygame
import random
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

# colores en RGB
BLANCO = (255, 255, 255)
NEGRO = (36, 36, 36)
ROJO = (194, 59, 33)
VERDE = (0, 107, 61)
AZUL = (0, 0, 131)
AMARILLO = (253, 204, 12)
MORADO = (202, 62, 230)
NARANJA = (255, 172, 4)
ROSITA = (255, 124, 234)
OSCAR_GAY = (79, 255, 51)


# DIMENSIONES DE LA VENTANA
WIDTH = 600
HEIGHT = 650

# Font
MAIN_FONT = pygame.font.SysFont('Arial', 40)
LEVEL_FONT = pygame.font.SysFont('arialbold', 35)
LEVEL_COMPLETE_FONT = pygame.font.SysFont('Tahoma', 32)
GAME_OVER_FONT = pygame.font.SysFont('Tahoma', 27)
COLOR_FONT = pygame.font.SysFont('Tahoma', 32)

# ruidos culeros
LEVEL_PASSED_SOUND = pygame.mixer.Sound('Assets/level_passed.mp3')
LEVEL_FAILED_SOUND = pygame.mixer.Sound('Assets/level_failed.mp3')
SOUND_1 = pygame.mixer.Sound('Assets/sound_1.mp3')
SOUND_2 = pygame.mixer.Sound('Assets/sound_2.mp3')
SOUND_3 = pygame.mixer.Sound('Assets/sound_3.mp3')
SOUND_4 = pygame.mixer.Sound('Assets/sound_4.mp3')

# innicializamos pygame
pygame.display.set_caption("Memory matrix")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

CORRECT_COLOR = (0, 0, 0)


def main():
    sequence_length = level = 1
    game_sequence = generate_color_sequence(sequence_length)
    player_sequence = []

    color_rectangles = {  # color del rectangulo
        ROJO: pygame.Rect(0, 100, 225, 225),  # x, y, largo y ancho del rectangulo
        VERDE: pygame.Rect(0, 325, 225, 225),
        AZUL: pygame.Rect(225, 100, 225, 225),
        AMARILLO: pygame.Rect(225, 325, 225, 225),
        NEGRO: pygame.Rect(0, 0, 0, 0),
        MORADO: pygame.Rect(202, 62, 230, 255),
        NARANJA: pygame.Rect(255, 172, 4, 255),
        ROSITA: pygame.Rect(255, 124, 234, 255),
        OSCAR_GAY: pygame.Rect(79, 255, 51, 255)
    }

    display_sequence(game_sequence)
    running = True
    while running:

        for event in pygame.event.get():

            # el usuario presiono el boton de salir.
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # usuario presiona algún boton del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                for color, rect in color_rectangles.items():
                    if rect.collidepoint(x, y):
                        generate_sound(color)
                        player_sequence.append(color)
                        break

                if compare_pressed_button(game_sequence, player_sequence):
                    if player_sequence == game_sequence:
                        sequence_length += 1
                        level += 1
                        draw_level_completed("Nivel completado! :)")
                        game_sequence = generate_color_sequence(sequence_length)
                        player_sequence = []
                        time.sleep(2)
                        display_sequence(game_sequence)
                else:
                    draw_game_over(f"PerdisTEC iwi ")
                    running = False
                    break

        if running != False:
            draw_window(color_rectangles, str(level))
            clock.tick(60)

        # Makes random RGB color sequence


def generate_color_sequence(length):
    return [random.choice([ROJO, VERDE, AZUL, AMARILLO, NEGRO, MORADO, NARANJA, ROSITA, OSCAR_GAY]) for _ in range(length)]


# regresa un string equivalente al color
def get_color_string(color):
    color_dictionary = {ROJO: "ROJO", AMARILLO: "AMARILLO", VERDE: "VERDE", AZUL: "AZUL", NEGRO: "NEGRO", MORADO: "MORADO", NARANJA: "NARANJA", ROSITA: "ROSITA", OSCAR_GAY: "VERDE-CAGUAMA"}
    return color_dictionary.get(color, None)


def generate_sound(color):
    sound_dict = {ROJO: SOUND_1, AZUL: SOUND_2, AMARILLO: SOUND_3, VERDE: SOUND_4, NEGRO: SOUND_1, MORADO: SOUND_2, NARANJA: SOUND_3, ROSITA: SOUND_4, OSCAR_GAY: SOUND_1}
    sound = sound_dict.get(color, None)
    sound.play()
    return sound


# muestra la secuencia de colores que el jugador debe de seguir
def display_sequence(sequence):
    for color in sequence:
        generate_sound(color)
        screen.fill(color)
        pygame.display.update()
        time.sleep(1)


# interfaz principal del juego
def draw_window(color_rectangles, level):
    screen.fill(BLANCO)

    # titulo
    color_game_text = MAIN_FONT.render("MEMORY MATRIX", True, NEGRO)
    screen.blit(color_game_text, (WIDTH / 2 - color_game_text.get_width() / 2, 0))

    # muestra el texto de nivel
    level_final_text = "Nivel " + level
    render_level_text = LEVEL_FONT.render(level_final_text, True, NEGRO)
    screen.blit(render_level_text, (WIDTH / 2 - render_level_text.get_width() / 2, 60))

    # muestra los 9 cuadraditos de colores en una cuadrícula 3x3
    row_count = 0
    col_count = 0
    rect_width = WIDTH // 3
    rect_height = (HEIGHT - 100) // 3

    for color, rect in color_rectangles.items():
        rect.x = col_count * rect_width
        rect.y = row_count * rect_height + 100
        rect.width = rect_width
        rect.height = rect_height

        pygame.draw.rect(screen, color, rect)

        col_count += 1
        if col_count >= 3:
            col_count = 0
            row_count += 1

    pygame.display.update()


# pantalla de juego terminado
def draw_game_over(text):
    LEVEL_FAILED_SOUND.play()
    screen.fill(BLANCO)

    draw_text = GAME_OVER_FONT.render(text, True, NEGRO)
    color_text = COLOR_FONT.render(get_color_string(CORRECT_COLOR), True, CORRECT_COLOR)

    total_width = draw_text.get_width() + color_text.get_width()
    start_x = WIDTH / 2 - total_width / 2

    screen.blit(draw_text, (start_x, HEIGHT / 2 - draw_text.get_height() / 2))
    screen.blit(color_text, (start_x + draw_text.get_width(), HEIGHT / 2 - color_text.get_height() / 2))

    pygame.display.update()
    pygame.time.delay(2000)


# dibuja los niveles completados con la ventana
def draw_level_completed(text):
    LEVEL_PASSED_SOUND.play()
    screen.fill(BLANCO)

    draw_text = LEVEL_COMPLETE_FONT.render(text, True, NEGRO)

    text_x = (WIDTH - draw_text.get_width()) // 2
    text_y = (HEIGHT - draw_text.get_height()) // 2

    screen.blit(draw_text, (text_x, text_y))

    pygame.display.update()
    pygame.time.delay(800)


# compara la secuencia elegida por el jugadr por la seccuencia correcta.
def compare_pressed_button(game_sequence, player_sequence):
    global CORRECT_COLOR

    length_player_sequence = len(player_sequence)
    for i in range(length_player_sequence):
        if player_sequence[i] != game_sequence[i]:
            CORRECT_COLOR = game_sequence[i]
            return False
    return True


if __name__ == "__main__":
    main()