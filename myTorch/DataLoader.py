import numpy as np

def parse_fen(fen):
    """ Parse the FEN part of a line and return a numerical board representation,
    castling rights, and player to move. """
    pieces = {'p': -1, 'n': -2, 'b': -3, 'r': -4, 'q': -5, 'k': -6,
              'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6}

    board, player, castling, _ = fen.split(' ')[0:4]
    board_matrix = np.zeros((8, 8), dtype=int)

    # Fill the board matrix
    for i, row in enumerate(board.split('/')):
        col = 0
        for char in row:
            if char.isdigit():
                col += int(char)
            else:
                board_matrix[i, col] = pieces[char]
                col += 1

    # Castling rights
    castling_rights = [0, 0, 0, 0] # [K, Q, k, q]
    for char in castling:
        if char == 'K':
            castling_rights[0] = 1
        elif char == 'Q':
            castling_rights[1] = 1
        elif char == 'k':
            castling_rights[2] = 1
        elif char == 'q':
            castling_rights[3] = 1

    # Player to move
    player_to_move = 1 if player == 'w' else -1

    return board_matrix, castling_rights, player_to_move



def load_chess_data(file_path):
    """ Load and parse the chess data from a given file. """
    data = []
    states = []  # For storing the game states

    with open(file_path, 'r') as file:
        for line in file:
            fen, state = line.strip().split('|')
            board_matrix, castling_rights, player_to_move = parse_fen(fen)

            # Combine board, castling rights, and player to move into one array
            combined = np.concatenate((board_matrix.flatten(), castling_rights, [player_to_move]))
            data.append(combined)

            # Add the game state
            states.append([int(x) for x in state.strip('[]').split(',')])

    # Convert lists to NumPy arrays
    data_array = np.array(data)
    states_array = np.array(states)

    return data_array, states_array

# Example usage (assuming the file path is correct)
# file_path = "path_to_your_chess_data_file.txt"
# chess_data, game_states = load_chess_data(file_path)

# Since we can't actually read a file in this environment, this code is just an example.
