import numpy as np
import re


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




class Parsing():
    def __init__(self):
        self.check_mate = ([], [])
        self.board = ([], [])
        self.loadData()
        pass

    def loadData(self):
        fileBoard = [open("datasets/boards/fen_10_pieces.txt", "r"), open("datasets/boards/fen_20_pieces.txt", "r"), open("datasets/boards/fen_lots_pieces.txt", "r")]
        fileCheckMat = [open("datasets/checkmate/fen_10_pieces.txt", "r"), open("datasets/checkmate/fen_20_pieces.txt", "r"), open("datasets/checkmate/fen_lots_pieces.txt", "r")]
        for board in fileBoard:
            for line in board:
                self.board[0].append(FENtoBoard(line))
                self.board[1].append([1,0,0,0])
                break
        for check in fileCheckMat:
            for line in check:
                self.check_mate[0].append(FENtoBoard(line))
                self.check_mate[1].append([0,1,0,0])
                break
        print(self.board)
        print(self.check_mate)

    def getData(self, split):
        data = self.board + self.check_mate
        split_index = int(split * len(data))
        np.random.shuffle(data)
        training_data = data[:split_index]
        testing_data = data[split_index:]
        return (training_data, testing_data)