
#Name:Tailin Zhang
#Id:tailinz

###Intro:
##The goal of this game is to defend the yellow energy core at the bottom.
##Player may use the red tank to fight against the two bot purle and blue tanks.
##More bots can be easily added by simply copying the program and changing the number in the bots' methods.
##Press'up','down','left','right' to move your tank, 's' to shoot a bullet, and you can not shoot a new bullet until the old one explods.
##Your scores will increase through out time and you can either gain extra points by shooting an enermy or just collides with it, although the latter situation will send you to the default location.
##The enermy can not be pernamentally killed, while they will be sent to random location when damaged.
##So try sustain as long as you can.
###
#Add backgroud, page intro
############################################################################################################################################################################################     

import random
from Tkinter import *

############################################################################################################################################################################################     
#real player part#

def newPlayer():
    cd.playerX=280
    cd.playerY=480  
    cd.playerDic='u'

def movePlayer(dx,dy):
    if playerIsLegal(cd.playerX+dx,cd.playerY+dy)==True:
        cd.playerX+=dx
        cd.playerY+=dy 

def playerIsLegal(x,y):
    board=cd.board
    cellSize=cd.cellSize
    if x<0 or y<0 or x>560 or y>560:
        return False
    for ax in xrange(3):
        for ay in xrange(3):
            if ax==2:
                col=(x-1)/cellSize+ax
            else:
                col=x/cellSize+ax
            if ay==2:
                row=(y-1)/cellSize+ay           
            else:
                row=y/cellSize+ay
            if board[row][col]!='green':
                return False
    return True
    


def drawPlayer():
    x=cd.playerX
    y=cd.playerY
    canvas.create_rectangle( x,y,x+40,y+40, fill='red',width=0)
    if cd.playerDic=='u':
        canvas.create_rectangle( x+15,y-10,x+25,y+20,fill='orange',width=0)
        canvas.create_rectangle( x,y,x+5,y+40,fill='orange',width=0)
        canvas.create_rectangle( x+35,y,x+40,y+40,fill='orange',width=0)
    if cd.playerDic=='d':
        canvas.create_rectangle( x+15,y+20,x+25,y+50,fill='orange',width=0)
        canvas.create_rectangle( x,y,x+5,y+40,fill='orange',width=0)
        canvas.create_rectangle( x+35,y,x+40,y+40,fill='orange',width=0)
    if cd.playerDic=='l':
        canvas.create_rectangle( x-10,y+15,x+20,y+25,fill='orange',width=0)
        canvas.create_rectangle( x,y,x+40,y+5,fill='orange',width=0)
        canvas.create_rectangle( x,y+35,x+40,y+40,fill='orange',width=0)
    if cd.playerDic=='r':
        canvas.create_rectangle( x+20,y+15,x+50,y+25,fill='orange',width=0)
        canvas.create_rectangle( x,y,x+40,y+5,fill='orange',width=0)
        canvas.create_rectangle( x,y+35,x+40,y+40,fill='orange',width=0)



############################################################################################################################################################################################       
#player shoots bullets#
        
def newbullet():
    cd.canShoot=False
    d=cd.playerDic
    cd.oneDic=d
    x=cd.playerX
    y=cd.playerY
    if d=='u':
        cd.bulletX=cd.playerX+15
        cd.bulletY=cd.playerY-10
    if d=='d':
        cd.bulletX=cd.playerX+15  
        cd.bulletY=cd.playerY+2*cd.cellSize
    if d=='l':
        cd.bulletX=cd.playerX-10
        cd.bulletY=cd.playerY+15
    if d=='r':
        cd.bulletX=cd.playerX +2*cd.cellSize 
        cd.bulletY=cd.playerY+15
    

def printbullet():
    canvas.create_rectangle( cd.bulletX,cd.bulletY,(cd.bulletX)+10,(cd.bulletY)+10,fill='orange')
                          
def bulletIsLegal(x,y): 
    board=cd.board
    cellSize=cd.cellSize
    if x<0 or y<0 or x>590 or y>590:
        return False
    if board[y/cellSize][x/cellSize]!='green':
        cd.board[y/cellSize][x/cellSize]='green'
        return False
    if board[y/cellSize][(x+9)/cellSize]!='green':
        cd.board[y/cellSize][(x+9)/cellSize]='green'
        return False
    if board[(y+9)/cellSize][x/cellSize]!='green':
        cd.board[(y+9)/cellSize][x/cellSize]='green'
        return False
    if board[(y+9)/cellSize][(x+9)/cellSize]!='green':
        cd.boarddr=board[(y+9)/cellSize][(x+9)/cellSize]='green'
        return False
    return True
    

def fly():
    d=cd.oneDic
    x=cd.bulletX
    y=cd.bulletY
    if bulletIsLegal(cd.bulletX,cd.bulletY):
        if d=='u':
            cd.bulletY-=20
        if d=='d':
            cd.bulletY+=20
        if d=='l':
            cd.bulletX-=20
        if d=='r':
            cd.bulletX+=20
    else:
        cd.shoot=False
        cd.canShoot=True

    

############################################################################################################################################################################################
#build the bot1#


def newBot():
    randomDic()
    cd.botX=random.randint(0, 560)/10*10
    cd.botY=random.randint(0, 440)/10*10
    while playerIsLegal(cd.botX,cd.botY)==False:
        cd.botX=random.randint(0, 560)/10*10
        cd.botY=random.randint(0, 440)/10*10

def randomDic():
    chooseDic=random.randint(0,3)
    if chooseDic==0:
        cd.botDic='u'
    if chooseDic==1:
        cd.botDic='d'
    if chooseDic==2:
        cd.botDic='l'
    if chooseDic==3:
        cd.botDic='r'
   
def moveBot():
    choose=random.randint(0,19)
    if choose==0:
        randomDic()
    else:
        if cd.botDic=='u'and playerIsLegal(cd.botX,cd.botY-10)==True:
            cd.botY-=10
        elif cd.botDic=='d'and playerIsLegal(cd.botX,cd.botY+10)==True:
            cd.botY+=10
        elif cd.botDic=='l'and playerIsLegal(cd.botX-10,cd.botY)==True:
            cd.botX-=10
        elif cd.botDic=='r'and playerIsLegal(cd.botX+10,cd.botY)==True:
            cd.botX+=10
        elif  cd.botX==0 or cd.botX==560 or cd.botY==0 or cd.botY==560:
            randomDic()
            
        
             
def drawBot():
    x=cd.botX
    y=cd.botY
    canvas.create_rectangle( x,y,x+40,y+40,fill='blue',width=0)
    if cd.botDic=='u':
        
        canvas.create_rectangle( x+15,y-10,x+25,y+20,fill='purple',width=0)
        canvas.create_rectangle( x,y,x+5,y+40,fill='purple',width=0)
        canvas.create_rectangle( x+35,y,x+40,y+40,fill='purple',width=0)
    if cd.botDic=='d':
        
        canvas.create_rectangle( x+15,y+20,x+25,y+50,fill='purple',width=0)
        canvas.create_rectangle( x,y,x+5,y+40,fill='purple',width=0)
        canvas.create_rectangle( x+35,y,x+40,y+40,fill='purple',width=0)
    if cd.botDic=='l':
    
        canvas.create_rectangle( x-10,y+15,x+20,y+25,fill='purple',width=0)
        canvas.create_rectangle( x,y,x+40,y+5,fill='purple',width=0)
        canvas.create_rectangle( x,y+35,x+40,y+40,fill='purple',width=0)
    if cd.botDic=='r':
       
        canvas.create_rectangle( x+20,y+15,x+50,y+25,fill='purple',width=0)
        canvas.create_rectangle( x,y,x+40,y+5,fill='purple',width=0)
        canvas.create_rectangle( x,y+35,x+40,y+40,fill='purple',width=0)


############################################################################################################################################################################################
#bot1 shoots bullets#


def Bnewbullet():
    cd.BcanShoot=False
    d=cd.botDic
    cd.BoneDic=d
    x=cd.botX
    y=cd.botY
    if d=='u':
        cd.BbulletX=cd.botX+15
        cd.BbulletY=cd.botY-10
    if d=='d':
        cd.BbulletX=cd.botX+15  
        cd.BbulletY=cd.botY+2*cd.cellSize
    if d=='l':
        cd.BbulletX=cd.botX-10
        cd.BbulletY=cd.botY+15
    if d=='r':
        cd.BbulletX=cd.botX +2*cd.cellSize 
        cd.BbulletY=cd.botY+15
    

def Bprintbullet():
    canvas.create_rectangle( cd.BbulletX,cd.BbulletY,(cd.BbulletX)+10,(cd.BbulletY)+10,fill='purple')                          


def Bfly():
    d=cd.BoneDic
    x=cd.BbulletX
    y=cd.BbulletY
    if x>275 and x<315 and y>555 and y<595:
        cd.isGameOver=True
        cd.Bshoot=False
    if bulletIsLegal(cd.BbulletX,cd.BbulletY):
        if d=='u':
            cd.BbulletY-=20
        if d=='d':
            cd.BbulletY+=20
        if d=='l':
            cd.BbulletX-=20
        if d=='r':
            cd.BbulletX+=20
    else:
        cd.Bshoot=False
        cd.BcanShoot=True
############################################################################################################################################################################################
#draw bot2#

def newBot2():
    randomDic2()
    cd.botX2=random.randint(0, 560)/10*10
    cd.botY2=random.randint(0, 440)/10*10
    while playerIsLegal(cd.botX2,cd.botY2)==False:
        cd.botX2=random.randint(0, 560)/10*10
        cd.botY2=random.randint(0, 440)/10*10


def randomDic2():
    chooseDic=random.randint(0,3)
    if chooseDic==0:
        cd.botDic2='u'
    if chooseDic==1:
        cd.botDic2='d'
    if chooseDic==2:
        cd.botDic2='l'
    if chooseDic==3:
        cd.botDic2='r'

   
def moveBot2():
    choose=random.randint(0,19)
    if choose==0:
        randomDic2()
    else:
        if cd.botDic2=='u'and playerIsLegal(cd.botX2,cd.botY2-10)==True:
            cd.botY2-=10
        elif cd.botDic2=='d'and playerIsLegal(cd.botX2,cd.botY2+10)==True:
            cd.botY2+=10
        elif cd.botDic2=='l'and playerIsLegal(cd.botX2-10,cd.botY2)==True:
            cd.botX2-=10
        elif cd.botDic2=='r'and playerIsLegal(cd.botX2+10,cd.botY2)==True:
            cd.botX2+=10
        elif  cd.botX2==0 or cd.botX2==560 or cd.botY2==0 or cd.botY2==560:
            randomDic2()

             
        
def drawBot2():
    x=cd.botX2
    y=cd.botY2
    canvas.create_rectangle( x,y,x+40,y+40,fill='purple',width=0)
    if cd.botDic2=='u':
        canvas.create_rectangle( x+15,y-10,x+25,y+20,fill='blue',width=0)
        canvas.create_rectangle( x,y,x+5,y+40,fill='blue',width=0)
        canvas.create_rectangle( x+35,y,x+40,y+40,fill='blue',width=0)
    if cd.botDic2=='d':
        
        canvas.create_rectangle( x+15,y+20,x+25,y+50,fill='blue',width=0)
        canvas.create_rectangle( x,y,x+5,y+40,fill='blue',width=0)
        canvas.create_rectangle( x+35,y,x+40,y+40,fill='blue',width=0)
    if cd.botDic2=='l':
    
        canvas.create_rectangle( x-10,y+15,x+20,y+25,fill='blue',width=0)
        canvas.create_rectangle( x,y,x+40,y+5,fill='blue',width=0)
        canvas.create_rectangle( x,y+35,x+40,y+40,fill='blue',width=0)
    if cd.botDic2=='r':
       
        canvas.create_rectangle( x+20,y+15,x+50,y+25,fill='blue',width=0)
        canvas.create_rectangle( x,y,x+40,y+5,fill='blue',width=0)
        canvas.create_rectangle( x,y+35,x+40,y+40,fill='blue',width=0)

############################################################################################################################################################################################
#bot2 shoots bullets#


def Bnewbullet2():
    cd.BcanShoot2=False
    d=cd.botDic2
    cd.BoneDic2=d
    x=cd.botX2
    y=cd.botY2
    if d=='u':
        cd.BbulletX2=cd.botX2+15
        cd.BbulletY2=cd.botY2-10
    if d=='d':
        cd.BbulletX2=cd.botX2+15  
        cd.BbulletY2=cd.botY2+2*cd.cellSize
    if d=='l':
        cd.BbulletX2=cd.botX2-10
        cd.BbulletY2=cd.botY2+15
    if d=='r':
        cd.BbulletX2=cd.botX2 +2*cd.cellSize 
        cd.BbulletY2=cd.botY2+15
    

def Bprintbullet2():
    canvas.create_rectangle( cd.BbulletX2,cd.BbulletY2,(cd.BbulletX2)+10,(cd.BbulletY2)+10,fill='blue')
                          


def Bfly2():
    d=cd.BoneDic2
    x=cd.BbulletX2
    y=cd.BbulletY2
    if x>275 and x<315 and y>555 and y<595:
        cd.isGameOver=True
        cd.Bshoot2=False
    if bulletIsLegal(cd.BbulletX2,cd.BbulletY2):
        if d=='u':
            cd.BbulletY2-=20
        if d=='d':
            cd.BbulletY2+=20
        if d=='l':
            cd.BbulletX2-=20
        if d=='r':
            cd.BbulletX2+=20
    else:
        cd.Bshoot2=False
        cd.BcanShoot2=True


############################################################################################################################################################################################
#Command#
############################################################################################################################################################################################
#Command#
############################################################################################################################################################################################
#Command#

def keyPressed(event):
    if cd.isGameOver==False and cd.pause==False:
        if event.keysym == 'Up':
            cd.playerDic='u'
            movePlayer(0,-10)
        if event.keysym == 'Down':
            cd.playerDic='d'
            movePlayer(0,10)
        if event.keysym== 'Left':
            cd.playerDic='l'
            movePlayer(-10,0)
        if event.keysym == 'Right':
            cd.playerDic='r'
            movePlayer(10,0)
        if event.char == 's':
            if cd.canShoot==True:
                cd.shoot=True
                newbullet()
    if cd.isGameOver==True:
        if event.char == 'r':
            cd.isGameOver==False
            init()
            
def mousePressed(event):
    if event.x<600:
        if cd.pause==False:
            cd.pause=True
        else:
            cd.pause=False
        
            
def timerFired():
    #make the whole board to change with certain time interval
    if cd.isGameOver==False and cd.pause==False:
        redrawAll()
    delay = 50
    canvas.after(delay, timerFired)
       
############################################################################################################################################################################################
#the core commanding part#       

def redrawAll():
    #redraw background,pieces and text
    canvas.delete(ALL)
    drawboard()
    if cd.BcanShoot==True:
        cd.Bshoot=True
        Bnewbullet()
    if cd.BcanShoot2==True:
        cd.Bshoot2=True
        Bnewbullet2()
    if cd.shoot==True:
        printbullet()
        fly()
    if cd.Bshoot==True:
        Bprintbullet()
        Bfly()
    if cd.Bshoot2==True:
        Bprintbullet2()
        Bfly2()
    drawPlayer()
    drawBot()
    moveBot()
    drawBot2()
    moveBot2()
    drawScoreBoard()
    collide()
    collide2()

############################################################################################################################################################################################
#other commading parts#

def collide():
    if abs(cd.playerX-cd.botX)<40 and abs(cd.playerY-cd.botY)<40:
##        newPlayer()
        newBot()
        cd.score+=500
        cd.kill+=1
##        cd.die+=1
    if abs(cd.bulletX-cd.BbulletX)<=20 and abs(cd.bulletY-cd.BbulletY)<=20:
        cd.shoot=False
        cd.canShoot=True
        cd.bulletX=-100
        cd.bulletY=-100
        Bnewbullet()
    if cd.BbulletX-cd.playerX>=-5 and cd.BbulletX-cd.playerX<=35 and cd.BbulletY-cd.playerY>=-5 and cd.BbulletY-cd.playerY<=35:
        newPlayer()
        cd.Bshoot=False
        cd.BcanShoot=True
        cd.score-=500
        cd.die+=1
    if cd.bulletX-cd.botX>=-5 and cd.bulletX-cd.botX<=35 and cd.bulletY-cd.botY>=-5 and cd.bulletY-cd.botY<=35:
        newBot()
        cd.score+=500
        cd.kill+=1

def collide2():
    if abs(cd.playerX-cd.botX2)<40 and abs(cd.playerY-cd.botY2)<40:
##        newPlayer()
        newBot2()
        cd.score+=500
        cd.kill+=1
##        cd.die+=1
    if abs(cd.bulletX-cd.BbulletX2)<=20 and abs(cd.bulletY-cd.BbulletY2)<=20:
        cd.shoot=False
        cd.canShoot=True
        cd.bulletX=-100
        cd.bulletY=-100
        Bnewbullet2()
    if cd.BbulletX2-cd.playerX>=-5 and cd.BbulletX2-cd.playerX<=35 and cd.BbulletY2-cd.playerY>=-5 and cd.BbulletY2-cd.playerY<=35:
        newPlayer()
        cd.Bshoot2=False
        cd.BcanShoot2=True
        cd.score-=500
        cd.die+=1
    if cd.bulletX-cd.botX2>=-5 and cd.bulletX-cd.botX2<=35 and cd.bulletY-cd.botY2>=-5 and cd.bulletY-cd.botY2<=35:
        newBot2()
        cd.score+=500
        cd.kill+=1


def drawScoreBoard():
    if cd.isGameOver==True:
        canvas.create_oval(285,565, 315, 595, fill='black',width=0)
        canvas.create_text(55,250,text='Game Over ',font='Helvetica 70',fill = 'yellow',anchor = 'nw')
        canvas.create_text(620,480,text='Press "r" to resume',font='Helvetica 15',fill = 'yellow',anchor = 'nw')
    canvas.create_text(620,20,text='TANK',font='Helvetica 43',fill = 'yellow',anchor = 'nw')
    canvas.create_text(618,80,text='Energy Defense',font='Helvetica 17',fill = 'black',anchor = 'nw')
    canvas.create_text(632,105,text='WAR',font='Helvetica 43',fill = 'yellow',anchor = 'nw')
    cd.score+=1
    canvas.create_text(620,240,text='Score: '+str(cd.score),font='Helvetica 17',fill = 'black',anchor = 'nw')
    canvas.create_text(620,280,text='Kill:  '+str(cd.kill),font='Helvetica 17',fill = 'black',anchor = 'nw')
    canvas.create_text(620,320,text='Die: '+str(cd.die),font='Helvetica 17',fill = 'black',anchor = 'nw')
    canvas.create_text(620,380,text='Click the board to pause',font='Helvetica 12',fill = 'black',anchor = 'nw')
    canvas.create_text(620,400,text='Press  "up", "down", ',font='Helvetica 12',fill = 'black',anchor = 'nw')
    canvas.create_text(620,420,text='"left", "right"  to move',font='Helvetica 12',fill = 'black',anchor = 'nw')
    canvas.create_text(620,440,text='Press "s" to shoot ',font='Helvetica 12',fill = 'black',anchor = 'nw')
    
##    canvas.create_text(620,300,text='keys:',font='Helvetica 20',fill = 'black',anchor = 'nw')
##    canvas.create_text(620,350,text='keys:  s  r',font='Helvetica 20',fill = 'black',anchor = 'nw')
##    canvas.create_text(620,400,text='Up  Down',font='Helvetica 20',fill = 'black',anchor = 'nw')
##    canvas.create_text(620,450,text='Left  Right',font='Helvetica 20',fill = 'black',anchor = 'nw')
##    
##      
         
def drawboard():
    canvas.create_rectangle(0,0,canvas.data.canvasWidth,canvas.data.canvasHeight, fill = 'orange')
    board=cd.board
    rows=cd.rows 
    cols=cd.cols 
    for r in xrange(rows):
        for c in xrange(cols):
            drawCell(r, c,board[r][c] )
    if cd.isGameOver==False:
        canvas.create_oval(285,565, 315, 595, fill='yellow',width=0)
    canvas.create_rectangle(600,0,800,600, fill = 'orange')


def drawCell(rows, cols, color):
    margin=canvas.data.margin
    cellSize=cd.cellSize 
    cellMargin =cd.cellMargin 
    if color=='green':
        canvas.create_rectangle( margin + cols*cellSize,margin + rows*cellSize,\
                             margin + (cols+1)*cellSize,margin + (rows+1)*cellSize,\
                             fill=color,width=cellMargin)
    else:
        canvas.create_rectangle( margin + cols*cellSize,margin + rows*cellSize,\
                             margin + (cols+1)*cellSize,margin + (rows+1)*cellSize,\
                             fill=color,width=2)


def init():
    #set up global variables
    #Allocate our board as a 2-dimensional list of names of colors
    cd.isGameOver=False
    cd.pause=False
    cd.score=0
    cd.kill=0
    cd.die=0
    cd.board = []
    cd.shoot=False
    cd.canShoot=True
    cd.Bshoot=False
    cd.BcanShoot=True
    cd.Bshoot2=False
    cd.BcanShoot2=True
    board=cd.board
    rows=cd.rows 
    cols=cd.cols 
    for r in xrange(rows):
        board+=[[]]
        for c in xrange(cols):
            board[r]+=['brown']
    for r in xrange(rows):
         for c in xrange(cols):
            if c==14 or c==15 or c==2 or c==3 or c==26 or c==27 or r==29 or r==28 or r==0 or r==1 or r==14 or r==15:#?
                board[r][c]='green'
            if (c>=10 and c<=19 and r>=24):
                board[r][c]='green'
            if (c>=12 and c<=17 and r>=28):
                board[r][c]='silver'
            if (c>=14 and c<=15 and r>=26):
                board[r][c]='silver'
            if (c>=14 and c<=15 and r>=28):
                board[r][c]='green'
    newPlayer()
    cd.bulletX=-100
    cd.bulletY=-100
    newBot()
    newBot2()
    redrawAll()



def run():
    # create the root and the canvas
    #take the rows and columns as parameters, and use these values to create a properly sized window.
    global canvas
    global cd
    root = Tk()
    rows = 30
    cols = 30
    margin = 0
    cellSize = 20
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    canvas = Canvas(root, width=canvasWidth+200, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)
    # makes window non-resizable
    class Struct: pass
    canvas.data = Struct()
    cd = canvas.data
    # Set up canvas data and call init
    cd.rows = rows
    cd.cols = cols
    cd.margin = margin
    cd.cellSize = cellSize
    cd.cellMargin = 0
    cd.canvasWidth = canvasWidth
    cd.canvasHeight = canvasHeight
    init()
    # set up events
    root.bind("<Key>", keyPressed)
    root.bind("<Button-1>", mousePressed)
    timerFired()
   # and launch the app
    root.mainloop()
    # This call BLOCKS (so your program waits until you close the window!)

run()
    




