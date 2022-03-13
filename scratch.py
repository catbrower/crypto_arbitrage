import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

network = 'mainnet'
wallet_addr = os.getenv('WALLET_ADDR')
project_url = f'https://%s.infura.io/v3/%s' % (network, os.getenv('PROJECT_ID'))

w3 = Web3(Web3.HTTPProvider(project_url))

addresses = json.loads(open('addresses.json', 'r').read())
UniswapV2FactoryABI = json.loads(open('abis/IUniswapV2Factory.json', 'r').read())['abi']
UniswapV2PairABI = json.loads(open('abis/IUniswapV2Pair.json', 'r').read())['abi']
InchOffChainOracleABI = json.loads(open('abis/1InchOffChainOracle.json', 'r').read())['abi']

uniswap_factory = w3.eth.contract(
    Web3.toChecksumAddress(addresses['uniswap']['factory']),
    abi=UniswapV2FactoryABI)

sushiswap_factory = w3.eth.contract(
    Web3.toChecksumAddress(addresses['sushiswap']['factory']),
    abi=UniswapV2FactoryABI)

uni_eth_usdc = w3.eth.contract(
    uniswap_factory.functions.getPair(
        Web3.toChecksumAddress(addresses['uniswap']['ETH']),
        Web3.toChecksumAddress(addresses['uniswap']['USDC'])
    ).call(),
    abi=UniswapV2PairABI
)

sushi_eth_usdc = w3.eth.contract(
    sushiswap_factory.functions.getPair(
        Web3.toChecksumAddress(addresses['uniswap']['ETH']),
        Web3.toChecksumAddress(addresses['uniswap']['USDC'])
    ).call(),
    abi=UniswapV2PairABI
)

inch_oracle = w3.eth.contract(
    Web3.toChecksumAddress(addresses['1inch']['offChainOracle']),
    abi=InchOffChainOracleABI
)

rate = inch_oracle.functions.getRateToEth(
    Web3.toChecksumAddress(addresses['uniswap']['SNX']),
    True
).call()

print(str(rate))
print(len(str(rate)))
# rate = int(str(rate).ljust(27, '0'))
print('{:.36f}'.format(rate / 1e18))