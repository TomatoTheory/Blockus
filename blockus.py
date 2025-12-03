import numpy as np
from blockus_player import Player
from blockus_piece import Piece

board = np.zeros((20, 20))

blue = Player(1)
red = Player(2)

def place(piece: Piece, x, y):
    corner_offsets = [
        (1, 1), (-1, 1), (-1, -1), (1, -1)
    ]

    side_offsets = [
        (0, 1), (1, 0), (0, -1), (-1, 0)
    ]

    # corner_valid = False
    # for offx, offy in corner_offsets:
    #     if(board[x+offx][y+offy] == piece.color):
    #         corner_valid = True

    if traverse_validate(piece, x, y):
        traverse_insert(piece, x, y)
        return True
    return False

def traverse_validate(piece:Piece, x, y):
    
    x_length, y_length = piece.lt.shape
    for temp_x in range(x_length):
        for temp_y in range(y_length):
            if piece.lt[temp_x][temp_y] != 0:
                if board[x+temp_x][y+temp_y] != 0:
                    return False
                side_offsets = [
                    (0, 1), (1, 0), (0, -1), (-1, 0)
                ]
                for offx, offy in side_offsets:
                    if(board[x+offx][y+offy] == piece.color):
                        return False
    return True

def traverse_insert(piece:Piece, x, y):
    
    x_length, y_length = piece.lt.shape
    for temp_x in range(x_length):
        for temp_y in range(y_length):
            if piece.lt[temp_x][temp_y] != 0:
                board[x+temp_x][y+temp_y] = piece.color


def play():

    won = False
    blue_turn = True

    while(not won):
        print(board)
        valid_position = False
        while(not valid_position):
            if blue_turn:
                count = 1
                for piece in blue.pieces:
                    print(count)
                    print(piece.lt)
                    count += 1
                choice = int(input("Type the number behind your chosen piece."))
                piece = blue.pieces[choice-1]
                rotations = int(input("Type the amount of times you want to rotate the piece."))
                for t in range(rotations):
                    piece.rotate()
                loc_x = int(input("input the x coordinate"))
                loc_y = int(input("input the y coordinate"))
                if(place(piece, loc_x, loc_y)):
                    print("piece placed successfully")
                    valid_position = True
                    blue_turn = not blue_turn
                else:
                    print("invalid position")
            else:
                count = 1
                for piece in red.pieces:
                    print(count)
                    print(piece.lt)
                    count += 1
                choice = int(input("Type the number behind your chosen piece."))
                piece = red.pieces[choice-1]
                rotations = int(input("Type the amount of times you want to rotate the piece."))
                for t in range(rotations):
                    piece.rotate()
                loc_x = int(input("input the x coordinate"))
                loc_y = int(input("input the y coordinate"))
                if(place(piece, loc_x, loc_y)):
                    print("piece placed successfully")
                    valid_position = True
                    blue_turn = not blue_turn
                else:
                    print("invalid position")
        
play()