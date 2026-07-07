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
    
    def matDifference(matrix: list, reference: tuple, target: tuple) ->  tuple:
        # Find indices of reference and target
        referenceLocation = MyFunctions.matIndex(matrix, reference)
        targetLocation = MyFunctions.matIndex(matrix, target)
        return (-1 * (targetLocation[0] - referenceLocation[0]), targetLocation[1] - referenceLocation[1])

class Tile:

    def __init__(self, pieceID: str, image):
        self.pieceID = pieceID
        self.image = image
        self.hitbox = image.get_rect()
        self.isSelected = False
        self.locationHistory = []

class MoveSet():

    def __init__(self):
        self.checks = {'p': self.Pawn, 
                  'n': self.Knight, 
                  'b': self.Bishop, 
                  'r': self.Rook, 
                  'k': self.King, 
                  'q': self.Queen}

    def Pawn(self, board: list, locations: list, chessPiece: Tile, pieces: list, locationDifference):

        if len(chessPiece.locationHistory) <= 1 and (locationDifference == (1, 0) or locationDifference == (2, 0)):
            return True
        elif len(chessPiece.locationHistory) > 1 and locationDifference == (1, 0):
            return True
        else:
            return False
        

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
    

    def MoveCheck(self, board: list, locations: list, chessPiece: Tile, pieces: list) -> bool:
        
        validMove = False

        # Rotate board to black perspective if black's move
        if chessPiece.pieceID[0] == 'b':
            board = MyFunctions.flipMat(board)
            locations = MyFunctions.flipMat(locations)

        # Get piece location based on board row and column index
        pcsIdx = MyFunctions.matIndex(locations, chessPiece.locationHistory[-1])

        locDif = MyFunctions.matDifference(locations, chessPiece.locationHistory[-1], chessPiece.hitbox.center)
        print(locDif)

        return self.checks['p'](board, locations, chessPiece, pieces, locDif)
    

