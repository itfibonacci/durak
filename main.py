import argparse

def main():
	# non class based approach
	# user running program: python main.py --cards 36 --players 4
	# make sure to check that number of cards >= num_of_players * 6

	class CardsAction(argparse.Action):
		def __call__(self, parser, namespace, values, option_string=None):
			num_of_players = getattr(namespace, 'players')
			if values < num_of_players * 6:
				parser.error("Number of cards must be greater or equal than num_of_players * 6")
			else:
				setattr(namespace, self.dest, values)
	
	# user can choose game of 2, 3, 4, 5, 6 players
	parser = argparse.ArgumentParser("durak game", description="This is a game. Use the --num_of_players option to specify the number of players and the --num_of_cards option to specify the number of cards. The number of cards must be greater than or equal to six times the number of players.")
	
	parser.add_argument('-p', '--players', required=True, type=int, choices=[ 2, 3, 4, 5, 6 ], help="Number of players in the game, values can be: 2, 3, 4, 5, 6 players")
	
	parser.add_argument('-c', '--cards', required=True, type=int, choices=[ 24, 36, 52 ], action=CardsAction, help="Number of cards in the game, Values can be: 24, 36, 52 ")
	args = parser.parse_args()

	# one data structure to keep all the cards
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

	if args.cards == 24:
		values = list(range(9, 15))
	elif args.cards == 36:
		values = list(range(6, 15))
	elif args.cards == 52:
		values = list(range(2, 15))

	# one dictionary to keep the cards remaining to be distributed
	# one list for bita
	# classes/types: card, deck
	
if __name__ == "__main__":
	main()