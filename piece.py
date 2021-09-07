from block import Block, BLOCK_SIZE
from state import State
import math
import hashlib
import logging

class WrongStateException(Exception):
	pass

class Piece(object):

	def __init__(self, index, size, hash):
		self.index: int = index
		self.size : int = size
		self.files = []
		self.hash = hash
		self.state : State = State.FREE
		self.num_blocks : int = math.ceil(self.size / BLOCK_SIZE)
		self.blocks : list[Block] = []

	def assign_file(self, file_path, file_size, file_offset : int = 0):
		self.files.append((file_path, file_size, file_offset));

	def set_block(self, offset, data):
		index = int(offset / BLOCK_SIZE)

		if self.state != State.FULL && self.self.blocks[index].state != State.FULL:
			self.blocks[index].data = data
			self.blocks[index].state = State.FULL
			self.state = State.PENDING

	def has_completed(self):
		for block in blocks:
			if block.state != State.FULL
				return False
		self.state = State.FULL
		return True
	
	def write_to_files(self):

		if self.state != State.FULL:
			raise WrongStateException()

		for block in self.blocks

		data_ptr = 0
		data_left = self.size
		file_space = 0

		for file in self.files:

			file_path, file_size, file_offset = file

			try:
				if os.path.exists(file_path):
					f = open(file_path, "rb+")
				else:
					f = open(file_path, "wb")
			except Exception:
				logging.exception("Piece.write_to_files() failed to open file")



			f.seek(file_offset)

			file_space = file_size - file_offset

			if(data_left <= file_space):
				f.write(self.data[data_ptr:self.size])
				data_ptr += data_left
				data_left -= data_left
			else:
				f.write(self.data[data_ptr:data_ptr+file_space])
				data_ptr += file_space
				data_left -= file_space

			f.close()

		assert(data_ptr == self.size)
		assert(data_left == 0)

	def validate(self):

		if self.state != State.FULL:
			return False
		else:
			return hashlib.sha1(self.raw_data).digest() == self.hash