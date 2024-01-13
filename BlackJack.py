#BlackJack Class - game functions



from graphics import *

from PlayingCardClass import *

from DeckClass import *

from ButtonClass import *



class BlackJack:

    def __init__(self,win,dealerH=[],playerH=[]):

        self.dealerH=[]


        self.playerH=[]

        

        self.playerTxt=Text(Point(50,300),"")
        
        self.playerTxt.setSize(15)
        
        self.playerTxt.draw(win)

        self.dealerTxt=Text(Point(50,150),"")

        self.dealerTxt.setSize(15)

        self.dealerTxt.draw(win)

        

        self.output=Text(Point(250,220),"")

        self.output.draw(win)



        

        self.stack=Deck()

        

        self.stack.shuffles()





    def initialDeal (self,win,xposD,yposD,xposP,yposP):

        self.d1=self.stack.dealCard()

        self.d1hand=self.dealerH.append(self.d1)

        self.dealImage=Image(Point(xposD,yposD),"playingcards/"+self.d1.getSuit()+str(self.d1.getRank())+".gif")

        self.dealImage.draw(win)

        

        self.faceD=Image(Point(xposD+50,yposD),"playingcards/b2fv.gif")

        self.faceD.draw(win)

        

        

        self.p1=self.stack.dealCard()

        self.playerhand=self.playerH.append(self.p1)

        self.playerImage=Image(Point(xposP,yposP),"playingcards/"+self.p1.getSuit()+str(self.p1.getRank())+".gif")

        self.playerImage.draw(win)

        #Getsuit:Look at the actual card: We dont know the rank or suit

        #Suit=Face card: CDHS(clubs,diomonds,hearts,spades)

        #Rank=Value of the card (1-13 Values)

        #Deal card:Grabbing from the stack of cards



        self.p2=self.stack.dealCard()

        self.player2=self.playerH.append(self.p2)

        self.player2Image=Image(Point(xposP+50,yposP),"playingcards/"+self.p2.getSuit()+str(self.p2.getRank())+".gif")

        self.player2Image.draw(win)



    #Giving an extra card because "hit" adds a new card to the player

    def hit (self,win,xposP,yposP):

        #Picking up the card

        self.p3=self.stack.dealCard()

        self.player3=self.playerH.append(self.p3)

        self.player3Image=Image(Point(xposP+100,yposP+150),"playingcards/"+self.p3.getSuit()+str(self.p3.getRank())+".gif")

        self.player3Image.draw(win)



    def evaluatehands(self,win,button1,button2):

        self.button1=button1

        self.button2=button2



        #Player score

        self.playerScore=0

        #player rank

        self.playerRank=[]

        for self.playerc in self.playerH:

            self.playerRank.append(self.playerc.getRank())

            self.playerScore=self.playerScore+self.playerc.getRank()

        self.playerTxt.setText("Total: " + str(self.playerScore))


        
        for self.ranklst in self.playerRank:


            if self.ranklst==11:

                self.playerScore=self.playerScore-1

                self.playerTxt.setText("Total: " + str(self.playerScore))

            if self.ranklst==12:

                self.playerScore=self.playerScore-2

                self.playerTxt.setText("Total: " + str(self.playerScore))

            if self.ranklst==13:

                self.playerScore=self.playerScore-3

                self.playerTxt.setText("Total: " + str(self.playerScore))

            if self.ranklst==1:

                if self.playerScore<=10:

                    self.playerScore += 10
    

                if self.playerScore>10:

                    self.playerScore=self.playerScore

                    self.playerTxt.setText("Total: " + str(self.playerScore))

                
        if (self.playerRank[0] == 1 and self.playerRank[1] >= 10) or (self.playerRank[0] >= 10 and self.playerRank[1] == 1):
            
            self.playerScore=21

            self.playerTxt.setText("Total: " + str(self.playerScore))
            

        self.dealerScore=0

        self.dealerRank=[]

        for self.dealerc in self.dealerH:

            self.dealerRank.append(self.dealerc.getRank())

            self.dealerScore=self.dealerScore+self.dealerc.getRank()

        self.dealerTxt.setText("Total: " + str(self.dealerScore))



        for self.rankd in self.dealerRank:

             

            if self.rankd==1:

                if self.dealerScore<=10:

                    self.dealerScore += 10

                

                if self.dealerScore>10:

                    self.dealerScore=self.dealerScore

                    self.dealerTxt.setText("Total: " + str(self.dealerScore))

        

            if self.rankd==11:

                self.dealerScore=self.dealerScore-1

                self.dealerTxt.setText("Total: " + str(self.dealerScore))

            if self.rankd==12:

                self.dealerScore=self.dealerScore-2

                self.dealerTxt.setText("Total: " + str(self.dealerScore))

            if self.rankd==13:

                self.dealerScore=self.dealerScore-3

                self.dealerTxt.setText("Total: " + str(self.dealerScore))



        if self.playerScore>21:

            self.output.setText("Dealer Wins!")

            self.button1.deactivate()

            self.button2.deactivate()





        if self.playerScore==21:

            self.output.setText("Player Wins!")

            self.button1.deactivate()

            self.button2.deactivate()

        return self.playerScore



    def evaldealerhand(self,win,button1,button2,xposD,yposD):

        

        self.button1=button1

        self.button2=button2

        



        self.dealer2=self.stack.dealCard()

        self.dealer2hand=self.dealerH.append(self.dealer2)

        self.dealerImage=Image(Point(xposD,yposD),"playingcards/"+self.dealer2.getSuit()+str(self.dealer2.getRank())+".gif")

        self.dealerImage.draw(win)

        self.dealerScore=0

        self.dealerRank=[]

        for self.dealerCard in self.dealerH:

            self.dealerRank.append(self.dealerCard.getRank())

            self.dealerScore += self.dealerCard.getRank()

        self.dealerTxt.setText("Total: " + str(self.dealerScore))



        for self.dealerR in self.dealerRank:

             

            if self.dealerR==1:

                if self.dealerScore<=10:

                    self.dealerScore += 11

                    self.dealerTxt.setText("Total: " + str(self.dealerScore))

                    

                if self.dealerScore>10:

                    self.dealerTxt.setText("Total: " + str(self.dealerScore))

        

            if self.dealerR==11:

                self.dealerScore=self.dealerScore-1

                self.dealerTxt.setText("Total: " + str(self.dealerScore))

            if self.dealerR==12:

                self.dealerScore=self.dealerScore-2

                self.dealerTxt.setText("Total: " + str(self.dealerScore))

            if self.dealerR==13:

                self.dealerScore=self.dealerScore-3

                self.dealerTxt.setText("Total: " + str(self.dealerScore))

        xposVariable=200

    

        while not self.dealerScore>=17:

            xposVariable+=50

            self.dealerX=self.stack.dealCard()

            self.dealerXhand=self.dealerH.append(self.dealerX)

            self.dealerXImage=Image(Point(xposVariable,yposD),"playingcards/"+self.dealerX.getSuit()+str(self.dealerX.getRank())+".gif")

            self.dealerXImage.draw(win)

   

            self.dealerRank=[]

            self.dealerScore=0



            for self.dealerXCard in self.dealerH:

                self.dealerScore += self.dealerXCard.getRank()

                self.dealerRank.append(self.dealerXCard.getRank())

            self.dealerTxt.setText("Total: " + str(self.dealerScore))

                

            for self.dealerXR in self.dealerRank:

                

                if self.dealerXR==1:

                    if self.dealerScore<=10:

                        self.dealerScore += 10

                        self.dealerTxt.setText("Total: " + str(self.dealerScore))

                        

                    if self.dealerScore>10:

                        self.dealerScore=self.dealerScore+0

                        self.dealerTxt.setText("Total: " + str(self.dealerScore))

            

                if self.dealerXR==11:

                    self.dealerScore=self.dealerScore-1

                    self.dealerTxt.setText("Total: " + str(self.dealerScore))

                if self.dealerXR==12:

                    self.dealerScore=self.dealerScore-2

                    self.dealerTxt.setText("Total: " + str(self.dealerScore))

                if self.dealerXR==13:

                    self.dealerScore=self.dealerScore-3

                    self.dealerTxt.setText("Total: " + str(self.dealerScore))



        if self.dealerScore>21:

            self.output.setText("Dealer Busted!")

    

        elif self.dealerScore==21 or self.dealerScore>self.playerScore:

            self.output.setText("Dealer Wins!")

            

        elif self.dealerScore==self.playerScore:

            self.output.setText("Push!")

            

        else:

            self.output.setText("Player Wins!")



        self.button1.deactivate()

        self.button2.deactivate()

        
