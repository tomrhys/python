import pygame
from pygame.locals import *

pygame.init()

# VARIABLES
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_WIDTH = 6
BACKGROUND = (255, 255, 200)
markers = []
clicked = False
pos = [] # POSITION OF MOUSE
player = 1
winner = 0
game_over = False
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
font = pygame.font.SysFont(None, 40)
again_rect = Rect(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 , 160, 50) # MADE A VARIABLE FOR THIS RECT FOR EASE WHEN CHECKING IF IT HAS BEEN CLICKED

# GAME WINDOW
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# WINDOW TITLE
pygame.display.set_caption('TicTacToe')

# GAME GRID
def draw_grid():
    grid = (50, 50, 50)
    screen.fill(BACKGROUND)

    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (SCREEN_WIDTH, x * 100), LINE_WIDTH)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, SCREEN_HEIGHT), LINE_WIDTH)

# SET UP THE BOARD FOR CLICK EVENTS
for x in range (3):
    row = [0] * 3
    markers.append(row)

# FILLING THE CELLS WITH PLAYER'S MARKERS
def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                # DRAWS A CROSS FOR PLAYER 1
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), LINE_WIDTH)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), LINE_WIDTH)
            if y == -1:
                # DRAWS A CIRCLE FOR PLAYER 2
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, LINE_WIDTH)
            y_pos += 1
        x_pos += 1

# CHECKING IF THERE'S A WINNER
def check_winner():

    global winner
    global game_over
    y_pos = 0

    for x in markers:
        # CHECKING COLUMNS
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        # CHECKING ROWS
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    # CHECKING CROSS
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True

# DISPLAY WINNER AND 'PLAY AGAIN' BUTTON
def draw_winner(winner):
    win_text = 'Player ' + str(winner) + ' wins!'
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60, 200, 50))
    screen.blit(win_img, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))

    again_text = 'Play again?'
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 10))

run = True

while run:

    draw_grid()
    draw_markers()

    # EVENT HANDLERS
    # QUITING THE GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # ONCE THERE IS A WINNER, IT WILL NOT ALLOW ANY MORE CLICKS
        if game_over == 0:

            # CHECKING TO SEE IF THERE'S BEEN A FULL MOUSE CLICK CYCLE
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()

    if game_over == True:
        draw_winner(winner)

        # CHECK TO SEE IF USER HAS CLICKED 'PLAY AGAIN'
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked == False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                
                # RESET VARIABLES TO PLAY AGAIN
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False

                # SET UP THE BOARD FOR CLICK EVENTS AGAIN
                for x in range (3):
                    row = [0] * 3
                    markers.append(row)

    pygame.display.update()

pygame.quit()