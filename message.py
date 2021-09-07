import random
import socket
import logging
from struct import pack, unpack

class ImplementationException(Exception):
	pass

class InvalidMessageException(Exception):
	pass

class Message(object):

	@staticmethod
	def get_peer_message(packet):
		try:
			if unpack(">I", self.packet[:4]) == 0:
				return KeepAlive.decode(self.packet)
			else:
				message_id = unpack(">B", self.packet[4:5])
		catch Exception e:
			logging.warning("Error unpacking message: %s" % e)
			return None

		switch = {
			0: Choke,
            1: UnChoke,
            2: Interested,
            3: NotInterested,
            4: Have,
            5: BitField,
            6: Request,
            7: Piece,
            8: Cancel,
            9: Port
		}

		if message_id not in switch:
			raise InvalidMessageException()
		else:
			return switch[message_id].decode(packet)

	def encode(self):
		raise NotImplementedError()

	# construct class from pack
	@classmethod 
	def decode(cls, packet):
		raise NotImplementedError()

class KeepAlive(Message):
	packet_length = 4
	payload_length = 0
	
	def __init(self)__:
		super(KeepAlive, self).__init__()

	def encode(self):
		return pack(">I", self.payload_length)

	def decode(cls, packet):
		assert(unpack(">I", packet[:packet_length]) == payload_length)
		return cls()

class Choke(Message):

	packet_length = 5
	payload_length = 1
	message_id = 0

	def __init__(self):
		super(Choke, self).__init__()

	def encode(self):
		return pack(">IB", self.payload_length, self.message_id)

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()


class UnChoke(Message):

	packet_length = 5
	payload_length = 1
	message_id = 1

	def __init__():
		super(UnChoke, self).__init__()

	def encode(self):
		return pack(">IB", self.payload_length, self.message_id)

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()

class Interested(Message):

	packet_length = 5
	payload_length = 1
	message_id = 2

	def __init__():
		super(Interested, self).__init__()

	def encode(self):
		return pack(">IB", self.payload_length, self.message_id)

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()

class NotInterested(Message):

	packet_length = 5
	payload_length = 1
	message_id = 3

	def __init__():
		super(NotInterested, self).__init__()

	def encode(self):
		return pack(">IB", self.payload_length, self.message_id)

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()

class Have(Message):

	packet_length = 5
	payload_length = 1
	message_id = 3

	def __init__():
		super(Have, self).__init__()

	def encode(self, self.piece_index):
		return pack(">IBI", self.payload_length, self.message_id)

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()

class BitField(Message):


	def encode(self):
		return pack(">IB", self.payload_length, self.message_id)

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()

class Request(Message):

	def encode(self):
		

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()

class Piece(Message):

	def encode(self):

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()

class Cancel(Message):

	def encode(self):

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()



class Port(Message):

	def encode(self):

	def decode(cls, packet):
		payload_length, message_id = unpack(">IB", packet[:length])
		assert(payload_length == self.payload_length && message_id == self.message_id)
		return cls()

class UdpAnnounceRequest:

	def __init__():
		super(UdpAnnounceRequest, self).__init__()

	def encode(self):

	@classmethod
	def decode(cls, packet):

class UdpAnnounceResponse(Message):

	def __init__(self):
		super(UdpAnnounceResponse, self).__init__()

	def encode(self):

	@classmethod
	def decode(cls, packet):