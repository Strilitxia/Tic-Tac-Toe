# SPDX-FileCopyrightText: 2025-2026 Asif Amin 
# SPDX-License-Identifier: MIT

import pygame, sys

# Initialize pygame
pygame.init()

# Screen dimensions
HEIGHT, WIDTH = 600, 600
LINE_WIDTH = 12
BOARD_ROWS, BOARD_COLS = 3, 3

# Colors
bg_color = (23, 203, 209)
LINE_COLOR = (11, 12, 13)
TEXT_COLOR = (28, 170, 156)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER = (100, 100, 100)
WHITE = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Tic-Tac-Toe")
font = pygame.font.Font(None, 40)

# Board state
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Load images
try:
    x_img = pygame.image.load('x.png')
    y_img = pygame.image.load('o.png')
    x_img = pygame.transform.scale(x_img, (150, 150))
    y_img = pygame.transform.scale(y_img, (150, 150))
except:
    x_img, y_img = None, None  # Prevent crashes if images are missing

# Draw grid lines
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

# Draw X and O
def draw_xo(row, col, player):
    x_pos, y_pos = col * 200 + 100, row * 200 + 100
    if player == 'X' and x_img:
        screen.blit(x_img, (x_pos - 75, y_pos - 75))
    elif player == 'O' and y_img:
        screen.blit(y_img, (x_pos - 75, y_pos - 75))
    pygame.display.update()

# Check winner
def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

# Check for a tie
def check_tie():
    return all(all(cell is not None for cell in row) for row in board)

# Display message
def draw_message(text):
    message = font.render(text, True, TEXT_COLOR)
    screen.blit(message, (HEIGHT // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.update()

# Draw a button
def draw_button(x, y, width, height, text, hover=False):
    color = BUTTON_HOVER if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=10)
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))

# Show intro screen
def intro_screen():
    while True:
        screen.fill(bg_color)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        start_hover = 200 <= mouse_x <= 400 and 250 <= mouse_y <= 310
        exit_hover = 200 <= mouse_x <= 400 and 350 <= mouse_y <= 410

        draw_button(200, 250, 200, 60, "Start Game", start_hover)
        draw_button(200, 350, 200, 60, "Exit", exit_hover)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_hover:
                    return  # Start the game
                if exit_hover:
                    pygame.quit()
                    sys.exit()

def main():
    global board
    player = 'X'
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX, mouseY = event.pos
                clicked_row, clicked_col = mouseY // 200, mouseX // 200

                if 0 <= clicked_row < BOARD_ROWS and 0 <= clicked_col < BOARD_COLS:
                    if board[clicked_row][clicked_col] is None:
                        board[clicked_row][clicked_col] = player
                        draw_xo(clicked_row, clicked_col, player)

                        winner = check_winner()
                        if winner:
                            draw_message(f"Player {winner} wins!")
                            game_over = True
                        elif check_tie():
                            draw_message("It's a tie!")
                            game_over = True

                        player = 'O' if player == 'X' else 'X'
                else:
                    print("Click outside board!")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
                    screen.fill(bg_color)
                    draw_lines()
                    pygame.display.update()
                    game_over = False
                    player = 'X'

# Run the intro screen
intro_screen()

# Draw the initial grid and start the game
screen.fill(bg_color)
draw_lines()
main()
