import chess.pgn
import io
import sys

def normalize_pgn(pgn_string):
    game = chess.pgn.read_game(io.StringIO(pgn_string))
    board = game.board()

    # Obtenez tous les coups dans le format UCI
    uci_moves = [move.uci() for move in game.mainline_moves()]

    # Recréez la partie à partir des coups UCI
    new_game = chess.pgn.Game()
    new_node = new_game
    uci_moves.pop()
    uci_moves.pop()
    for uci_move in uci_moves:
        move = chess.Move.from_uci(uci_move)
        board.push(move)

        new_node = new_node.add_variation(move)
    res = ""
    for line in new_game.__str__().split("\n"):
        if len(line)!= 0 and line[0] == '1':
            # print(line)
            res = line
            break
    return res

def get_fen_from_pgn_stalemate_checkmate(pgn_string):
    pgn_game = chess.pgn.read_game(io.StringIO(pgn_string))
    last_position = pgn_game.end().board()
    if pgn_game.end().board().is_checkmate():
        print(last_position.fen(), "|[1, 0, 0, 0]")
        get_fen_from_pgn_board(normalize_pgn(pgn_string))
    if pgn_game.end().board().is_stalemate():
        print(last_position.fen(), "|[0, 0, 1, 0]")
        get_fen_from_pgn_board(normalize_pgn(pgn_string))

def get_fen_from_pgn_board(pgn_string):
    if (pgn_string.count("6.") == 0):
        return
    pgn_game = chess.pgn.read_game(io.StringIO(pgn_string.split("6.")[0]))
    last_position = pgn_game.end().board()
    if pgn_game.end().board().is_check():
        print(last_position.fen(), "|[0, 1, 0, 0]")
    else:
        print(last_position.fen(), "|[0, 0, 0, 1]")

if __name__ == "__main__":
    # res = Parsing.Parsing()
    # print(res.data)
    # AllFenToOne()
    # AddResFile()
    # GetOnlyFen()
    # generateChessBoard()
    data = open(sys.argv[1], "r")
    for line in data:
        if line[0] == '1':
            # print(line)
            # print(normalize_pgn(line))
            get_fen_from_pgn_stalemate_checkmate(line)
    
    data.close()
