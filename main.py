import itertools
import argparse
import logging
from os import makedirs, path
from datetime import datetime
from random import choice

from deck import Deck
from card import Card
from player import Player

def get_log_filename():
	dir_name = "logs"
	# Check if the directory exists
	if not path.exists(dir_name):
		# If the directory doesn't exist, create it
		makedirs(dir_name)

	# Get current date and time
	now = datetime.now()

	# Format as a string
	date_time_str = now.strftime("%Y%m%d_%H%M%S")

	# Attach to a filename
	filename = f"{dir_name}/durak_{date_time_str}.txt"

	return filename

def main():
	# non class based approach
	# user running program: python main.py --cards 36 --players 4
	# make sure to check that number of cards >= num_of_players * 6
	logging.basicConfig(filename=get_log_filename(), encoding='utf-8', format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

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

	# one dictionary to keep the cards remaining to be distributed
	# one list for bita
	# classes/types: card, deck

	deck = Deck(args.players, args.cards)
	logging.info(f'Created a deck for {args.players} players and {args.cards} cards.')

	# card1 = Card('hearts', 6, '6', True)
	# card2 = Card('hearts', 13, 'K',True)
	# print(card2)
	players = []
	distribution = deck.distribute_cards()
	logging.info(f'Created a generator for distributing the cards.')

	for i in range(args.players):
		player = Player(i + 1)
		logging.info(f'Created a player with name {player.name}, position: {player.position}')
		player.hand = next(distribution)
		logging.info(f'Distributed the hand to {player.name}')
		players.append(player)
	
	# returns all the remaining cards that havent been distributed to the prikup
	deck.populate_prikup(list(itertools.chain.from_iterable(distribution)))

	if deck.prikup:
		logging.info(f'Populated the Prikup.')
		deck.determine_kozr_card()
	else:
		logging.info(f'No Prikup. Kozr will be determined from the last player\'s hand')
		deck.determine_kozr_card(players[-1].hand)
	
	deck.update_kozr()

	# Log each player's hand to the log file
	for player in players:
		logging.info(f'{str(player)}')
	
if __name__ == "__main__":
	main()