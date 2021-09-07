from bcoding import bencode, bdecode
import logging
import hashlib
import time
import os

class Torrent(object):
    def __init__(self):
        self.meta_info = {}
        self.total_length: int = 0
        self.piece_length: int = 0
        self.piece_hashes: int = 0
        self.info_hash: str = ''
        self.peer_id: str = ''
        self.created_by: str = ''
        self.comment: str = ''
        self.announce_list = []
        self.files = []
        self.num_pieces: int = 0

    def load(self, path):
        with open(path, 'rb') as file:
            self.meta_info = bdecode(file.read())
        self._parse()
        self._init_files()

        return self

    def _parse(self):

        self.piece_length = self.meta_info['info']['piece length']
        self.piece_hashes = self.meta_info['info']['pieces']
        raw_info_hash = bencode(self.meta_info['info'])
        self.info_hash = hashlib.sha1(raw_info_hash).digest()
        self.peer_id = self._generate_peer_id()
        if 'announce-list' in self.meta_info:
            self.announce_list = self.meta_info['announce-list']
        else:
            self.announce_list = [[self.meta_info['announce']]]
        self.num_pieces = int(len(self.piece_hashes)/20)

    def _init_files(self):
        name = self.meta_info['info']['name']

        if 'files' in self.meta_info['info']:
            if not os.path.exists(name):
                os.mkdir(name)

            for file in self.meta_info['info']['files']:
                full_path = os.path.join(name, *file["path"])

                if not os.path.exists(os.path.dirname(full_path)):
                    os.makedirs(os.path.dirname(full_path))

                self.files.append({"path": full_path , "length": file["length"]})
                self.total_length += file["length"]

        else:
            self.files.append({"path": name, "length": self.meta_info['info']['length']})
            self.total_length = self.meta_info['info']['length']

        assert(self.total_length > 0)
        assert(len(self.files) > 0)
        

    def _generate_peer_id(self):
        seed = str(time.time())
        peer_id = b'-JT0001-' + hashlib.sha1(seed.encode('utf-8')).digest()[:12]
        assert(len(peer_id)==20)
        return peer_id


    def __repr__(self):
        return str(self.meta_info)