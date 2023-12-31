import logging

from card import Card
from random import choice, shuffle

class Deck():
	def __init__(self, num_of_players, num_of_cards) -> None:
		self.num_of_cards = num_of_cards
		self.num_of_players = num_of_players
		self.kozr = False
		self.generated_deck = self.generate_deck()
		self.shuffled_deck = self.shuffle_deck()
		self.prikup = []
	
	# the below method is used to run after a kozr has been determined and will update the card's
	# kozr attribute
	def update_kozr(self):
		for card in self.generated_deck:
			if card.suit == self.kozr.suit:
				card.kozr = True
		logging.info(f'Updated each card\'s kozr value.')

	def determine_kozr_card(self, last_players_hand=None):
		if last_players_hand:
			self.kozr = choice(last_players_hand)
			logging.info(f'Kozr has been established from the last player\'s hand. {self.kozr.suit}')
		else:
			self.kozr = choice(self.prikup)
			logging.info(f'Chose the kozr from prikup. {self.kozr}')

	def generate_deck(self):
		# first step is to determine the kozr/trump suite
		# one data structure to keep all the cards
		if self.num_of_cards == 24:
			return [ Card( suit, numerical_value, Deck.symbol_map[numerical_value] ) 
						for suit in Deck.suits
						for numerical_value in range(9, 15)]
		elif self.num_of_cards == 36:
			return [ Card( suit, numerical_value, Deck.symbol_map[numerical_value] ) 
						for suit in Deck.suits
						for numerical_value in range(6, 15)]
		elif self.num_of_cards == 52:
			return [ Card( suit, numerical_value, Deck.symbol_map[numerical_value] ) 
						for suit in Deck.suits
						for numerical_value in range(2, 15)]
	
	def shuffle_deck(self):
		shuffled_deck = self.generated_deck.copy()
		shuffle(shuffled_deck)
		return shuffled_deck

	# distribute deck to the players. so that each player has 6 cards
	# player class i think should be created
	def distribute_cards(self):
		for i in range(0, len(self.shuffled_deck), 6):
			yield self.shuffled_deck[i:i+6]
	
	# this will be called once all the cards from the deck have been distributed
	# it will add the remaining cards to the prikup(talon)
	def populate_prikup(self, prikup):
		self.prikup = prikup
	# method for drawing from the prikup

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
		return "\n".join([str(card) for card in self.shuffled_deck])