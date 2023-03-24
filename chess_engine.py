
# add file description here at the top







class GameState():

    def __init__(self):
        
        # first char: color of piece (B or W); second char: type of piece - King (K), queen (Q), Rook (R), Bishop (B), Knight (N), Pawn (P), or Empty (.)
        self.board = [
            ["bR", "bK", "bB", "bQ", "bK", "bB", "bK", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wK", "wB", "wQ", "wK", "wB", "wK", "wR"],
        ] 

        self.moveLog = []
        self.whiteMove = False 