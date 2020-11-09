from web3 import Web3


def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/b85ca4dfafd94e1ea8f0b77e326fdc64'))
    address = '0x153A203d93e741bB328e8Fb8d631e319558e7230'
    privateKey = '0xe91616c05da0c190f86d8ac508779e1522031f478b285c032db709079adcecd3'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, "ether")
    signedTx = w3.eth.account.sign_transaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0xFe0196504dF34c4Bf30D3089EfFf86cFe3B34617',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)
    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId

