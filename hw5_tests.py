###############################
##### Name: Sushmitha Rao #####
##### Uniqname: sushrao   #####
###############################

import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c3 = hw5_cards.Card(0, 12)

        
        self.assertEqual(c3.rank_name, "Queen")
        return c3.rank_name, "Queen"
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        #create card instance with suit = 1, rank = 2
        c4 = hw5_cards.Card(1, 2)
        self.assertEqual(c4.suit_name, "Clubs")
        return c4.suit_name, "Clubs"
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        #create card instance with suit = 3, rank = 13
        c5 = hw5_cards.Card(3,13)
        self.assertEqual(str(c5),"King of Spades")

        return str(c5),"King of Spades"
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        #creating Deck instance
        c6 = hw5_cards.Deck()
        #checking if number of cards in Deck.cards is 52
        self.assertEqual(len(c6.cards),52)

        return len(c6.cards),52

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        #creating Deck instance
        c6 = hw5_cards.Deck()
        #checking type of the deal_card function's return is a Card class instand
        self.assertIsInstance(c6.deal_card(),type(hw5_cards.Card()))


        return c6.deal_card(),type(hw5_cards.Card())
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        #creating Deck instance
        c7 = hw5_cards.Deck()
        #dealing out one card
        c7.deal_card()
        #creating Deck instance
        c8 = hw5_cards.Deck()
        #comparing two instances one with card dealt(c7) and one without (c8)
        self.assertEqual(len(c8.cards)-1,len(c7.cards))

        return len(c8.cards)-1,len(c7.cards)

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        #creating Deck instance
        c9 = hw5_cards.Deck()
        #dealing card and capturing instance
        card = c9.deal_card()
        #checking length of deck after dealing card
        deal_len = len(c9.cards)
        #replacing card back into deck
        c9.replace_card(card)
        #checking length of deck with card replaced
        replace_len = len(c9.cards)
        #comparing length of card before and after replacing
        self.assertEqual(replace_len,deal_len+1)

        return replace_len,deal_len+1
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        #creating Deck instance
        c10 = hw5_cards.Deck()
        #deal one card from the card and store the card properties
        card = c10.deal_card()
        #deal another card from the card and store the card properties
        #card2 = c10.deal_card()
        #check the length of deck with 2 cards dealt
        deal_len = len(c10.cards)
        #replace a card into the deck
        c10.replace_card(card)
        #try to replace same card into deck
        c10.replace_card(card)
        #check length of deck after two replace attempts
        replace_len = len(c10.cards)
        #compare the two lengths to make sure that
        #it ignores the attempt if the same card is tried
        self.assertEqual(replace_len,deal_len+1)
        
        return replace_len,deal_len+1



if __name__=="__main__":
    unittest.main()