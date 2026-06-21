import pygame as py
import numpy as np
import os
import sys # pyright: ignore[reportMissingImports]

py.init()

def main():
    while True:
        
        # Screen reset and board drawing
        screen.fill('black')
        drawBoard()
        drawPieces(screen, board, locations, pieceIDS, sprites)
        
        count = 0
        for key in pieceIDS:
            pieceIDS[key] = sprites[count].get_rect()
            #print(f'Key: {key}, Cnt: {count}, Sprite: {sprites[count]}, IDs: {pieceIDS[key]}')
            screen.blit(sprites[count], pieceIDS[key])
            count = count + 1

        # Event handler
        for event in py.event.get():

            if event.type == py.MOUSEBUTTONDOWN: 
                mousePos = event.pos

            if event.type == py.QUIT:
                py.quit()
                sys.exit()

        # Screen update and clock ticker
        py.display.update()
        fpsClock.tick(FPS)

def drawBoard():
    
    for row in range(0, 8, 1): # iterate through rows
        for col in range(0, 8, 1): # iterate through columns
            if (row + 1) % 2 == 1: # if we are on an even row, follow this ruleset
                if (((row * 8) + (col + 1)) % 2) == 1: # check if column is odd
                    py.draw.rect(screen, LightColor, (col * scale, row * scale, scale, scale)) # if odd, draw a light square
                else:
                    py.draw.rect(screen, DarkColor, (col * scale, row * scale, scale, scale)) # if odd, draw a dark square
            else: # otherwise follow this one
                if (((row * 8) + (col + 1)) % 2) == 0: # check if column is odd
                    py.draw.rect(screen, LightColor, (col * scale, row * scale, scale, scale)) # if odd, draw a dark square
                else:
                    py.draw.rect(screen, DarkColor, (col * scale, row * scale, scale, scale)) # if odd, draw a light square
    
def loadImages() -> list:

    kwIm = py.image.load(os.path.join('Assets', 'king-w.png')).convert_alpha()
    kbIm = py.image.load(os.path.join('Assets', 'king-b.png')).convert_alpha()
    qwIm = py.image.load(os.path.join('Assets', 'queen-w.png')).convert_alpha()
    qbIm = py.image.load(os.path.join('Assets', 'queen-b.png')).convert_alpha()
    bwIm = py.image.load(os.path.join('Assets', 'bishop-w.png')).convert_alpha()
    bbIm = py.image.load(os.path.join('Assets', 'bishop-b.png')).convert_alpha()
    nwIm = py.image.load(os.path.join('Assets', 'knight-w.png')).convert_alpha()
    nbIm = py.image.load(os.path.join('Assets', 'knight-b.png')).convert_alpha()
    rwIm = py.image.load(os.path.join('Assets', 'rook-w.png')).convert_alpha()
    rbIm = py.image.load(os.path.join('Assets', 'rook-b.png')).convert_alpha()
    pwIm = py.image.load(os.path.join('Assets', 'pawn-w.png')).convert_alpha()
    pbIm = py.image.load(os.path.join('Assets', 'pawn-b.png')).convert_alpha()

    pcsImages = [kwIm, kbIm, qwIm, qbIm, bwIm, bbIm, nwIm, nbIm, rwIm, rbIm, pwIm, pbIm]
    return pcsImages


def drawPieces(screen, board: list, locs: list, pcs: dict, sprite: list):

    for i, piece_id in enumerate(board):
        if piece_id in pcs:

            return#must start here


    #print(pcs)


# Initialize clock
FPS = 60
fpsClock = py.time.Clock()

# Starter Variables
dim = 720
scale = dim / 8
LightColor = (156, 135, 109)
DarkColor = (79, 65, 48)

# Generate all 64 locations centered on each tile
locations = []
for row in range(1, 9):
    for column in range(1, 9):
        locations.append((( (scale / 2) * column), (scale / 2 * row)))


# Define initial piece locations
board = ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br',
          'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 
          '0', '0', '0', '0', '0', '0', '0', '0', 
          '0', '0', '0', '0', '0', '0', '0', '0', 
          '0', '0', '0', '0', '0', '0', '0', '0', 
          '0', '0', '0', '0', '0', '0', '0', '0', 
          'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 
          'wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']

# Initialize screen
screen = py.display.set_mode((dim, dim))
py.display.set_caption("Chess but Better!")

# Load images
sprites = loadImages()
print(sprites)

# Assign rectangles to piece id's
pieceIDS = {'wk': 0, 'bk': 1, 'wq': 2, 'bq': 3, 'wb': 4, 'bb': 5, 'wn': 6, 'bn': 7, 'wr': 8, 'br': 9, 'wp': 10, 'bp': 11}


main()

    