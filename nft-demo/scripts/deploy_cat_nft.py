from brownie import network, config, SimpleCollectible
from brownie.network import accounts

LOCAL_BLOCKCHAIN = ["development", "ganache-local"]

OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN:
        return accounts[0]  # get from ganache-cli
    else:
        return accounts.add(config["wallets"]["private_key"])


def main():
    account = get_account()

    # Skip: simple_collectible_contract = SimpleCollectible.deploy({"from": account})
    # Assume that SimpleCollectible is already deployed
    print(SimpleCollectible[-1])
    tx = SimpleCollectible[-1].createCollectible({"from": account})
    tx.wait(2)

    # simple_collectible_contract = SimpleCollectible.deploy({"from": account})
    # tx = simple_collectible_contract.createCollectible({"from": account})
    # tx.wait(2)
