class Card():
	def __init__(self, suit, numerical_value, symbol_name, kozr) -> None:
		self.suit = suit
		self.numerical_value = numerical_value
		self.symbol_name = symbol_name
		self.kozr = kozr
	
	def __ge__(self, other):
		if self.kozr == True and other.kozr == True:
			return (self.numerical_value >= other.numerical_value)
		elif self.kozr == True:
			return True
		elif other.kozr == True:
			return False
		else:
			return self.numerical_value >= other.numerical_value
