import pygame
import random
import time

# Inicialización de Pygame y definición de colores
pygame.init()
pygame.font.init()

# Definición de colores en formato RGB para un tablero de 5x5
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
MORADO = (128, 0, 128)
CIAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
NARANJA = (255, 165, 0)
GRIS = (128, 128, 128)
ROSA = (255, 192, 203)
TURQUESA = (64, 224, 208)
MARRÓN = (139, 69, 19)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE_OLIVA = (128, 128, 0)
VIOLETA = (238, 130, 238)
LIMA = (0, 255, 0)
PLATA = (192, 192, 192)
ORO = (255, 215, 0)
CELESTE = (0, 191, 255)
LAVANDA = (230, 230, 250)
SALVIA = (184, 211, 200)
CORAL = (255, 127, 80)
MARFIL = (255, 255, 240)
CHOCOLATE = (210, 105, 30)

# Dimensiones de la ventana para un tablero de 5x5
WIDTH = 800
HEIGHT = 800

# Definición de fuentes de texto
MAIN_FONT = pygame.font.SysFont('Arial', 40)
LEVEL_FONT = pygame.font.SysFont('arialbold', 35)
LEVEL_COMPLETE_FONT = pygame.font.SysFont('Tahoma', 32)
GAME_OVER_FONT = pygame.font.SysFont('Tahoma', 27)
COLOR_FONT = pygame.font.SysFont('Tahoma', 32)

# Inicialización de Pygame y creación de la ventana
pygame.display.set_caption("Memory matrix")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Definición de sonidos y carga de archivos de sonido
LEVEL_PASSED_SOUND = pygame.mixer.Sound('Assets/level_passed.mp3')
LEVEL_FAILED_SOUND = pygame.mixer.Sound('Assets/level_failed.mp3')
SOUND_1 = pygame.mixer.Sound('Assets/sound_1.mp3')
SOUND_2 = pygame.mixer.Sound('Assets/sound_2.mp3')
SOUND_3 = pygame.mixer.Sound('Assets/sound_3.mp3')
SOUND_4 = pygame.mixer.Sound('Assets/sound_4.mp3')

# Inicialización de variables de juego y cuadrícula de colores
def main():
    sequence_length = level = 1
    game_sequence = generate_color_sequence(sequence_length)
    player_sequence = []

    color_rectangles = {
        ROJO: pygame.Rect(0, 0, 160, 160),
        VERDE: pygame.Rect(0, 0, 160, 160),
        AZUL: pygame.Rect(0, 0, 160, 160),
        AMARILLO: pygame.Rect(0, 0, 160, 160),
        MORADO: pygame.Rect(0, 0, 160, 160),
        CIAN: pygame.Rect(0, 0, 160, 160),
        MAGENTA: pygame.Rect(0, 0, 160, 160),
        NARANJA: pygame.Rect(0, 0, 160, 160),
        GRIS: pygame.Rect(0, 0, 160, 160),
        ROSA: pygame.Rect(0, 0, 160, 160),
        TURQUESA: pygame.Rect(0, 0, 160, 160),
        MARRÓN: pygame.Rect(0, 0, 160, 160),
        BLANCO: pygame.Rect(0, 0, 160, 160),
        NEGRO: pygame.Rect(0, 0, 160, 160),
        VERDE_OLIVA: pygame.Rect(0, 0, 160, 160),
        VIOLETA: pygame.Rect(0, 0, 160, 160),
        LIMA: pygame.Rect(0, 0, 160, 160),
        PLATA: pygame.Rect(0, 0, 160, 160),
        ORO: pygame.Rect(0, 0, 160, 160),
        CELESTE: pygame.Rect(0, 0, 160, 160),
        LAVANDA: pygame.Rect(0, 0, 160, 160),
        SALVIA: pygame.Rect(0, 0, 160, 160),
        CORAL: pygame.Rect(0, 0, 160, 160),
        MARFIL: pygame.Rect(0, 0, 160, 160),
        CHOCOLATE: pygame.Rect(0, 0, 160, 160)

        # Agrega más colores y posiciones para completar un tablero de 5x5
    }

    display_sequence(game_sequence)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
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
                    draw_game_over("Perdiste :(")
                    running = False
                    break
        if running != False:
            draw_window(color_rectangles, str(level))
            clock.tick(60)

def generate_color_sequence(length):
    return [random.choice([ROJO, VERDE, AZUL, AMARILLO, MORADO, CIAN, MAGENTA, NARANJA, GRIS, ROSA, TURQUESA, MARRÓN, BLANCO, NEGRO, VERDE_OLIVA, VIOLETA, LIMA, PLATA, ORO, CELESTE, LAVANDA, SALVIA, CORAL, MARFIL, CHOCOLATE]) for _ in range(length)]

def get_color_string(color):
    color_dictionary = {
        ROJO: "ROJO", VERDE: "VERDE", AZUL: "AZUL", AMARILLO: "AMARILLO",
        MORADO: "MORADO", CIAN: "CIAN", MAGENTA: "MAGENTA", NARANJA: "NARANJA",
        ROSA: "ROSA", TURQUESA: "TURQUESA", GRIS: "GRIS"
    }
    return color_dictionary.get(color, None)

def generate_sound(color):
    sound_dict = {
        ROJO: SOUND_1,
        VERDE: SOUND_2,
        AZUL: SOUND_3,
        AMARILLO: SOUND_4,
        MORADO: SOUND_1,
        CIAN: SOUND_2,
        MAGENTA: SOUND_3,
        NARANJA: SOUND_4,
        GRIS: SOUND_1,
        ROSA: SOUND_2,
        TURQUESA: SOUND_3,
        MARRÓN: SOUND_4,
        BLANCO: SOUND_1,
        NEGRO: SOUND_2,
        VERDE_OLIVA: SOUND_3,
        VIOLETA: SOUND_4,
        LIMA: SOUND_1,
        PLATA: SOUND_2,
        ORO: SOUND_3,
        CELESTE: SOUND_4,
        LAVANDA: SOUND_1,
        SALVIA: SOUND_2,
        CORAL: SOUND_3,
        MARFIL: SOUND_4,
        CHOCOLATE: SOUND_1
    }
    sound = sound_dict.get(color, None)
    sound.play()
    return sound

def display_sequence(sequence):
    for color in sequence:
        generate_sound(color)
        screen.fill(color)
        pygame.display.update()
        time.sleep(1)

def draw_window(color_rectangles, level):
    screen.fill(BLANCO)
    row_count = 0
    col_count = 0
    rect_width = WIDTH // 5
    rect_height = HEIGHT // 5
    for color, rect in color_rectangles.items():
        rect.x = col_count * rect_width
        rect.y = row_count * rect_height
        rect.width = rect_width
        rect.height = rect_height
        pygame.draw.rect(screen, color, rect)
        col_count += 1
        if col_count >= 5:
            col_count = 0
            row_count += 1
    pygame.display.update()

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

def draw_level_completed(text):
    LEVEL_PASSED_SOUND.play()
    screen.fill(BLANCO)
    draw_text = LEVEL_COMPLETE_FONT.render(text, True, NEGRO)
    text_x = (WIDTH - draw_text.get_width()) // 2
    text_y = (HEIGHT - draw_text.get_height()) // 2
    screen.blit(draw_text, (text_x, text_y))
    pygame.display.update()
    pygame.time.delay(800)

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
