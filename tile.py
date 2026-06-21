import pygame as py
import os, sys

py.init()

class MyFunctions:

    def flipMat(matrix: list) -> list:
        return [row[::-1] for row in matrix[::-1]]
    
    def matIndex(matrix: list, value) -> tuple:
        # Assume only one appearance of "value"
        for idx, row in enumerate(matrix):
            if value in row:
                return (idx, row.index(value))
        return 'You Messed Up'



class Tile:

    def __init__(self, pieceID: str, image):
        self.pieceID = pieceID
        self.image = image
        self.hitbox = image.get_rect()
        self.isSelected = False
        self.locationHistory = []

class MoveSet():

    def Pawn():

        return True

    def Knight():

        return True
    
    def Bishop():

        return True
    
    def Rook():

        return True
    
    def King():

        return True
    
    def Queen():

        return True
    
    checks = {'p': Pawn(), 'n': Knight(), 'b': Bishop(), 'r': Rook(), 'k': King(), 'q': Queen()}

    def MoveCheck(board: list, locations: list, chessPiece: Tile, pieces: list):
        
        validMove = False

        # Rotate board to black perspective if black's move
        if chessPiece.pieceID[0] == 'b':
            board = MyFunctions.flipMat(board)
            locations = MyFunctions.flipMat(locations)

        # Get piece location based on board row and column index
        pcsIdx = MyFunctions.matIndex(locations, chessPiece.locationHistory[-1])
        legalMoves = [(pcsIdx[0] - 1, pcsIdx[1]), (pcsIdx[0] - 2, pcsIdx[1])]

        

        return validMove
    

