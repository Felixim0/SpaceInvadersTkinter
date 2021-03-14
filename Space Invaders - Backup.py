from tkinter import *
from time import sleep
from random import randint
window =Tk()
window.configure(background='black')
window.title("Space Invaders")

w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.overrideredirect(1)
window.geometry("%dx%d+0+0" % (w, h))

canvasHeight = round(h, -1)
canvasWidth = round(w, -1)

y = canvasHeight
playerCOy = y-30
playerCOx = canvasWidth/2

canvas = Canvas(bg="black",height=canvasHeight,width=canvasWidth,highlightthickness=0)
canvas.grid(column=1,row=1,columnspan=2)

playerImagePath = (r"./environment/playerModels/playerModel1.gif")
playerImage = PhotoImage(file=playerImagePath)
playerImageItem = canvas.create_image(playerCOx, playerCOy, image=playerImage)
playerImage.image = playerImage

bulletImagePath = (r"./environment/bullet/bullet.gif")
bulletImage = PhotoImage(file=bulletImagePath)
bulletImageItem = canvas.create_image(playerCOx, playerCOy, image=bulletImage)
bulletImage.image = bulletImage

bulletY = playerCOy-(playerImage.height()/2)+bulletImage.height()
bulletX = playerCOx
bulletShot = False
mothershipVisable = False
mothershipHit = False
allAlienCO = []
highestAlien = []

alienImagePathA1 = (r"./environment/aliens/A1.gif")
alienImageA1 = PhotoImage(file=alienImagePathA1)
alienImagePathA2 = (r"./environment/aliens/A2.gif")
alienImageA2 = PhotoImage(file=alienImagePathA2)

alienBulletPath = (r"./environment/aliens/alien1.gif")
alienBulletImage = PhotoImage(file=alienBulletPath)
alienBulletImageItem = canvas.create_image(-200,-200,image=alienBulletImage)

alienImagePathB1 = (r"./environment/aliens/B1.gif")
alienImageB1 = PhotoImage(file=alienImagePathB1)
alienImagePathB2 = (r"./environment/aliens/B2.gif")
alienImageB2 = PhotoImage(file=alienImagePathB2)

alienImagePathC1 = (r"./environment/aliens/C1.gif")
alienImageC1 = PhotoImage(file=alienImagePathC1)
alienImagePathC2 = (r"./environment/aliens/C2.gif")
alienImageC2 = PhotoImage(file=alienImagePathC2)

mothershipImagePath = (r"./environment/aliens/mothership.gif")
mothershipImage = PhotoImage(file=mothershipImagePath)

#Generic image for alien (size refference only)
genericAlien = (r"./environment/aliens/alien1.gif")
alienImage = PhotoImage(file=genericAlien)

alienImageItem = []
motherCOx = 0
direction = "Right"
runOnce = True
canvasFit = round((canvasWidth/alienImage.width())+(alienImage.width()*1.5),-1)
alienSpeed = 10 #300 is good
gameOver = False
bulletFalling = False
alienBulletX = 0
alienBulletY = 0
def drawAliens():
    global allAlienCO,alienImageItem,runOnce,highestAlien,canvasFit,direction,alienImageA1,alienImageA2,alienImageB1,alienImageB2,alienImageC1,alienImageC2,alienSpeed
    global gameOver
    
    maxAlienXCO = max(highestAlien)*canvasFit
    
    if runOnce == True:
        for i in range(0,len(allAlienCO)-1):
            if allAlienCO[i][0] == "A1":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageA1)
                alienImageItem.append(alienID)
            if allAlienCO[i][0] == "A2":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageA2)
                alienImageItem.append(alienID)
            if allAlienCO[i][0] == "B1":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageB1)
                alienImageItem.append(alienID)
            if allAlienCO[i][0] == "B1":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageB2)
                alienImageItem.append(alienID)            
            if allAlienCO[i][0] == "C1":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageC1)
                alienImageItem.append(alienID)
            if allAlienCO[i][0] == "C2":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageC2)
                alienImageItem.append(alienID)

                
    else:
        if (allAlienCO[int((max(highestAlien))-1)][1]+alienImage.width() > canvasWidth) and (direction == "Right"):
            a = 0
            b = 20
            direction = "Left"
        elif (allAlienCO[int((min(highestAlien))-1)][1]-alienImage.width() < 0) and (direction == "Left"):
            a = 0
            b = +20
            direction = "Right"
        elif direction == "Left":
            a = -20
            b = 0
        elif direction == "Right":
            a = 20
            b = 0
        for i in range(0,len(allAlienCO)-1):
            allAlienCO[i][1] = (allAlienCO[i][1] + a) # add a to x co of all aliens
            allAlienCO[i][2] = (allAlienCO[i][2] + b) # add b to y co of all aliens
            # Next:  Changes picture type to make it appear that the aliens are moving their legs

            if allAlienCO[i][0] == "A1":
                allAlienCO[i][0] = "A2"

            elif allAlienCO[i][0] == "B1":
                allAlienCO[i][0] = "B2"

            elif allAlienCO[i][0] == "C1":
                allAlienCO[i][0] = "C2"
                
            elif allAlienCO[i][0] == "A2":
                allAlienCO[i][0] = "A1"

            elif allAlienCO[i][0] == "B2":
                allAlienCO[i][0] = "B1"

            elif allAlienCO[i][0] == "C2":
                allAlienCO[i][0] = "C1"
        
        for i in range(0,len(alienImageItem)):
            canvas.delete(alienImageItem[i])
            
        alienImageItem = []
        for i in range(0,len(allAlienCO)-1):           
            if allAlienCO[i][0] == "A1":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageA1)
                alienImageItem.append(alienID)
            if allAlienCO[i][0] == "A2":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageA2)
                alienImageItem.append(alienID)
            if allAlienCO[i][0] == "B1":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageB1)
                alienImageItem.append(alienID)
            if allAlienCO[i][0] == "B2":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageB2)
                alienImageItem.append(alienID)            
            if allAlienCO[i][0] == "C1":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageC1)
                alienImageItem.append(alienID)
            if allAlienCO[i][0] == "C2":  
                alienID = canvas.create_image(allAlienCO[i][1], allAlienCO[i][2], image=alienImageC2)
                alienImageItem.append(alienID)
                
    if gameOver == False:   
        window.after(alienSpeed, drawAliens)            

def createAliens():
    global allAlienCO,alienImage,canvasFit,highestAlien
    #How many aliens fit on screen? ALways 20 aliens

    
    print(canvasFit)
    alienType = "Normal"
    bar = canvasHeight/10
    iTemp = 0
    typeNo = 0
    listOfAlienTypes = ["A1","A1","B1","C1","C1","C1","C1"]
    for i in range(1,50): # total 30 aliens
        iTemp = iTemp+1
        tempArray = [str(listOfAlienTypes[typeNo]),iTemp*canvasFit,bar]
        highestAlien.append(iTemp)
        allAlienCO.append(tempArray[:])
        if (tempArray[1]+canvasFit)+(4*alienImage.width()) > canvasWidth:
            bar = bar+(alienImage.height()*2)
            iTemp = 0
            typeNo = typeNo + 1
            
def deleteAlien(alienID):
    global allAlienCO
    allAlienCO[alienID][0] = "Hidden"

def isBulletToutchingMothership(bulletY,bulletX):
    global mothershipImage,motherCOx,motherCOy,mothershipHit
    if ((bulletX - ((1/2)*(mothershipImage.width()))) <= motherCOx <= (bulletX + ((1/2)*(mothershipImage.width())))) and ((bulletY - ((1/2)*(mothershipImage.height()))) <=mothershipImage.height()  <= (bulletY + ((1/2)*(mothershipImage.height())))):
        mothershipHit = True
        return True
    return False

def isBulletToutchingAlien(bulletY,bulletX):
    global allAlienCO,alienImage,alienSpeed
    for i in range (0,len(allAlienCO)-1):
        if ((bulletX - ((1/2)*(alienImage.width()))) <= allAlienCO[i][1] <= (bulletX + ((1/2)*(alienImage.width())))) and ((bulletY - ((1/2)*(alienImage.height()))) <= allAlienCO[i][2] <= (bulletY + ((1/2)*(alienImage.height())))):
            if allAlienCO[i][0] != "Hidden":
                deleteAlien(i)
                if alienSpeed > 100 :
                    alienSpeed = alienSpeed - 2
                return True
    
    return False

def drawPlayer():
    global playerCOy,playerCOx,playerImageItem
    canvas.coords(playerImageItem,playerCOx,playerCOy)

def drawBullet():
    global bulletImageItem,bulletX,bulletY
    canvas.coords(bulletImageItem,bulletX,bulletY)

def stopAliens(w):
    global alienSpeed
    alienSpeed = 500

def drawMothership():
    global mothershipImage,mothershipVisable,mothership,motherCOx,directionOfMother,mothershipHit
    if mothershipVisable == True:
        if directionOfMother == "Left":
            a = 10
        elif directionOfMother == "Right":
            a = -10
        
        motherCOx = motherCOx + a

        if (motherCOx > canvasWidth) or (motherCOx < 0) or (mothershipHit == True):
            canvas.delete(mothershipItem)
            mothershipVisable = False
            mothershipHit = False
            
        canvas.coords(mothershipItem,motherCOx,mothershipImage.height())    

def mothership():
    global mothershipImage,mothershipVisable,mothershipItem,motherCOx,directionOfMother
    if mothershipVisable == False:
        #generate chance of appearing
        chance = randint(0,200)
        if chance == 45:
            side = randint(0,1)
            if side == 0: # (left)
                directionOfMother = "Right"
                motherCOx = canvasWidth - mothershipImage.width()/2
            elif side  == 1: # Right
                directionOfMother = "Left"
                motherCOx = mothershipImage.width()/2
                
            mothershipVisable = True
            mothershipItem = canvas.create_image(motherCOx, mothershipImage.height(), image=mothershipImage)            

def havePlayerWon():
    global allAlienCO,gameOver
    temp = []
    for i in range (0,len(allAlienCO)):
        if allAlienCO[i][0] == "Hidden":
            temp.append("Entry")

    if len(temp) == len(allAlienCO):
        gameOver = True
        return True
    return False

def deleteAllAliens(e):
    global allAlienCO
    for i in range (0,len(allAlienCO)):
        allAlienCO[i][0] = "Hidden"

def showFinalScreen():
    canvas.create_text(canvasWidth/2,canvasHeight/2,fill="white",font="Times 100 italic bold",text="Game Over")

def haveAliensWon():
    global allAlienCO,playerImage,hiddenAliens,gameOver
    hiddenAliens=[]
    for i in range(0,len(allAlienCO)-1):
        if allAlienCO[i][0] != "Hidden":
            hiddenAliens.append(allAlienCO[i][2])

    for i in range (0,len(hiddenAliens)-1):
        if hiddenAliens[i] > (canvasHeight - playerImage.height()):
            gameOver = True
            return True
                        
    return False            

def alienFire():
    global allAlienCO,bulletFalling,alienBulletImageItem
    #randomChance = randint(0,300)
    randomChance = 34
    if randomChance == 34:
        a = 8

def main():
    global bulletShot,bulletY,bulletX,playerCOy,playerCOx,playerImageItem,runOnce,mothershipVisable,gameOver
    createAliens()
    drawAliens()
    runOnce = False
    
    while gameOver == False:
        if bulletShot == True:
            if (bulletY < 10) or (isBulletToutchingAlien(bulletY,bulletX) == True) or (isBulletToutchingMothership(bulletY,bulletX) == True):
                bulletY = playerCOy-(playerImage.height()/2)+bulletImage.height()
                bulletX = playerCOx
                bulletShot = False
            else:
                bulletY = bulletY - 20
        elif bulletShot==False:
            bulletY = playerCOy-(playerImage.height()/2)+bulletImage.height()
            bulletX = playerCOx
            
        if (havePlayerWon() == False):
            if (haveAliensWon() == False):
                mothership()
                drawMothership()
                drawPlayer()
                drawBullet()
                alienFire()
                window.update()
                sleep(0.03)

    showFinalScreen()
        

def moveRight(e):
    global playerCOx,playerImageItem
    if playerCOx < canvasWidth-playerImage.width():
        playerCOx = playerCOx + 20 

def moveLeft(e):
    global playerCOx,playerImageItem
    if (playerCOx > 0+playerImage.width()):
        playerCOx = playerCOx - 20

def bullet(e):
    global bulletShot, bulletX
    bulletShot = True
    
window.bind("<Right>",moveRight)
window.bind("<Left>",moveLeft)
window.bind("<space>",bullet)
window.bind("c",deleteAllAliens)
window.bind("d",stopAliens)
main()

drawPlayer()

window.mainloop()
