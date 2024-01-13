#functions for cards

from graphics import *


class PlayingCard:

    def __init__(self,rank,suit):

        self.rank=rank

        self.suit=suit



    def getRank(self):

        return self.rank



    def getSuit(self):

        return self.suit



    def values(self):

        if 10<=self.rank<=13:

            self.rank=10

        else:

            self.rank=self.rank



        return self.rank

    def __str__(self):

        value=self.rank

        if self.suit=="c":

            self.suit="Clubs"

        elif self.suit=="d":

            self.suit="Diomands"

        elif self.suit=="h":

            self.suit="Hearts"

        else:

            self.suit="Spades"



        rank=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]



        self.cardValue="{0} of {1}".format(rank[value-1],self.suit)

        return self.cardValue









        

        

        

    

    

