import logging
from random import choice
# each player has position in the game (1, 2, 3, 4, 5, 6
# each player has the cards in their hand

class Player():
	def __init__(self, position) -> None:
		self.name = choice(self.first_names)		
		self.position = position
		self.hand = []
		
	def __str__(self) -> str:
		return f"Name: {self.name}, Position: {self.position}, Hand: {[str(card) for card in self.hand]}"

	first_names = ['John', 'Andy', 'Joe', 'Mike', 'Amy', 'Rose', 'Grace']