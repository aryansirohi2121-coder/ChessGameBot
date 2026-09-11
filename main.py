import pygame
import chess
import sys
from bot import get_best_move

# Config
WIDTH, HEIGHT = 640, 640
DIMENSION = 8
SQ_SIZE = WIDTH // DIMENSION
FPS = 30

LIGHT_COLOR = (238, 238, 210)
DARK_COLOR = (118, 150, 86)
HIGHLIGHT_COLOR = (186, 202, 68)


def load_images():
    """Maps chess pieces to Pygame surface objects."""
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    images = {}
    for p in pieces:
        # Load your downloaded piece of images here:
        try:
            img = pygame.image.load(f"assets/{p}.png")
            images[p] = pygame.transform.scale(img, (SQ_SIZE, SQ_SIZE))
        except FileNotFoundError:
            # Fallback placeholder font if assets aren't downloaded yet
            surf = pygame.Surface((SQ_SIZE, SQ_SIZE), pygame.SRCALPHA)
            font = pygame.font.SysFont('Arial', 32, bold=True)
            text = font.render(p, True, (0, 0, 0) if p[0] == 'b' else (255, 255, 255))
            surf.blit(text, (SQ_SIZE // 4, SQ_SIZE // 4))
            images[p] = surf
    return images


def draw_board(screen, board, selected_sq):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            sq = chess.square(c, 7 - r)
            color = LIGHT_COLOR if (r + c) % 2 == 0 else DARK_COLOR
            if sq == selected_sq:
                color = HIGHLIGHT_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board, images):
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece:
            col = chess.square_file(sq)
            row = 7 - chess.square_rank(sq)
            key = ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().upper()
            screen.blit(images[key], (col * SQ_SIZE, row * SQ_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Chess - [1] Solo PvP | [2] Play vs Bot")
    clock = pygame.time.Clock()

    board = chess.Board()
    images = load_images()

    vs_bot = False  # Toggle with key '2'
    bot_color = chess.BLACK
    selected_sq = None

    running = True
    while running:
        is_bot_turn = vs_bot and (board.turn == bot_color) and not board.is_game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    vs_bot = False
                    pygame.display.set_caption("Mode: 2-Player Pass & Play")
                elif event.key == pygame.K_2:
                    vs_bot = True
                    pygame.display.set_caption("Mode: Playing vs Bot (Black)")
                elif event.key == pygame.K_r:
                    board.reset()
                    selected_sq = None

            elif event.type == pygame.MOUSEBUTTONDOWN and not is_bot_turn and not board.is_game_over():
                x, y = pygame.mouse.get_pos()
                col, row = x // SQ_SIZE, y // SQ_SIZE
                clicked_sq = chess.square(col, 7 - row)

                if selected_sq is None:
                    # Select only pieces belonging to the current side
                    piece = board.piece_at(clicked_sq)
                    if piece and piece.color == board.turn:
                        selected_sq = clicked_sq
                else:
                    # Attempt move or promotion
                    move = chess.Move(selected_sq, clicked_sq)
                    # Auto-promote to Queen for simplicity
                    if chess.Move(selected_sq, clicked_sq, promotion=chess.QUEEN) in board.legal_moves:
                        move = chess.Move(selected_sq, clicked_sq, promotion=chess.QUEEN)

                    if move in board.legal_moves:
                        board.push(move)
                    selected_sq = None

        # Bot Move Execution
        if is_bot_turn:
            bot_move = get_best_move(board, depth=3)
            if bot_move:
                board.push(bot_move)

        draw_board(screen, board, selected_sq)
        draw_pieces(screen, board, images)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()