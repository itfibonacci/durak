class Card():
	def __init__(self, suit, numerical_value, symbol_name, kozr) -> None:
		self.suit = suit
		self.numerical_value = numerical_value
		self.symbol_name = symbol_name
		self.kozr = kozr
	
	def __ge__(self, other):
		if not isinstance(other, Card):
			return NotImplemented
		if self.kozr == True and other.kozr == True:
			return (self.numerical_value >= other.numerical_value)
		elif self.kozr:
			return True
		elif other.kozr:
			return False
		else:
			return self.numerical_value >= other.numerical_value
	
	def __str__(self) -> str:
		return f'Card: suit: {self.suit} numerical_value: {self.numerical_value} symbol_name: {self.symbol_name} kozr: {self.kozr}'
