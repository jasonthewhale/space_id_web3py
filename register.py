from web3 import Web3, HTTPProvider
import json
import time

address = '' #wallet address
private_key = ''
spaceid_ADDRESS = Web3.toChecksumAddress('b504f72985486001119c4068a61bE0b476614930') #contract address
rpc = 'https://bsc-dataseed.binance.org/'
spaceid_ABI = json.loads('[{"inputs":[{"internalType":"contract BaseRegistrarImplementation","name":"_base","type":"address"},{"internalType":"contract IPriceOracle","name":"_prices","type":"address"},{"internalType":"uint256","name":"_minCommitmentAge","type":"uint256"},{"internalType":"uint256","name":"_maxCommitmentAge","type":"uint256"},{"internalType":"uint256","name":"_startTimestamp","type":"uint256"},{"internalType":"uint256","name":"_endTimestamp","type":"uint256"},{"internalType":"uint256","name":"_dailyQuota","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":true,"internalType":"bytes32","name":"label","type":"bytes32"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"cost","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"expires","type":"uint256"}],"name":"NameRegistered","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":true,"internalType":"bytes32","name":"label","type":"bytes32"},{"indexed":false,"internalType":"uint256","name":"cost","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"expires","type":"uint256"}],"name":"NameRenewed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oracle","type":"address"}],"name":"NewPriceOracle","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"MIN_REGISTRATION_DURATION","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"available","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"claimed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"commitment","type":"bytes32"}],"name":"commit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"commitments","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"dailyQuota","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"dailyUsed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"endTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentDayUsage","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"day","type":"uint256"}],"name":"getDayUsageOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"isClaimable","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bytes32","name":"secret","type":"bytes32"}],"name":"makeCommitment","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bytes32","name":"secret","type":"bytes32"},{"internalType":"address","name":"resolver","type":"address"},{"internalType":"address","name":"addr","type":"address"}],"name":"makeCommitmentWithConfig","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"maxCommitmentAge","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minCommitmentAge","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"duration","type":"uint256"},{"internalType":"bytes32","name":"secret","type":"bytes32"}],"name":"register","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"duration","type":"uint256"},{"internalType":"bytes32","name":"secret","type":"bytes32"},{"internalType":"address","name":"resolver","type":"address"},{"internalType":"address","name":"addr","type":"address"}],"name":"registerWithConfig","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"renew","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"rentPrice","outputs":[{"components":[{"internalType":"uint256","name":"base","type":"uint256"},{"internalType":"uint256","name":"premium","type":"uint256"}],"internalType":"struct IPriceOracle.Price","name":"price","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_minCommitmentAge","type":"uint256"},{"internalType":"uint256","name":"_maxCommitmentAge","type":"uint256"}],"name":"setCommitmentAges","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IPriceOracle","name":"_prices","type":"address"}],"name":"setPriceOracle","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceID","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"}],"name":"valid","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
web3 = Web3(HTTPProvider(rpc))
ens_contract = web3.eth.contract(address=spaceid_ADDRESS, abi=spaceid_ABI)
    
def make_commit(ens, addr, num32):
    """
    num32 means 32 random numbers
    need to add "0x" before give input
    """
    commitment1 = ens_contract.functions.makeCommitment(ens, addr, num32)
    result = commitment1.call()
    return '0x' + result.hex()

def commitment(hex_commit):
    commitment2 = ens_contract.functions.commit(hex_commit)
    nonce = web3.eth.getTransactionCount(address)
    params = {
    "value": web3.toWei(0, 'ether'),
    'gasPrice': web3.toWei(5, 'gwei'),
    "gas": 50000,
    "nonce": nonce,
    }
    try:
        tx = func.buildTransaction(params)
        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Transaction Success! Transaction hash：{tx_hash.hex()}")
    except Exception as e:
        print(f"{address}Transaction Failed!：", e)
        
def register(pay_amount, ens, owner, time, secret):
    amount = web3.toWei(pay_amount, "ether")
    register = ens_contract.functions.commit(amount, ens, owner, time, secret)
    """
    time = 31536000 (1 year)
    secret is from make_commitment
    """
    nonce = web3.eth.getTransactionCount(address)
    params = {
    "value": web3.toWei(amount, 'ether'),
    'gasPrice': web3.toWei(5, 'gwei'),
    "gas": 50000,
    "nonce": nonce,
    }
    try:
        tx = register.buildTransaction(params)
        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Transaction Success! Transaction hash：{tx_hash.hex()}")
    except Exception as e:
        print(f"{address}Transaction Failed!：", e)
    
def main():
    make_commit(ens, addr, num32) # off-chain
    commitment(hex_commit)        # start to on-chain
    time.sleep(30)                # set 30s interval between commitment2 and register
    register(pay_amount, ens, owner, time, secret)
#main()
