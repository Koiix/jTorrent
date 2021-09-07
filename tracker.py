from Peer import peer
from Message import UdpAnnounceRequest, UdpAnnounceResponse, UdpTrackerConnection
from peerwireprotocol import PeerWireProtocol, MAX_CONNECTIONS

import requests
import logging
import socket
import ipaddress
import struct
from urllib.parse import urlparse


class Tracker(object):

	def __init__(self, url):
		self.url = url
		self.event = 'started'
		self.interval = 0
		self.tracker_id = None


class Announcer(Thread):

	def __init__(self, torrent, peer_wire):
		Thread.__init__(self)
		self.torrent = torrent
		self.peer_wire = peer_wire
		self.event = 'started'
		self.trackers = []
		_init_trackers()

	def _init_trackers(self):

		for url in self.torrent.announce_list:
			self.trackers.append(Tracker(url[0]))


	def http_request(self, tracker):

		params = {
			'info_hash': self.torrent.info_hash,
			'peer_id': self.torrent.peer_id,
			'port': 6881,
			'uploaded': 0
			'downloaded': 0
			'left': self.torrent.total_length,
		}

		returned_peers = []
		
		try:

			response = requests.get(tracker.url, params=params, timeout=4)
			response_dict = bdecode(response.content)
			tracker.interval = int(response_dict['interval'])
			if 'tracker id' in response_dict:
				tracker.tracker_id = response_dict['tracker id']


			if type(response_dict['peers']) == dict:
				return response_dict['peers']
			
			
			else:

				returned_peers = []

				for _ in range(len(list_peers['peers'])//6):

	                ip = struct.unpack_from("!i", response_dict['peers'], offset)[0]
	                ip = socket.inet_ntoa(struct.pack("!i", ip))
	                offset += 4
	                port = struct.unpack_from("!H",list_peers['peers'], offset)[0]
	                offset += 2
	                peer = {}
	                peer['ip'] = ip
	                peer['port'] = port
	                returned_peers.append(peer)

	            return returned_peers

		except Exception as e:

			logging.exception(e.__str__())
			

	def run(self):

		while True:
			
			for tracker in self.trackers:

				if len(peer_wire.peers) >= MAX_CONNECTIONS:
					break

				else:
					peers = http_request(tracker)
					for peer in peers:
						if len(peer_wire.peers) >= MAX_CONNECTIONS:
							break
						if not peer_wire.has_peer(peer['ip'], peer['port']):
							new_peer = Peer(self.torrent.num_pieces, ip, port)
							if new_peer.connect():
								peer_wire.add_peer(new_peer)

			time.sleep(self.trackers[0].interval)


