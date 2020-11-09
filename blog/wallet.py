from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/b85ca4dfafd94e1ea8f0b77e326fdc64'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f'Your address: {address}\nYour key: {privateKey}')
