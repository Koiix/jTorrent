from piece import Piece
from state import State
import logging

class StorageManager(object):

	def __init__(self, torrent):

		self.torrent = torrent
		self.piece_size = self.torrent.piece_length
		self.num_pieces: int = self.torrent.num_pieces
		self.pieces: list[Piece] = init_pieces()
		map_files()

	def has_completed(self):
		for piece in self.pieces:
			if piece.state != State.FULL:
				return False
		return True

	def get_block(self, piece_index, block_offset, block_size):
		# invariant: only get blocks from full pieces
		return self.pieces[piece_index].get_block(block_offset, block_size) if self.pieces[piece_index].state == State.FULL else None

	def init_pieces(self):
		pieces = []	

		hash_begin = 0
		hash_end = 20
		for  i in range(self.num_pieces):
			
			size = self.torrent.total_length - (self.num_pieces - 1) * self.piece_size if i == self.num_pieces - 1 else self.piece_size

			pieces.append(Piece(i, size, self.torrent.piece_hashes[hash_begin:hash_end]))


	def map_files(self):
		files = []
		piece_offset = 0
		allocated = 0

		for f in self.torrent.files:
			file_size = f["length"]
			file_offset = 0

			while file_size > 0:
				piece_num = int(piece_offset / self.piece_size)
				piece = self.pieces[piece_num]
				to_allocate = piece.size - allocated

				piece.assign_file(f["path"], file_size, file_offset)

				if file_size < to_allocate:
					piece_offset += file_size
					allocated += file_size
					file_size = 0
				else: # file_size >= to_allocate
					file_size -= to_allocate
					piece_offset += to_allocate
					file_offset += to_allocate
					allocated = 0

			
