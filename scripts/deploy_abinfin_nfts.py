from brownie import ABInfinityERC1155, ABInfinityERC721, accounts, network, config

def main():
    dev = accounts.add(config['wallets']['from_key'])
    addressList = [dev.address for x in range(50)]
    uriList = ["" for x in range(50)]
    print(network.show_active())
    print(dev)
    publish_source = False
    print("deploying ERC1155...")
    ab_infin = ABInfinityERC1155.deploy(
        "base_uri",
        {"from": dev},
        publish_source=publish_source
    )
    print("minting 50 ERC1155s...")
    ab_infin.batchMint(addressList, uriList, {"from": dev}) # should mint 50
    print("Deploying ERC721...")
    ab_infin_erc721 = ABInfinityERC721.deploy(
        "base_uri",
        {"from": dev},
        publish_source=publish_source
    )
    print("Minting 50 ERC721s...")
    ab_infin_erc721.batchMint(addressList, uriList, {"from": dev}) # should mint 50
