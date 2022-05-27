import pygame
from checkers.button import Button
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLUE, BLACK
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
font = "assets/big_noodle_titling.ttf"
BG = pygame.image.load("assets/bg.jpeg")

def get_font(size):
    return pygame.font.Font(font, size)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main(mode):
    run = True
    clock = pygame.time.Clock()
    game = Game(SCREEN)

    while run:
        clock.tick(FPS)

        if game.turn == BLUE and mode == "pvc":
            value, new_board = minimax(game.get_board(), 4, BLUE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


def main_menu():
    menu = True
    clock = pygame.time.Clock()

    while menu:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("CHECKERS", True, "#9267ff")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 200))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Button Rect.png"), pos=(400, 350),
                             text_input="PvP", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Button Rect.png"), pos=(400, 475),
                                text_input="PvC", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Button Rect.png"), pos=(400, 600),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main("pvp")
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main("pvc")
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu = False

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

main_menu()
