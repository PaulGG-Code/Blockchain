#Basic Crypto_Blockain project
#imports
import hashlib
import time


#Creating Block class
class Block(object):

    #initial method
    def __init__ (self, index, proof_number, previous_hash, data, timestamp=None):
        
        self.index = index #track the position of a block within the blockchain
        self.proof_number = proof_number
        self.previous_hash = previous_hash #reference the hash of the previous block within the blockchain
        self.data = data # details of the transactions done, for example, the amount bought.
        self.timestamp = timestamp or time.time() #inserts a timestamp for all the transactions performed

    @property
    def compute_hash(self): #produce the cryptographic hash of each block based on the above values
        string_block = "{}{}{}{}{}".format(self.index, self.proof_number, self.previous_hash, self.data, self.timestamp)
        return hashlib.sha256(string_block.encode()).hexdigest()


#blockchain is based on the fact that the blocks are “chained” to each other
#blockchain class that will play the critical role of managing the entire chain
#creating Blockchain class
class BlockChain(object):
    
    def __init__(self):
        self.chain = [] #stores all the blocks
        self.current_data = []  #stores information about the transactions in the block
        self.nodes = set()  
        self.build_genesis() #create the initial block in the chain.

    
    def build_genesis(self):
        self.build_block(proof_number=0, previous_hash=0)  #default values

    def build_block(self, proof_number, previous_hash):

        block = Block(index=len(self.chain),proof_number=proof_number,previous_hash=previous_hash,data=self.current_data)

        self.current_data = []

        self.chain.append(block)
        
        return block

    @staticmethod

    #examining the integrity of the blockchain and making sure inconsistencies are lacking
    #series of if statements to assess whether the hash of each block has been compromised
    #compares the hash values of every two successive blocks to identify any anomalies
    
    def confirm_validity(block, previous_block):

        #if chain is working properly, it returns true, if not it returns false
        if previous_block.index + 1 != block.index:
            return False

        elif previous_block.compute_hash != block.previous_hash:
            return False
        
        elif block.timestamp <= previous_block.timestamp:
            return False

        return True


    def get_data(self, sender, receiver, amount):

        self.current_data.append({'sender': sender, 'receiver' : receiver, 'amount' : amount})
        
        return True


    #Proof of Work (PoW) refers to the complexity involved in mining or generating new blocks on the blockchain
    # PoW can be implemented by identifying a number that solves a problem whenever a user completes some computing work.
    #Anyone on the blockchain network should find the number complex to identify but easy to verify
    #This is the main concept of PoW
    @staticmethod
    def proof_of_work(last_proof):
        
        pass

    @property

    # retreive the last block on the network (actually the current block)
    def latest_block(self):
        return self.chain[-1]


    def chain_validity(self):
        pass

    #Usually the transactions are holded in a list of unverified transactions. 
    #Mining meaning placing a unverified transaction in a block and solve the PoW problem
    #It can be reffered to as the computing work involved in verifying the transactions
    #If everything work correctly, the block is mined or created and joing together with the others in the blockchain
    #If users have successully mined a block, in real life they are rewarded for using their computing power to solve the PoW problem

    def block_mining(self, details_miner):
        self.get_data(
            sender = "0",  #it implies that this node has created a new block
            receiver = details_miner,
            amount=1, #creating a new block or mining a block is rewarded by 1 
            )

        last_block = self.latest_block
        last_proof_number = last_block.proof_number
        proof_number = self.proof_of_work(last_proof_number)

        last_hash = last_block.compute_hash

        block = self.build_block(proof_number, last_hash)

        return vars(block)


    def create_node(self, address):

        self.nodes.add(address)
        return True

    @staticmethod
    #Return the block value
    def get_block_object(block_data):
        
        return Block(
            block_data['index'],
            block_data['proof_number'],
            block_data['previous_hash'],
            block_data['data'],
            timestamp=block_data['timestamp']

        )


blockchain = BlockChain()

print("LET'S START MINING!!")

print(blockchain.chain)

last_block = blockchain.latest_block

last_proof_number = last_block.proof_number

proof_number = blockchain.proof_of_work(last_proof_number)

blockchain.get_data(


    sender="0", #this means that this node has constructed another block
    receiver="Paul",
    amount=1, #Building a new block or succesfuly mine is awareded with 1
)

last_hash = last_block.compute_hash
block = blockchain.build_block(proof_number,last_hash)

print("NICE JOB! CODE [1] Success Mining")
print(blockchain.chain)