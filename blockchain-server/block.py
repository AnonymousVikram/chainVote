from hashlib import sha256

import json

class Block:
    def __init__(self, index,first_name, last_name, candidate, na_id,previousHash, nonce = 0):
        self.index = index 
        self.first_name = first_name
        self.last_name = last_name
        self.candidate = candidate
        self.na_id = na_id
        self.previousHash = previousHash
        self.nonce = nonce
    
    @staticmethod
    def fromDict(blockDict):
        block = Block(blockDict['index'], blockDict['first_name'], blockDict['last_name'], blockDict['candidate'],blockDict['na_id'] ,blockDict['previousHash'],blockDict['nonce'])
        block.hash = blockDict['hash']
        return block
    
    def computeHash(self):
        # This method will return the hash of whatever contents are in the block

        block_string = json.dumps(self.__dict__, sort_keys = True)
        return sha256(block_string.encode()).hexdigest()



Block1 = Block()

print(Block1)
