from hashlib import sha256

import json

class Block:
    def __init__(self, index, transactions, timestamp, previousHash, nonce = 0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.nonce = nonce
    
    @staticmethod
    def fromDict(blockDict):
        block = Block(blockDict['index'], blockDict['transactions'], blockDict['timestamp'], blockDict['previousHash'], blockDict['nonce'])
        block.hash = blockDict['hash']
        return block
    
    def computeHash(self):
        # This method will return the hash of whatever contents are in the block

        block_string = json.dumps(self.__dict__, sort_keys = True)
        return sha256(block_string.encode()).hexdigest()