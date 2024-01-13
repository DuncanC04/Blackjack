#Button class



from random import *

from graphics import *



class Button:

    def __init__(self,win,center,width,height,label):

        #the parameters are essentially creating a way to provide a fill in

        #for the answer.

        #WIDTH AND HEIGHT

        w,h = width/2.0, height/2.0

        x,y = center.getX(), center.getY()

        #CENTER

        self.xmax, self.xmin = x+w, x-w

        self.ymax, self.ymin = y+h, y-h

        p1=Point(self.xmin, self.ymin)

        p2=Point(self.xmax, self.ymax)

        #R3CTANGLE

        self.rect = Rectangle(p1,p2)

        self.rect.draw(win)

##        self.color=color

        self.label = Text(center, label)

        self.label.setStyle("bold")

        self.label.setFace("courier")

        self.label.setTextColor("beige")

        self.label.draw(win)

        self.activate()



##        return self.color



    def getLabel(self):

        "Returns the label string of this button."

        return self.label.getText()



    def activate (self):

        "Setting the button to 'activate'"

        self.rect.setFill("dark green")

        self.rect.setWidth(1)

        self.active = True



    def deactivate (self):

        self.rect.setFill("grey")

        self.rect.setWidth(1)

        self.active = False



    def isClicked (self, p):

        return (self.active and

                self.xmin <= p.getX() <= self.xmax and

                self.ymin <= p.getY() <= self.ymax)

    



def main():

    #create a graphical window in which to test the Button class

    win = GraphWin("button", 500,500)

    win.setCoords(0,0,10,10)

   

   

    ##create two Button objects, one for "Roll Dice" and the other for "Quit"

    roll = Button(win, Point(3,7),2,2,"Roll Dice")

    Quit = Button(win, Point(7,3),2,2,"Quit")

    ##activate the Roll button

    roll.activate()

    Quit.deactivate()





    ##deactivate the "Quit" button

    Quit.deactivate()



    pt = win.getMouse()

 

    ##loop until the "Quit" button is clicked...

    while not (Quit.isClicked(pt)):

        ##if the roll button is clicked

        if roll.isClicked(pt):

            ##activate the quit button

            Quit.activate()

        ##take the next mouse click

        pt = win.getMouse()



    win.close()  

if __name__=="__main__":

    main()

