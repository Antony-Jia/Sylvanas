from web3 import Web3, EthereumTesterProvider
from web3 import Web3, AsyncHTTPProvider
from web3.eth import AsyncEth
from web3.net import AsyncNet
import json

from tornado.ioloop import IOLoop
from tornado.queues import Queue
from tornado.httpclient import AsyncHTTPClient


class Web3Util:

    async_web3: None
    
    apikey = '2ZR1W2G6A8Y7WMVINBMPQ6A3NST8AYNU6K'

    uniswap_factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

    def __init__(self, url) -> None:
        self.initProvider(url)


    def initProvider(self, url='https://bsc-dataseed3.defibit.io/'):
        self.async_web3 = Web3(
            AsyncHTTPProvider(url),
            modules={'eth': (AsyncEth,),
                     'net': (AsyncNet,)
                     },
            middlewares=[]   # See supported middleware section below for middleware options
        )

    async def getAbi(self, address):
        abi_endpoint = f"https://api.bscscan.com/api?module=contract&action=getabi&address={address}&apikey={self.apikey}"
        http_client = AsyncHTTPClient()
        try:
            response = await http_client.fetch(abi_endpoint)
            return json.loads(response.body)
        except Exception as e:
            print("Error: %s" % e)
            
    async def getTotalSupply(self, address, abi):
        FactoryContract = self.async_w3.eth.contract(address = address, abi=abi)
        res = await FactoryContract.functions.totalSupply().call()
        return res
    
    async def getName(self, address, abi):
        FactoryContract = self.async_w3.eth.contract(address = address, abi=abi)
        name = await FactoryContract.functions.name().call()
        return name
    
    async def getSymbol(self, address, abi):
        FactoryContract = self.async_w3.eth.contract(address = address, abi=abi)
        symbol = await FactoryContract.functions.symbol().call()
        return symbol
    
    
    @classmethod
    def get_singleton(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls(*args, **kwargs)
        return cls._instance


web3instance = Web3Util('https://bsc-dataseed3.defibit.io/')