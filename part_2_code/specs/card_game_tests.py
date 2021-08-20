import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("diamond", 8)
        self.card2 = Card("heart", 5)
        self.card3 = Card("jack", 11)
        self.card4 = Card("spade", 1)
        self.card_game = CardGame()
        self.cards = [self.card1, self.card2, self.card3, self.card4]

    def test_check_for_ace_true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card4))
    
    def test_check_for_ace_false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card1))

    def test_card__3_is_highest(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card3, self.card2))
    
    def test_card_2_is_not_highest(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card2, self.card3))
    
    def test_cards_total(self):
        self.assertEqual("You have a total of 25", self.card_game.cards_total(self.cards))
    

    

    