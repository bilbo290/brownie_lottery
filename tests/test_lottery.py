# 0.019
# 190000000000000000
from brownie import Lottery, accounts, config, network
from web3 import Web3
import time


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    time.wait(1)
    # assert lottery.getEntranceFee() > Web3.toWei(0.018, "ether")
    # assert lottery.getEntranceFee() < Web3.toWei(0.022, "ether")
