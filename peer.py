import socket
import struct
import bitstring
import logging
import message

class Peer(object):

	def __init__(self, num_pieces, ip, port=6881):
		self.num_pieces = num_pieces
		self.connected = False
		self.ip = ip
		self.port = port
		self.socket = None
		self.has_pieces: list[bool] = [False * num_pieces]

	def connect(self):
		try:
			self.socket = socket.create_connection((self.ip, self.port), timeout = 2)
			self.socket.setblocking(False)
			logging.debug("Connected to peer ip=%d port=%d" % (self.ip, self.port))
			self.connected = True

		except Exception as e:
			logging.debug("Failed to connect to peer ip=%d port=%d" % (self.ip, self.port))
			return False

		return True

	def has_piece(self, index):
		return self.has_pieces[index]

	def close_socket(self):
		try:
			self.socket.close()
		except Exception:
			logging.exception("PeerWire - failed to close socket")