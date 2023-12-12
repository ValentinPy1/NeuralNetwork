import numpy as np

##TODO add one hot encoding
class Ftn:
    def __init__(self):
        self.mapping = {'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
               'p': 7, 'n': 8, 'b': 9, 'r': 10, 'q': 11, 'k': 12, '.': 0}

    def convert(self, fen_str):
        """Convert a fen string to a numeric array (for neural network)
        Args:
            fen_str (str): fen string
        Returns:
            normalized_board (list): list of numeric values
        """

        board = []
        for row in fen_str.split(' ')[0].split('/'):
            current_row = []
            for piece in row:
                if piece.isdigit():
                    current_row.extend([0] * int(piece))
                else:
                    current_row.append(self.mapping[piece])
            board.append(current_row)
        # np.Ie
        flattened_board = [val for row in board for val in row]
        # Normalize the values if needed ( we should try other / if neural network is not learning maybe like / 10.0)
        # normalized_board = [val / 6.0 for val in flattened_board]
        return flattened_board

import ast
import os
import json
import numpy as np

##NEED TO ADD ERROR HANDLING TODO
class Ld:
    def __init__(self):
        self.input = []
        self.target = []

    def fileExists(self, filename):
        """Check if a file exists
        Args:
            filename (string): filepath
        Returns:
            bool: True if file exists, False otherwise
        """

        if os.path.isfile(filename):
            return True
        return False

    def loadinput(self, filename, mode):
        """Load datasets from a file
        Args:
            filename (string): filepath
            mode (string): train or predict
        """

        if not self.fileExists(filename):
            print(f'File "{filename}" does not exist')
            exit(1)
        ftn = Ftn()
        tempInput = []
        tempTarget = []
        with open(filename) as f:
            for line in f:
                if line:
                    l = line.split("|")
                    ftnNumerical = (ftn.convert(l[0]))
                    tempInput.append(ftnNumerical)
                    if mode == "train":
                        tempTarget.append((ast.literal_eval(l[1].strip("\n"))))
        self.input = np.array(tempInput)
        if mode == "train":
            self.target = np.array(tempTarget)

##
## EPITECH PROJECT, 2023
## B-CNA-500-BAR-5-1-neuralnetwork-henry.giraud
## File description:
## fen_to_numeric
##

