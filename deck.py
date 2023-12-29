from card import Card
from random import choice

class Deck():
	def __init__(self, num_of_players, num_of_cards) -> None:
		self.num_of_cards = num_of_cards
		self.num_of_players = num_of_players
		self.kozr = self.determine_kozr()

	@classmethod
	def determine_kozr(cls):
		return choice(cls.suits)

	def generate_deck(self):
		# first step is to determine the kozr/trump suite
		# one data structure to keep all the cards
		if self.num_of_cards == 24:
			return [ Card( suit, numerical_value, Deck.symbol_map[numerical_value], suit == self.kozr ) 
						for suit in Deck.suits
						for numerical_value in range(9, 15)]
		elif self.num_of_cards == 36:
			values = list(range(6, 15))
		elif self.num_of_cards == 52:
			values = list(range(2, 15))
	
	def shuffle_deck():
		pass

	suits = ['hearts', 'diamonds', 'clubs', 'spades']

	symbol_map = {
		2: '2',
		3: '3',
		4: '4',
		5: '5',
		6: '6',
		7: '7',
		8: '8',
		9: '9',
		10: '10',
		11: 'J',  # Jack
		12: 'Q',  # Queen
		13: 'K',  # King
		14: 'A'   # Ace
	}

	def __str__(self) -> str:
		return "\n".join([str(card) for card in self.generate_deck()])