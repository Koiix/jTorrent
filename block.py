import State

BLOCK_SIZE = 2 ** 14

class Block(object):

	def __init__(self, state: State = State.FREE, size: int = BLOCK_SIZE, data: bytes = b''):
		self.size: int = size
		self.data: bytes = data
		self.state: State = state