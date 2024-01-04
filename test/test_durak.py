import logging
import unittest
from sys import stdout

from player import Player
from main import get_log_filename
from deck import Deck

class TestDurakGame(unittest.TestCase):
	def setUp(self):
		"""This method is run before each test. You can use it to set up any state that's shared across 	tests."""
		# Create a logger
		self.logger = logging.getLogger()
		self.logger.propagate = False
		self.logger.setLevel(logging.DEBUG)  # You can set this to be any level

		# Create a handler for writing to the log file
		self.file_handler = logging.FileHandler(get_log_filename("test/logs/"))
		self.file_handler.setLevel(logging.DEBUG)  # You can set this to be any level

		# Create a handler for writing to the console
		self.console_handler = logging.StreamHandler(stdout)
		self.console_handler.setLevel(logging.DEBUG)  # You can set this to be any level

		# Create a formatter
		self.formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

		# Add the formatter to the handlers
		self.file_handler.setFormatter(self.formatter)
		self.console_handler.setFormatter(self.formatter)

		# Add the handlers to the logger
		if not self.logger.hasHandlers():
			self.logger.addHandler(self.console_handler)
			self.logger.addHandler(self.file_handler)
	
	def tearDown(self) -> None:
		self.logger.removeHandler(self.console_handler)
		self.logger.removeHandler(self.file_handler)
		self.console_handler.close()
		self.file_handler.close()

	def test_deal_cards(self):
		"""Test the player class."""
		self.player = Player(1)
		self.assertEqual(len(self.player.hand), 0)
		logging.info(f'Assert that player\'s hand is empty. {len(self.player.hand)}')
		self.assertEqual(self.player.position, 1)
		logging.info(f'Assert that player\'s position is 1: {self.player.position}')
		self.assertIn(self.player.name, self.player.first_names)
		logging.info(f'Assert that player\'s name ({self.player.name}) is in: {self.player.first_names}')

	def test_play_round_4_24(self):
		"""Test a game with 4 players and 24 cards.\n"""
		deck = Deck(4, 24)
		logging.info(f'Assert that the deck has generated the correct number of cards: {len(deck.generated_deck)}')
		self.assertEqual(len(deck.generated_deck), 24)
		logging.info(f'Assert that the prikup is empty.')
		self.assertEqual(len(deck.prikup), 0)
		logging.info(f'Assert that the prikup is of length 0.')
		self.assertIsNone(deck.kozr)
		logging.info(f'Assert that a kozer has not been determined yet.')

if __name__ == "__main__":
	unittest.main(verbosity=2)
