# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLUE, BLACK
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
font = "assets/big_noodle_titling.ttf"


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


def draw_text(text, font, color, surface, x, y, size):
    textobj = text_format(text, font, size, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main(mode):
    run = True
    clock = pygame.time.Clock()
    game = Game(screen)

    while run:
        clock.tick(FPS)

        if game.turn == BLUE and mode == "multiplayer":
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
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
    click = False
    clock = pygame.time.Clock()

    while menu:
        button_1 = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 - 50, 200, 100)
        button_2 = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 + 50, 200, 100)
        button_3 = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 + 150, 200, 100)

        if button_1.collidepoint(pygame.mouse.get_pos()):
            if click:
                main("singleplayer")
        if button_2.collidepoint(pygame.mouse.get_pos()):
            if click:
                main("multiplayer")
        if button_3.collidepoint(pygame.mouse.get_pos()):
            if click:
                menu = False

        screen.fill(WHITE)
        draw_text("Checkers", font, BLACK, screen,
                  WIDTH/2 - 100, HEIGHT/2 - 100, 90)
        pygame.draw.rect(screen, RED, button_1)
        pygame.draw.rect(screen, BLUE, button_2)
        pygame.draw.rect(screen, BLACK, button_3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


main_menu()
