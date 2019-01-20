# tetris.py":Version without More Ideas
#Name:Tailin Zhang
#Id:tailinz
#Time:...too difficult,20h

import random
from Tkinter import *

def keyPressed(event):
    # first process keys that work even if the game is over and paused
    # now process keys that only work if the game is not over and not paused
    if event.char == 'r':
        init()
    if event.char == 'p':
            pause()
    if canvas.data.isGameOver==False and canvas.data.pause==False:
        if event.keysym== 'Left':
            moveFallingPiece(0, -1)
        if event.keysym == 'Right':
            moveFallingPiece(0, 1)
        if event.keysym == 'Down':
            moveFallingPiece(1, 0)
        if event.keysym == 'Up':
            rotateFallingPiece()
        if event.keysym=='space':
            hardDrop()
        if event.char == 't':
            rotateFallingPiece()
            rotateFallingPiece()
        if event.char == 'c':
            changeSpeed()    
            #print canvas.data.delay

    redrawAll()

def changeSpeed():
    print "change speed:" ,
    if canvas.data.delay==500:
        canvas.data.delay=1000
        print 'slow'
    elif canvas.data.delay==1000:
        canvas.data.delay=200
        print'fast'
    elif canvas.data.delay==200:
        canvas.data.delay=500
        print 'normal'
    

def pause():
    if canvas.data.pause==False:
        canvas.data.pause=True
    else:
        canvas.data.pause=False

def hardDrop():
    #immediately drops a piece as far as it can go and places it on the board
    rows=canvas.data.rows 
    fallingPieceRow=canvas.data.fallingPieceRow
    for r in xrange(fallingPieceRow,rows):
        canvas.data.fallingPieceRow=r
        if fallingPieceIsLegal()==False:
            canvas.data.fallingPieceRow=r-1
            break
    redrawAll()
        
    
    
def rotateFallingPiece():
    #in that it makes the rotation and then calls fallingPieceIsLegal and undoes any illegal changes.\
    # A new 2d list is created, and cells in the old list are mapped to cells in the new list according to a 90-degree counterclockwise rotation.
    oldRow=canvas.data.fallingPieceRow
    oldCol=canvas.data.fallingPieceCol
    oldPiece=canvas.data.piece
    (oldCenterRow, oldCenterCol)=fallingPieceCenter(canvas)
    canvas.data.piece=rotate(canvas.data.piece)
    (newCenterRow, newCenterCol)=fallingPieceCenter(canvas)
    canvas.data.fallingPieceRow+=(oldCenterRow - newCenterRow)
    canvas.data.fallingPieceCol+=(oldCenterCol - newCenterCol)
    if fallingPieceIsLegal()==False:
        canvas.data.fallingPieceRow=oldRow
        canvas.data.fallingPieceCol=oldCol
        canvas.data.piece=oldPiece
            
            
def rotate(piece):   
    #create a new rotated piece
    newRow=len(piece[0])
    newCol=len(piece)
    newPiece=[]
    for r in xrange(newRow):
        newPiece+=[[]]
        for c in xrange(newCol):
            newPiece[r]+=['']
    for r in xrange(len(piece)):
        for c in xrange(len(piece[0])):
            newPiece[newRow-c-1][r]=piece[r][c]
    return newPiece


def fallingPieceCenter(canvas):
    #find piece center
    piece=canvas.data.piece
    fallingPieceRow=canvas.data.fallingPieceRow
    fallingPieceCol=canvas.data.fallingPieceCol
    return((len(piece))/2+fallingPieceRow,(len(piece[0]))/2+fallingPieceCol)


def moveFallingPiece(drow, dcol):
    #move the falling piece a given number of rows and columns:
    canvas.data.fallingPieceRow+=drow
    canvas.data.fallingPieceCol+=dcol
    if fallingPieceIsLegal()==False:
        canvas.data.fallingPieceRow-=drow
        canvas.data.fallingPieceCol-=dcol
        return False
        
        
def fallingPieceIsLegal():
    #Check if the piece change is legal
    piece=canvas.data.piece
    fallingPieceRow=canvas.data.fallingPieceRow
    fallingPieceCol=canvas.data.fallingPieceCol
    board=canvas.data.board
    rows=canvas.data.rows 
    cols=canvas.data.cols 
    for r in xrange(len(piece)):
        for c in xrange(len(piece[r])):
            if piece[r][c]==True:
                if fallingPieceRow+r<0 or fallingPieceRow+r>=rows\
                    or fallingPieceCol+c<0 or fallingPieceCol+c>=cols \
                    or board[fallingPieceRow+r][fallingPieceCol+c] !='blue':
                    return False
    return True
                
                    

def newFallingPiece():
    #The newFallingPiece function is responsible for randomly choosing a new piece,\
    #setting its color, and positioning it in the middle of the top row.
    canvas.data.piece=canvas.data.tetrisPieces[random.randint(0, 6)]
    #canvas.data.piece=canvas.data.tetrisPieces[3]
    canvas.data.color=canvas.data.tetrisPieceColors[random.randint(0, 6)]
    canvas.data.fallingPieceRow=0
    canvas.data.fallingPieceCol=canvas.data.cols /2-len(canvas.data.piece[0])/2
    
def timerFired():
    #make the whole board to change with certain time interval
    if canvas.data.isGameOver==False and canvas.data.pause==False:
        test=moveFallingPiece(+1,0)
        if test==False:
            placeFallingPiece()
            newFallingPiece()
        if fallingPieceIsLegal()==False:
            canvas.data.isGameOver=True
    redrawAll()
    canvas.after(canvas.data.delay, timerFired)
    
    
def placeFallingPiece():
    #put the falling piece into the board while reach the end and launch a new piece
    piece=canvas.data.piece
    color=canvas.data.color
    for r in xrange(len(piece)):
        for c in xrange(len(piece[r])):
            if piece[r][c]==True:
                    canvas.data.board[canvas.data.fallingPieceRow+r][canvas.data.fallingPieceCol+c]=color
    removeFullRows()
                    

def removeFullRows():
    # start from the bottom looking for full row,clear full rows and build new rows, update score
    board=canvas.data.board
    rows=canvas.data.rows 
    cols=canvas.data.cols
    count=0
    newRow=rows-1
    for oldRow in range(rows)[::-1]:
        if 'blue' in board[oldRow]:
            for c in xrange(cols):
                board[newRow][c]=board[oldRow][c]
            newRow-=1
        else: count+=1
    for r in xrange(newRow):
        for c in xrange(cols):
            canvas.data.board[r][c]='blue'
    canvas.data.score+=count**2
            
def redrawAll():
    #redraw background,board,score
    canvas.delete(ALL)
    drawboard()
    drawscore()

def drawscore():
    #draw the score
    canvas.create_text(25,328,text='score: '+str(canvas.data.score),\
                       font='Helvetica 14',fill = 'black',anchor = 'nw')
    if random.randint(0, 3)==1:
        canvas.create_text(random.randint(0, 100),random.randint(0, 400),text='puta'+str(canvas.data.score),\
                       font='Helvetica 8',fill = 'green',anchor = 'nw')    


def drawboard():
    #draw the background of the entire game (orange in the pict), draw the board, draw the piece, draw gameover
    canvas.create_rectangle(0,0,canvas.data.canvasWidth,canvas.data.canvasHeight, fill = 'orange')
    board=canvas.data.board
    rows=canvas.data.rows 
    cols=canvas.data.cols 
    for r in xrange(rows):
        for c in xrange(cols):
            drawCell(r, c,board[r][c] )
    drawFallingPiece()
    if canvas.data.isGameOver==True:
        canvas.create_text(25,3,text='Game Over', font='Helvetica 14',fill = 'black',anchor = 'nw')

def drawFallingPiece():
    #the falling piece is drawn over the board
    piece=canvas.data.piece
    color=canvas.data.color
    for r in xrange(len(piece)):
        for c in xrange(len(piece[r])):
            if piece[r][c]==True:
                    drawCell(canvas.data.fallingPieceRow+r,canvas.data.fallingPieceCol+c,color)
                    

def drawCell(rows, cols, color):
    #draw the cells
    margin=canvas.data.margin
    cellSize=canvas.data.cellSize 
    cellMargin =canvas.data.cellMargin 
    canvas.create_rectangle( margin + cols*cellSize,margin + rows*cellSize,\
                             margin + (cols+1)*cellSize,margin + (rows+1)*cellSize,\
                             fill=color,width=cellMargin)


def init():
    #set up global variables
    #Allocate our board as a 2-dimensional list of names of colors, and fill it with our emptyColor ("blue"),and store the both things. 
    canvas.data.isGameOver=False
    canvas.data.pause=False
    canvas.data.score=0
    canvas.data.board = []
    board=canvas.data.board
    rows=canvas.data.rows 
    cols=canvas.data.cols 
    for r in xrange(rows):
        board+=[[]]
        for c in xrange(cols):
            board[r]+=['blue']
    canvas.data.BoardPieces = []
    canvas.data.BoardPieceColors = []
    canvas.data.tetrisPieces = Allpiece()
    canvas.data.tetrisPieceColors = ["red","yellow","magenta","pink","cyan","green","orange"]
    newFallingPiece()
    redrawAll()

def Allpiece():
    #return Seven "standard" pieces (tetrominoes)
    iPiece = [[ True,  True,  True,  True]]
    jPiece = [[ True, False, False ],[ True, True,  True]]
    lPiece = [[ False, False, True],[ True,  True,  True]]
    oPiece = [[ True, True],[ True, True]]
    sPiece = [[ False, True, True],[ True,  True, False ]]
    tPiece = [[ False, True, False ],[ True,  True, True]]
    zPiece = [[ True,  True, False ],[ False, True, True]]
    return [iPiece,jPiece,lPiece,oPiece,sPiece,tPiece,zPiece]
    

def run():
    # create the root and the canvas
    #take the rows and columns as parameters, and use these values to create a properly sized window.
    global canvas
    root = Tk()
    rows = 15
    cols = 10
    margin = 25
    cellSize = 20
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)
    # makes window non-resizable
    class Struct: pass
    canvas.data = Struct()
    # Set up canvas data and call init
    canvas.data.rows = rows
    canvas.data.cols = cols
    canvas.data.margin = margin
    canvas.data.cellSize = cellSize
    canvas.data.cellMargin = 2
    canvas.data.canvasWidth = canvasWidth
    canvas.data.canvasHeight = canvasHeight
    canvas.data.delay = 500
    init()
    # set up events
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()
    # This call BLOCKS (so your program waits until you close the window!)
 
run()




