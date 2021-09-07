from torrent import Torrent
from storagemanager import StorageManager 
from peerwire import PeerWire 
from tracker import Tracker
from piece import Piece 
from peer import Peer

import message
import time
import os

class App(object):

	def __init__(self):
		self.torrent = Torrent().load("./assets/wired-cd.torrent")

		self.storage_manager = StorageManager(self.torrent)
		self.peer_wire = PeerWire(self.torrent, self.storage_manager)

		self.announcer = Announcer(self.torrent, self.peer_wire)

		self.tracker.start()
		self.peer_wire.start()
		
	
	def start(self):

		while not self.storage_manager.has_completed():

			pieces_completed = 0

			for piece in self.storage_manager.pieces:

				if not piece.has_completed():

					empty_block = self.storage_manager().get_empty_block()

					peer_wire.request_block(block)
				
				else:

					pieces_completed ++

			os.system.clear()
			print("%d/%d pieces completed" % (pieces_completed, self.torrent.num_pieces))
			
			time.sleep(1)

		print("Torrent successfully finished downloading")
		os._exit(0)

if __name__ == "__main__":
	app = App()
	app.start()