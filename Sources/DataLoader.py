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
    data = []
    states = []
    with open(file_path, 'r') as file:
        for line in file:
            fen, state = line.strip().split('|')
            board_matrix, castling_rights, player_to_move = parse_fen(fen)
            combined = np.concatenate((board_matrix.flatten(), castling_rights, [player_to_move]))
            data.append(combined)
            states.append([int(x) for x in state.strip('[]').split(',')])
    data_array = np.array(data)
    states_array = np.array(states)
    return data_array, states_array

def one_hot_encode(x):
    one_hot = np.zeros((x.shape[0], 69, 13))
    for i in range(x.shape[0]):
        for j in range(69):
            one_hot[i][j][x[i][j]] = 1
    return one_hot

def flatten(x):
    return x.reshape(x.shape[0], x.shape[1] * x.shape[2])

def preprocess_data(x, y):
    x = one_hot_encode(x)
    x = flatten(x)
    x_train = x.reshape(x.shape[0], x.shape[1])
    y_train = y.reshape(y.shape[0], y.shape[1])
    perm = np.random.permutation(len(x_train))
    x_train = x_train[perm]
    y_train = y_train[perm]
    return x_train, y_train

def split_data(x, y, split):
    split_index = int(split * len(x))
    x_train, x_test = x[:split_index], x[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]
    return x_train, y_train, x_test, y_test


class Data:
    def __init__(self):
        self.data = {}

    def load(self, path, name):
        try:
            x, y = load_chess_data(path)
        except FileNotFoundError:
            raise FileNotFoundError(f'File {path} not found.')
        self.data[name] = preprocess_data(x, y)
    
    def split(self, name, split, new1, new2):
        if name not in self.data:
            raise KeyError(f'Data {name} not found.')
        if split < 0 or split > 1:
            raise ValueError(f'Split value must be between 0 and 1.')
        x_train, y_train, x_test, y_test = split_data(*self.data[name], split)
        self.data[new1] = (x_train, y_train)
        self.data[new2] = (x_test, y_test)

    def merge(self, name1, name2, new):
        if name1 not in self.data:
            raise KeyError(f'Data {name1} not found.')
        if name2 not in self.data:
            raise KeyError(f'Data {name2} not found.')
        x_train = np.concatenate((self.data[name1][0], self.data[name2][0]))
        y_train = np.concatenate((self.data[name1][1], self.data[name2][1]))
        self.data[new] = (x_train, y_train)
    
    def get(self, name):
        if name not in self.data:
            raise KeyError(f'Data {name} not found.')
        return self.data[name]

    def getSize(self, name):
        if name not in self.data:
            raise KeyError(f'Data {name} not found.')
        return len(self.data[name][0])
