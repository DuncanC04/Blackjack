#This program demonstrates how to include image files into a graphical window.

from graphics import *

def main():
    win = GraphWin("Image Practice", 600, 600)

    #create the image object using an image file (places the image
    #with filename s1.gif at point (300,300) of the graphical window)
    im = Image(Point(300,300),"playingcards/s1.gif") #ace of spades in this case
    im.draw(win)
    #NOTE: the above code assumes this program is 
    #*in the same folder as* the playingcards folder (i.e.
    #"next to" the playingcards folder).
    #This keeps the image files organized
    #separate from your code.
   
    win.getMouse()
    #after user click, display another card
    #this second card demonstrates how to construct the image file name
    #using a string variable that holds the suit
    #and an integer variable that holds the rank of the card
    suit = "h"  #indicates hearts
    rank = 12   #indicates queen
    #creates an image object from the file h12.gif by concatenating the above variables
    #note that rank must be string-ified before concatenating it with other strings!!
    im = Image(Point(350, 250), "playingcards/" + suit + str(rank) + ".gif")
    im.draw(win)
    
    #one more click closes the window
    win.getMouse()
    win.close()
    
main()
