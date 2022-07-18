# modulee 1- create the blockchain
import datetime
import hashlib
import json
from flask import Flask, jsonify


# Building blockchain

class Blockchain:
    def _init_ (self):
        self.chain = []
        self.create_Block(proof= 1, previousHash = '0')
        
        # we now create a block
        def create_Block(self,proof, previousHash):
            
            # create the block dictionary
            block = {'index': len(self.chain() + 1),
                  'timestamp' : str(datetime.datetime.now()),
                  'proof' : proof,
                  'previous_hash' : previousHash}
            
            # we now append the block to our object 
            self.chain.append(block)
            return block
            
        # we now create a function to get the previous block
        
        def get_previous_block(self):
            return self.chain[-1]
            
        # we now create a function of proof of work
        
        def proof_of_work(self, previous_proof):
            new_proof = 1
            check_proof = False
            
            while check_proof is False:
                hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexidigest()
                if hash_operation[:4] == '0000':
                    check_proof = True
                else:
                    new_proof +=1
                    return new_proof
                
                # now we create a hash for each block
                
                def hash_block(self, block):
                    encoded_block = json.dumps(block, sort_keys = True).encode()
                    
                     
                    return hashlib.sha256(encoded_block).hexidigest()
               
                # now we check the validity of our chain
                
                def is_chain_valid(self, chain):
                    previous_block = chain[0]
                    block_index = 1
                    
                    while block_index < len(self.chain):
                        block = chain[block_index]
                        if block['previous_hash'] != self.hash_block(previous_block):
                            
                            return False
                        previous_proof = previous_block['proof']
                        proof = block['proof']
                        
                        hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexidigest()
                        
                        if hash_operation[:4] != '0000' :
                            
                          return False
                        previous_block = block
                        block_index +=1
                    
                        return True
                    
                    
                        
                        
       
        #creating web pp with Flask
app = Flask(__name__)
        
        # creating an instance of Blockchain
blockchain = Blockchain()
        
        #Mining a blockchain
@app.route ('/mine_block' , methods = ['Get'])
def mine_block():
    
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash_block(previous_block)
    block = blockchain.create_Block(proof, previous_hash)
    response = {'index' : block['index'],
                'timestamp'  : block['timestamp'],
                'proof'  : block['proof'],
                'previous_hash'  : block['previous_hash']}
    return jsonify(response), 200

@app.route('/get_chain', methods = ['Get'])
def get_chain():
    response = { 'chain' : blockchain.chain,
                'length' : len( blockchain.chain)}  
    return jsonify(response), 200

app.run(host = "0.0.0.0" , port = 5000)



