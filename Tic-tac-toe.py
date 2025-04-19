# SPDX-FileCopyrightText: 2025-2026 Asif Amin 
# SPDX-License-Identifier: MIT

import pygame, sys


# Screen dimensions
HEIGHT, WIDTH = 600, 600
LINE_WIDTH = 12
BOARD_ROWS, BOARD_COLS = 3, 3


# Initialize pygame
pygame.init()
pygame.mixer.init()

# Load sounds
try:
    click_sound = pygame.mixer.Sound("click_sound.mp3")  # Load your click sound file
except:
    print("Could not load click sound")

# Load BGM 
try:
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)
except:
    print("Could not load background music")

# Load sound effects
try:
    win_sound = pygame.mixer.Sound("win_sound.mp3")
    tie_sound = pygame.mixer.Sound("tie_sound.mp3")
except:
    print("Could not load sound effects")

# Load background image
try:
    background_img = pygame.image.load('background.jpg')  # Replace with your image file
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
except:
    background_img = None
    print("Could not load background image")

# Load intro image
try:
    intro_img = pygame.image.load('intro_image.jpg')  # Replace with your actual image file
    intro_img = pygame.transform.scale(intro_img, (200, 200))  # Resize as needed
except:
    intro_img = None
    print("Could not load intro image")


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
    o_img = pygame.image.load('o.png')
    x_img = pygame.transform.scale(x_img, (150, 150))
    o_img = pygame.transform.scale(o_img, (150, 150))
except:
    x_img, o_img = None, None

# ========== GAME FUNCTIONS ==========

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_xo(row, col, player):
    x_pos, y_pos = col * 200 + 100, row * 200 + 100
    if player == 'X' and x_img:
        screen.blit(x_img, (x_pos - 75, y_pos - 75))
    elif player == 'O' and o_img:
        screen.blit(o_img, (x_pos - 75, y_pos - 75))
    pygame.display.update()

def check_winner(player):
    padding = 40
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            pygame.draw.line(screen, (255, 140, 0), (padding, y), (600 - padding, y),LINE_WIDTH)
            win_sound.play()  # Play winning sound
            return True

    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            x = col * 200 + 100
            pygame.draw.line(screen, (255, 140, 0), (x, padding), (x, 600 - padding),LINE_WIDTH)
            win_sound.play()  # Play winning sound
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        pygame.draw.line(screen, (255, 140, 0), (padding, padding), (600 - padding, 600 - padding), LINE_WIDTH)
        win_sound.play()  # Play winning sound
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        pygame.draw.line(screen, (255, 140, 0), (600 - padding, padding), (padding, 600 - padding), LINE_WIDTH)
        win_sound.play()  # Play winning sound
        return True

    return False

def check_tie():
    if all(all(cell is not None for cell in row) for row in board):
        tie_sound.play()  # Play tie sound
        return True
    return False

def draw_message(text):
    pygame.draw.rect(screen, (0, 0, 0), (100, 250, 400, 100))
    message = font.render(text, True, WHITE)
    screen.blit(message, (WIDTH//2 - message.get_width()//2, HEIGHT//2 - message.get_height()//2))
    pygame.display.update()

def reset_game():
    global board
    board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(bg_color)
    draw_lines()
    pygame.display.update()

# ========== SCREEN FUNCTIONS ==========

def intro_screen():
    font_large = pygame.font.Font(None, 60)
    font_small = pygame.font.Font(None, 40)

    start_button = pygame.Rect(WIDTH//2 - 100, 200, 200, 60)
    settings_button = pygame.Rect(WIDTH//2 - 100, 300, 200, 60)
    exit_button = pygame.Rect(WIDTH//2 - 100, 400, 200, 60)

    while True:
        screen.fill((30, 30, 30))

        # Draw intro image
        if intro_img:
            screen.blit(intro_img, (WIDTH//2 - 100, 20))  # Adjust position/size

        # Draw buttons
        pygame.draw.rect(screen, (70, 130, 180), start_button)
        pygame.draw.rect(screen, (100, 149, 237), settings_button)
        pygame.draw.rect(screen, (220, 20, 60), exit_button)

        # Render text
        screen.blit(font_large.render("TIC TAC TOE", True, WHITE), (WIDTH//2 - 140, 100))
        screen.blit(font_small.render("Start", True, WHITE), (start_button.x + 70, start_button.y + 15))
        screen.blit(font_small.render("Settings", True, WHITE), (settings_button.x + 45, settings_button.y + 15))
        screen.blit(font_small.render("Exit", True, WHITE), (exit_button.x + 70, exit_button.y + 15))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    click_sound.play()  # Play click sound
                    return 'start'
                elif settings_button.collidepoint(event.pos):
                    click_sound.play()  # Play click sound
                    return 'settings'
                elif exit_button.collidepoint(event.pos):
                    click_sound.play()  # Play click sound
                    pygame.quit()
                    sys.exit()

def sign_selection_screen():
    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 36)

    x_button = pygame.Rect(WIDTH // 2 - 75, 225, 150, 100)
    o_button = pygame.Rect(3 * WIDTH // 4 - 225, 375, 150, 100)
    x_icon = pygame.transform.scale(x_img, (90, 90))
    o_icon = pygame.transform.scale(o_img, (100, 100))


    while True:
        screen.fill((40, 40, 40))

        title = font.render("Player 1, choose your sign:", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))

        pygame.draw.rect(screen, (0, 191, 255), x_button)
        pygame.draw.rect(screen, (255, 105, 180), o_button)

        x_text = small_font.render("X", True, (0, 0, 0))
        o_text = small_font.render("O", True, (0, 0, 0))

        screen.blit(x_icon, (x_button.centerx - x_icon.get_width() // 2, x_button.centery -x_icon.get_height() // 2))

        screen.blit(o_icon, (o_button.centerx - o_icon.get_width() // 2, o_button.centery -o_icon.get_height() // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x_button.collidepoint(event.pos):
                    click_sound.play()  # Play click sound
                    return 'X'
                elif o_button.collidepoint(event.pos):
                    click_sound.play()  # Play click sound
                    return 'O'

def settings_screen():
    slider_rect = pygame.Rect(150, 250, 300, 10)
    knob_radius = 15
    knob_x = 300
    dragging = False
    back_button = pygame.Rect(225, 400, 150, 50)

    while True:
        screen.fill((30, 30, 30))

        # Title
        title_text = font.render("Settings", True, WHITE)
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 100))

        # Volume Label
        volume_label = font.render("Volume", True, (200, 200, 200))
        screen.blit(volume_label, (150, 210))

        # Slider
        pygame.draw.rect(screen, (200, 200, 200), slider_rect)
        pygame.draw.circle(screen, (100, 255, 100), (knob_x, slider_rect.y + 5), knob_radius)

        # Back button
        pygame.draw.rect(screen, (200, 0, 0), back_button)
        back_text = font.render("Back", True, WHITE)
        screen.blit(back_text, (back_button.x + 40, back_button.y + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    click_sound.play()  # Play click sound
                    return
                elif pygame.Rect(knob_x - knob_radius, slider_rect.y, knob_radius*2, knob_radius*2).collidepoint(event.pos):
                    dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.MOUSEMOTION and dragging:
                knob_x = min(max(event.pos[0], slider_rect.left), slider_rect.right)
                volume = (knob_x - slider_rect.left)/slider_rect.width
                pygame.mixer.music.set_volume(volume)

# ========== MAIN GAME ==========

def main(player1_sign):
    global board
    player = player1_sign
    game_over = False

    reset_game()

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

                        # Play click sound
                        try:
                            click_sound.play()
                        except:
                            pass

                        # Redraw background and board
                        if background_img:
                            screen.blit(background_img, (0, 0))
                        else:
                            screen.fill(bg_color)

                        draw_lines()

                        # Redraw all previous marks
                        for r in range(BOARD_ROWS):
                            for c in range(BOARD_COLS):
                                if board[r][c]:
                                    draw_xo(r, c, board[r][c])

                        # Draw current move
                        draw_xo(clicked_row, clicked_col, player)

                        if check_winner(player):
                            try:
                                win_sound.play()
                            except:
                                pass
                            draw_message(f"Player {player} wins!")
                            game_over = True
                        elif check_tie():
                            try:
                                tie_sound.play()
                            except:
                                pass
                            draw_message("It's a tie!")
                            game_over = True
                        else:
                            player = 'O' if player == 'X' else 'X'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    player = player1_sign
                    game_over = False

        pygame.display.flip()


# ========== GAME LOOP ==========

while True:
    choice = intro_screen()
    pygame.event.clear()
    
    if choice == 'start':
        player_sign = sign_selection_screen()
        main(player_sign)
    elif choice == 'settings':
        settings_screen()
    elif choice == 'exit':
        pygame.quit()
        sys.exit()



