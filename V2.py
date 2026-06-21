import pygame as py
import os, sys, math 
from tile import Tile, MoveSet

# initialize pygame
py.init()

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

    # Put loaded images into list and scale accordingly
    pcsImages = {'wk': kwIm, 'bk': kbIm, 'wq': qwIm, 'bq': qbIm, 'wb': bwIm, 'bb': bbIm, 
                 'wn': nwIm, 'bn': nbIm, 'wr': rwIm, 'br': rbIm, 'wp': pwIm, 'bp': pbIm}
    
    # Scale images to be slightly smaller than board tile
    for idx, image in pcsImages.items():
        pcsImages[idx] = py.transform.scale(image, (scale * 0.8, scale * 0.8))

    return pcsImages

# Start Variables
dim = 720
scale = dim / 8
LightColor = (156, 135, 109)
DarkColor = (79, 65, 48)
dragging = False
playerColor = 'w'

# Grid locations
locations = [[],[],[],[],[],[],[],[],[],[]]
for row in range(0, 10):
    for column in range(0, 10):
        if (row == 0) | (row == 9):
            locations[row].append('B')
        elif (column == 0) | (column == 9):
            locations[row].append('B')
        else:
            locations[row].append((( (scale * (column - 1)) + scale / 2), (scale * (row - 1)) + scale / 2))


# Game board
board = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
         ['B', 'br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br', 'B'],
         ['B', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'B'],
         ['B', '0', '0', '0', '0', '0', '0', '0', '0', 'B'],
         ['B', '0', '0', '0', '0', '0', '0', '0', '0', 'B'],
         ['B', '0', '0', '0', '0', '0', '0', '0', '0', 'B'],
         ['B', '0', '0', '0', '0', '0', '0', '0', '0', 'B'],
         ['B', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'B'], 
         ['B', 'wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr', 'B'],
         ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]

# Screen and running
running = True
screen = py.display.set_mode((dim, dim))
py.display.set_caption("Chess but Better!")

# Load images and construct board pieces

sprites = loadImages()
pieces = []
for num, row in enumerate(board):
    for idx, pc in enumerate(row):
        if (pc != '0') & (pc != 'B'):
            tempPiece = Tile(pc, sprites[pc])
            tempPiece.hitbox.center = locations[num][idx]
            tempPiece.locationHistory.append(tempPiece.hitbox.center)
            pieces.append(tempPiece)


# Run the main game loop
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            py.quit()
            sys.exit()
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1: # Check for left click
                mousePosition = event.pos
                
                # Loop through pieces for movement
                for pc in pieces:
                    if pc.hitbox.collidepoint(mousePosition) & (pc.pieceID[0] == playerColor): # Begin dragging if player color piece is clicked
                        dragging = True
                        pc.isSelected = True # Flag as clicked piece
                        pc.hitbox.center = mousePosition # Move to cursor

        if event.type == py.MOUSEMOTION:
            mousePosition = event.pos 

            # Loop through pieces for movement
            for pc in pieces:
                if dragging & pc.isSelected: # Ensure only clicked piece is moved
                    pc.hitbox.center = mousePosition # Follow cursor

        if event.type == py.MOUSEBUTTONUP:
            mousePosition = event.pos
            if event.button == 1: # Check for left click released
                for pc in pieces:
                    if pc.isSelected: # Ensure only clicked piece is moved
                        pc.hitbox.center = min((loc for row in locations for loc in row if type(loc) != str), key=lambda c: math.dist(c, mousePosition)) # Place at grid location on release
                        dragging = False     
                        pc.isSelected = False
                        
                        if MoveSet.MoveCheck(board, locations, pc, pieces): # Check if movement was legal
                            pc.locationHistory.append(pc.hitbox.center)
                        else:
                            pc.hitbox.center = pc.locationHistory[-1]




    # Rendering
    screen.fill('black')
    drawBoard()

    for pc in pieces:
        screen.blit(pc.image, pc.hitbox)

    py.display.flip()
    
