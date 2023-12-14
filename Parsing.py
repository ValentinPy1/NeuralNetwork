import numpy as np
import re
from itertools import zip_longest


# imgae(matrice) avec 7 chanel( 7 piece) et 3 etat (1 blanc, -1 noir, 0 vide)

# def FENtoBoard(FEN):
#     board = np.zeros((8, 8, 7))
#     print(FEN)
#     FEN = FEN.split(" ")[1]

#     print(FEN)
#     return board

def FENtoOne(FEN, piecesW, piecesB):
    result = ""
    for i in range(len(FEN)):
        if FEN[i].isnumeric():
            result += "0" * int(FEN[i])
        elif FEN[i] in piecesW:
            result += str(piecesW.index(FEN[i]) + 1)
        elif FEN[i] in piecesB:
            result += "-" + str(piecesB.index(FEN[i]) + 1)
        else:
            pass
    return result

def FENtoOneBoard(FEN):
    result = np.zeros((8, 8))
    k = 0
    for i in range(8):
        for j in range(8):
            if FEN[k] != "0":
                if FEN[k] == "-":
                    result[i][j] = -int(FEN[k+1])
                    k += 1
                else:
                    result[i][j] = int(FEN[k])
            k += 1
    return result

def BoardtoRaw(result):
    board = []
    for i in range(6):
        for j in range(8):
            for k in range(8):
                if result[j][k] == i + 1:
                    board.append(1)
                elif result[j][k] == -(i + 1):
                    board.append(-1)
                else:
                    board.append(0)
    return board

def getCastle(castle):
    result = []
    positionW = ["k", "q"]
    positionB = ["K", "Q"]
    for i in range(4):
        if i > len(castle) - 1:
            result.append(0)
            continue
        if castle[i] in positionW:
            result.append(1)
        elif castle[i] in positionB:
            result.append(1)
        else:
            result.append(0)
    return result

def FENtoBoard(FEN):
    print(FEN)
    castle = getCastle(FEN.split(" ")[3])
    tour = FEN.split(" ")[2]
    FEN = FEN.split(" ")[1]
    board = ""
    piecesW = ["r", "n", "b", "q", "k", "p"]
    piecesB = [ "R", "N", "B", "Q", "K", "P"]
    FEN = FENtoOne(FEN, piecesW, piecesB)
    result = FENtoOneBoard(FEN)
    board = BoardtoRaw(result)
    for i in range(len(castle)):
        board.append(castle[i])
    if tour == "w":
        board.append(1)
    else:
        board.append(-1)
    return board


def AllFenToOne():
    fileBoard = open("datasets/datasets/boards/fen_10_pieces.txt", "r")
    file2 = open("datasets/datasets/boards/fen_20_pieces.txt", "r")
    file3 = open("datasets/datasets/boards/fen_lots_pieces.txt", "r")
    fileCheckMat = open("datasets/datasets/checkmate/fen_10_pieces.txt", "r")
    file4 = open("datasets/datasets/checkmate/fen_20_pieces.txt", "r")
    file7 = open("datasets/datasets/checkmate/fen_lots_pieces.txt", "r")

    for line in zip_longest(fileBoard, fileCheckMat, file3, file7, file2, file4, fillvalue=''):
        print(''.join(line), end='')

def AddResFile():
    file = open("datasets/datasets/checkmate/fen_10_pieces.txt", "r")
    for line in file:
        line = line[:-1]
        line += " [0,1,0,0]"
        print(line)

def GetOnlyFen():
    file = open("datasets/datasets/boards/lots_pieces.txt", "r")
    for line in file:
        if line[0] == 'F':
            print(line, end='')


class Parsing():
    def __init__(self):
        self.check_mate = ([], [])
        self.board = ([], [])
        self.data= ([], [])
        self.loadData()
        pass

    def loadData(self):
        file = open("BigData")
        # fileBoard = [open("/home/Tumulus/ThirdYear/Math/B-CNA-500-BAR-5-1-neuralnetwork-thomas.laprie/datasets/datasets/boards/fen_10_pieces.txt", "r")]
        # fileCheckMat = [open("/home/Tumulus/ThirdYear/Math/B-CNA-500-BAR-5-1-neuralnetwork-thomas.laprie/datasets/datasets/checkmate/fen_10_pieces.txt", "r")]
        # fileBoard = [open("datasets/boards/fen_10_pieces.txt", "r"), open("datasets/boards/fen_20_pieces.txt", "r"), open("datasets/boards/fen_lots_pieces.txt", "r")]
        # fileCheckMat = [open("datasets/checkmate/fen_10_pieces.txt", "r"), open("datasets/checkmate/fen_20_pieces.txt", "r"), open("datasets/checkmate/fen_lots_pieces.txt", "r")]
        i = 0
        for line in file:
            if i >= 10:
                break
            i += 1
            self.data[0].append(FENtoBoard(line))
            self.data[1].append(line.split(" ")[7][:-1])
        # for check in fileCheckMat:
        #     for line in check:
        #         if i >= 10:
        #             break
        #         i += 1
        #         self.data[0].append(FENtoBoard(line))
        #         self.data[1].append([0,1,0,0])

    def getData(self, split):
        split_index = int(split * len(self.data[0]))
        training_data = (self.data[0][:split_index], self.data[1][:split_index])
        testing_data = (self.data[0][split_index:], self.data[1][split_index:])
        # print(training_data)
        # print("--------------------------------------------------")
        # print(testing_data)
        # print("--------------------------------------------------")

        return (training_data, testing_data)
