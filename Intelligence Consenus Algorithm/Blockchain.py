import datetime
import hashlib


class Block:

    def __init__(self, previous_hash, transaction, nonce):
        self.previousHash = previous_hash
        self.transaction = transaction
        self.transactionHash = self.compute_transaction_hash()
        self.timestamp = str(datetime.datetime.now())
        self.hash = self.compute_hash()
        self.nonce = nonce   #POW


    def compute_hash(self):
        input = self.previousHash + self.transaction.senderAccount + self.transaction.amount\
                + self.transaction.receiverAccount + self.timestamp
        hash_result = hashlib.sha3_256(input.encode()).hexdigest()
        return hash_result

    def compute_transaction_hash(self):
        input = self.transaction.senderAccount + self.transaction.amount\
                + self.transaction.receiverAccount
        hash_result = hashlib.sha3_256(input.encode()).hexdigest()
        return hash_result


class Transaction:

    def __init__(self, sender_account, receiver_account, amount):
        self.senderAccount = sender_account
        self.receiverAccount = receiver_account
        self.amount = amount


class Chain:

    blockchain = []
    difficulty = 87927498

    def append_new_block(self, new_block):
        self.blockchain.append(new_block)

    def print_chain(self):
        print(self.blockchain[0])


class POW:

    def mine_new_block(self, previoushash, transaction, difficuty, blockchain):

        nonce = 0
        input_to_hash = previoushash + transaction.amount + transaction.receiverAccount +\
                        transaction.senderAccount
        first_hash = input_to_hash + str(nonce)
        hash_result = hashlib.sha3_256(first_hash.encode()).digest()
        print("Difficulty", bytes(difficuty))
        while bytes(hash_result) > bytes(difficuty):
            nonce = nonce + 1
            print(nonce)
            input = input_to_hash + str(nonce)
            hash_result = hashlib.sha3_256(input.encode()).digest()

        print("Block Mined")
        print("Nonce:", nonce)
        print("Block hash: ", hash_result)

        block = Block(previoushash, transaction, nonce)
        blockchain.append(block)

# blockchain = []
# transaction = Transaction('0', '1', '21')
# block = Block('0', transaction, '0')
#
# pow = POW()
# pow.mine_new_block(block.compute_hash(), transaction, 67890, blockchain)