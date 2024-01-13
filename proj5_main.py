#IMPORTS

from BlackJack import *

from graphics import *

from random import *

from ButtonClass import *


def main():
    #create window
    win = GraphWin("Blackjack Game", 600, 600)
    win.setBackground("green4")

    #welcome
    welcome = Text(Point(300,300), "Welcome to Blackjack! \n\
Here, you will practice with fake money, \n\
so you have some practice for your next trip to the casino \n \n\
Click anywhere to continue")
    welcome.draw(win)

    #transition to game
    win.getMouse()
    welcome.undraw()
    

    #Stand and hit
    hitButton = Button(win, Point(200,400), 50, 30, "Hit")
    standButton = Button(win, Point(400,400), 50, 30, "Stand")

    #PLAY
    playButton = Button(win, Point(200,500), 50, 30, "PLAY")
    playButton.deactivate()

    #QUIT
    quitButton = Button(win, Point(400,500), 50, 30, "QUIT")
    quitButton.deactivate()

    
    black_jack=BlackJack(win)

    #START GAME
    black_jack.initialDeal(win,150,150,150,300)
    hitXposition=150
    black_jack.evaluatehands(win,standButton,hitButton)
    
    click=win.getMouse()

    while not quitButton.isClicked(click) or playButton.isClicked(click):

        if playButton.isClicked(click): #play again and close this window
            quitButton.activate()
            win.close()
            main()
            break

        if hitButton.isClicked(click): #hit
            quitButton.activate()
            black_jack.hit(win,hitXposition,150)
            playerScore = black_jack.evaluatehands(win,standButton,hitButton)
            if playerScore == 21: #hardcode fix for getting 21 with two cards
                quitButton.activate()
                black_jack.evaldealerhand(win,standButton,hitButton,200,150)
                playButton.activate()
            
        if standButton.isClicked(click): #stand
            quitButton.activate()
            playButton.activate()
            black_jack.evaldealerhand(win,standButton,hitButton,200,150)

        hitXposition=hitXposition+50
        
        if not quitButton.isClicked(click) or playButton.isClicked(click):
            click=win.getMouse()
            
    win.close()





main()
