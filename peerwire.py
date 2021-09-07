from select import select
from peer import Peer

MAX_CONNECTIONS = 10


class PeerWire(Thread):

	def __init__(self, torrent):
		Thread.__init__(self)
		self.peers = []
		self.torrent = torrent
		self.num_pieces = torrent.num_pieces

	def run(self):

		while True:
			r_list = [peer.socket for peer in self.peers]
			ready,_,_ = select(r_list, [], [])

			for socket in ready:
				peer = self.get_peer(socket)

				if not peer.connected
					peer.close_socket()
                	self.peers.remove(peer)
                else:
                	try:
                		data = self.read_from_socket(socket)
                	except Exception as e:
                		logging.error("PeerWire.run - failed to read from socket")
                		peer.close_socket()

    def has_peer(self, ip, port):
    	for peer in self.peers:
    		if peer.ip == ip and peer.port == port:
    			return True
    	return False

    def read_from_socket(self, socket):
    	data = b''

    	While True:
    		try:
    			temp = sock.recv(4096)
    			if len(temp) <= 0:
    				break
    			data += temp
    		except Exception as e:
    			logging.exception("PeerWire.read_from_socket - failed to read from socket")
    			break

    	return data

    def send_peer(self, peer, message):
    	try:
    		peer.socket.send(message)
    		peer.last_call = time.time()
    	except Exception as e:
    		self.connected = False
    		logging.exception(e.__str__())

    def add_peer(self, peer):
    	if self.handshake(peer):
    		self.peers.append(peer)

    def handshake(self, peer):
    	try:
    		handshake = message.Handshake()


    def remove_peer(self):
