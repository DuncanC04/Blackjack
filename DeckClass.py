#Deck Class - creates deck and deals card


from graphics import *

from random import *

from PlayingCardClass import *

class Deck:

    def __init__(self):

        rank=['c','d','h',"s"]

    

        cardSpecs=[]

        for i in range(52):

            x=i%13+1

            y=rank[i%4]

            cardSpecs.append((x,y))

        self.cards = []

        for (x,y) in cardSpecs:

            self.cards.append(PlayingCard(x,y))



    def shuffle(self):

        newList=[]

        for i in range (len(self.cards)):

            x=int(random()*len(self.cards))-1

            newList.append(self.cards[x])



        return newList

    

    def shuffles(self):

        self.cards=self.shuffle()



    def dealCard(self):

        return self.cards.pop(0)



    def cardsLeft(self):

        return len(self.cards)





def main():

        deck=Deck()

        deck.shuffles()

        for i in range (52):

            print(deck.dealCard())



if __name__=="__main__":

    

    main()

     







