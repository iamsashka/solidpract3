from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_address, abi=abi)

print (contract.address)

print(f"Баланс смарт контракта: {w3.eth.get_balance(contract.address)}")
print(f"Баланс первого аккаунта: {w3.eth.get_balance('0x2d6dBcDAa4DD4890339251743F112dFecDe7205D')}")
print(f"Баланс второго аккаунта: {w3.eth.get_balance('0x1D25015317d7513cedCD0517C89E80dcDAB83291')}")
print(f"Баланс третьего аккаунта: {w3.eth.get_balance('0x80CF6dF5cCd532063D6Dd25323F825C728409fcE')}")
print(f"Баланс четвертого аккаунта: {w3.eth.get_balance('0x8cb01d9aEAB71DC7f24CC1Cddb38dBEa8B2504c8')}")
print(f"Баланс пятого аккаунта: {w3.eth.get_balance('0x0a5d8F8AF7eF0C27b455c2523511243D5F5c034c')}")