from hashlib import sha256

from block import Block
import time

class Blockchain:
    # Setting up how difficult our proof of work algorithm is
    difficulty = 1

    def __init__ (self):
        self.unconfirmedTransactions = []
        self.chain = []

        # User validations, sort of like an 'account'
        self.openSurveys = {}

        # Setting up the smart contracts
        self.chainCode = {'chain': self.chain,
                            'open_surveys': self.openSurveys,
                            'unconfirmed_transactions': self.unconfirmedTransactions}
        
        self.create_genesis_block()
    

    @staticmethod
    def fromList(chain):
        blockchain = Blockchain()
        blockchain.unconfirmedTransactions = []

        for block in chain:
            blockchain.chain.append(Block.fromtDict(block))
        
        return blockchain
    
    def createGenesisBlock(self):
        # Method to make the first block of the block chain (genesis block)

        genesisBlock = Block(0, [], time.time(), "0")

        # First initiation proof of work
        self.proofOfWork(genesisBlock)

        genesisBlock.hash = genesisBlock.compute_hash()

        self.chain.append(genesis_block)
    
    @property
    def lastBlock(self):
        return self.chain[-1]
    
    def addBlock(self, block, proof):

        # This method adds to the blockchain after verifying PoW and
        # Ensuring previousHash in the block is the same as the newest block in the chain

        previousHash = self.lastBlock.hash

        if previousHash != block.previousHash:
            return False
        
        if not Blockchain.isValidProof(block, proof):
            return False
        
        block.hash = proof
        self.chain.append(block)
        return True
    
    def proofOfWork(self, block):
        # This method goes through values of nonce until it gets a hash satisfying the difficulty we set

        block.nonce = 0

        computedHash = block.computeHash()

        while not computedHash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computedHash = block.computeHash()
        
        return computedHash
    
    def addNewTransaction(self, transaction):
        self.unconfirmedTransaction.append(transaction)
    
    @classmethod
    def isValidProof(cls, block, blockHash):
        # Method to check if blockHash is a valid hash of block

        return (blockHash.startswith('0' * Blockchain.difficulty) and blockHash == block.computeHash())
    
    @classmethod
    def check_chain_validity(cls, chain):
        result = True
        previousHash = "0"

        for block in chain:
            blockHash = block.hash

            delattr(block, "hash")

            if not cls.isValidProof(block, blockHash) or previousHash != block.previousHash:
                result = False
                break

            block.hash, previousHash = blockHash, blockHash
        
        return result

print("everything working")