from torrent import Torrent

class Main(object):

	def __init__(self):
		self.torrent = Torrent().load("./assets/big-buck-bunny.torrent")
		print(repr(self.torrent))