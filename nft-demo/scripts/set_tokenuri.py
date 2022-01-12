from brownie import network, SimpleCollectible

from scripts.deploy_cat_nft import OPENSEA_URL, get_account

TOKEN_URI = "https://ipfs.io/ipfs/QmfGLULUiXniEW3jXXji4eEVybPqTF2UngFTRv9e3vPfJK?filename=ArsenCat0.json"


def main():
    simple_collectible_contract = SimpleCollectible[-1]
    for token_id in range(simple_collectible_contract.tokenCounter()):
        if not simple_collectible_contract.tokenURI(token_id).startswith("https://"):
            setTokenURI(token_id, simple_collectible_contract, TOKEN_URI)


def setTokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(2)
    print(f"NFT is deployed at {OPENSEA_URL.format(nft_contract.address, token_id)}")
