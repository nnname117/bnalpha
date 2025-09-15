import os
from binance.client import Client
import config

class SpotAlpha:
    def __init__(self):
        self.client = Client(config.BINANCE_API_KEY, config.BINANCE_API_SECRET)

    def run(self):
        # 示例：获取账户信息
        account_info = self.client.get_account()
        print("账户信息:", account_info)
        # 示例：获取当前价格
        price = self.client.get_symbol_ticker(symbol="BTCUSDT")
        print("BTCUSDT 当前价格:", price)
        # 更多交易逻辑可在此扩展
