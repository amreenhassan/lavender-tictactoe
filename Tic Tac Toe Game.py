import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_size = 400
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('Pastel Pink Tic Tac Toe')

# Colors (pastel theme)
PASTEL_PINK = (228, 177, 240)
LIGHT_PINK = (228, 177, 240)
WHITE = (255, 255, 255)
PASTEL_GREEN = (255, 225, 255)
PASTEL_BLUE = (67, 56, 120)
# Game variables
grid_size = screen_size // 3
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False

# Fonts
font = pygame.font.SysFont('Arial', 80)

# Function to draw the board
def draw_board():
    for row in range(1, 3):
        pygame.draw.line(screen, LIGHT_PINK, (0, row * grid_size), (screen_size, row * grid_size), 5)
        pygame.draw.line(screen, LIGHT_PINK, (row * grid_size, 0), (row * grid_size, screen_size), 5)

# Function to draw X and O
def draw_markers():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                text = font.render('X', True, PASTEL_GREEN)
                screen.blit(text, (col * grid_size + grid_size // 4, row * grid_size + grid_size // 8))
            elif board[row][col] == 'O':
                text = font.render('O', True, PASTEL_BLUE)
                screen.blit(text, (col * grid_size + grid_size // 4, row * grid_size + grid_size // 8))

# Function to check for a winner
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    
    return None

# Function to check for a draw
def check_draw():
    return all(cell != '' for row in board for cell in row)

# Function to reset the game
def reset_game():
    global board, current_player, game_over
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

# Main game loop
running = True
while running:
    screen.fill(PASTEL_PINK)  # Background color
    draw_board()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            col = mouse_x // grid_size
            row = mouse_y // grid_size

            if board[row][col] == '':
                board[row][col] = current_player
                if check_winner():
                    game_over = True
                elif check_draw():
                    game_over = True
                current_player = 'O' if current_player == 'X' else 'X'

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()

    # Display win or draw message
    if game_over:
        winner = check_winner()
        if winner:
            message = f'{winner} Wins!'
        else:
            message = 'Draw!'

        message_text = font.render(message, True, WHITE)
        screen.blit(message_text, (screen_size // 2 - message_text.get_width() // 2, screen_size // 2 - message_text.get_height() // 2))

    pygame.display.flip()

pygame.quit()
