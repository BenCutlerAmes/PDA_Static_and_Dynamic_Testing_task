import unittest

from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('clubs',1)
        self.card2 = Card('hearts',7)

        self.cards = [self.card1,self.card2]

    def test_check_for_ace_true(self):
        result = CardGame.check_for_ace(self,self.card1)
        self.assertEqual(True,result)

    def test_check_for_ace_false(self):
        result = CardGame.check_for_ace(self,self.card2)
        self.assertEqual(False,result)

    def test_highest_card_lowest_first(self):
        result = CardGame.highest_card(self,self.card1,self.card2)
        self.assertEqual(self.card2,result)

    def test_highest_card_highest_first(self):
        result = CardGame.highest_card(self,self.card2,self.card1)
        self.assertEqual(self.card2,result)

    def test_card_total(self):
        result = CardGame.cards_total(self,self.cards)
        self.assertEqual("You have a total of 8",result)
