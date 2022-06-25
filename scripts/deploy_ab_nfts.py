from brownie import ABInfinityERC721, accounts, network, config
def main():
    dev = accounts.add(config['wallets']['from_key'])
    full_address_list = [
        '0xC568C8203278844F5C72b6Aa1EB381e368A4B46e',
        '0x5bc9429285411D7C16244A87e9151D0275AcF33D',
        '0xC523758121E432E493C482449E5F8d629C0e2fA5',
        '0x72D7a14954550eF9fc75E27450C9eD6D1913b83c',
        '0x8EB2F9500698c5E94bADf7fA4F9Ca6cbe7c1740D',
        '0x8F4B7407326cE6261eBD38582f28f0156c055a42',
        '0x72FCAa6B2c3C9A99351457f602473B835585B80C',
        '0xB4f52D334E5C14691db094e7Bea187e5f4196D34',
        '0x7279590c3d7D51d9FA7e7678FaDE11cFc5499DD8',
        '0xeCf37ca251925a39D0Ed454f9df775277000Ecf0',
        '0x8171e2D2DA3ca4e8B8DF69a14B3bAEAa1f1Cd974',
        '0x962B008a7CC3547f38d80083dFf9bB22D7bFFBC2',
        '0xA5f680E5dfB4b2631D075F2e4a35Ee8A5f9ca3D7',
        '0xBa20C2efb070aFA1a2B5202405D4842fFFA87ec7',
        '0x2781Dc4A848182fe76Aff67093B6d9abE74239FC',
        '0xfe63d419D2C2FCb7472Bb602F41c6Bfe80cc136e',
        '0xae640e3b359e07f10A42D40b69E89Cb2e3782F17',
        '0xE35271122156a2488Fc1Af6477b2E68D8920f549',
        '0xf4FD9C1Bd7257b9F78edb75fbeEC23952DfB47a5',
        '0xf4FD9C1Bd7257b9F78edb75fbeEC23952DfB47a5',
        '0x56169f802Ffe1F6BAD4a8aaC9C58030E449A6286',
        '0xfe63d419D2C2FCb7472Bb602F41c6Bfe80cc136e',
        '0xd139f2d9ac5600d033B909e01150f350c0f0dd5A',
        '0x48713f62fcB7F880169bCEf5Be37c13304079e0f',
        '0x169AeD80C742FaF9489C2152C6D1Ef5Fc9BaADa9',
        '0xA10E9B751A8c91B5d7734C2257A4cc408e2b069b',
        '0x077AfbE98C34e67d0c001FD7A4631b24bb10eCC4',
        '0xc3f3Ea610f7DC5C20f932247d61C5FC41A851e09',
        '0xae727E004261401e6280F68f1CE18dB9cc1270A5',
        '0xfcC8fb67EAb6067E284EBCC04D04373d7afE60a3',
        '0x8A216d2F8C4AAA1d5167d75d55ba920bb5D6E8e5',
        '0xaD3ec4A17618fdf26223296B7AA254D19Fe809E2',
        '0x31cB716DAce61Af3856d877E432b4A23aF04cE0b',
        '0xAC6E3B2851383df5c975E56f2268b24733fAA476',
        '0xAC6E3B2851383df5c975E56f2268b24733fAA476',
        '0x6611187efBACBcD6438A3687d4bC104d6EA45506',
        '0x873B9EC41E04B81CCb394145223EBff3Bb09c0e2',
        '0xd008162778d56B27Bcfb8b7D76d6C87148c715f0',
        '0x218EcF35eA11e3214A99FdC4af14fFed37fcC555',
        '0x2162c9f6A619daC489Ff6C3A8D565c1183fAb6C4',
        '0x7dB9322928cFF24B4a7136359acDB0b9F2Db452D',
        '0x85B5f056b6324258F832bF0c855091Ed505F3154',
        '0x5f0822eb8B48e49808ba49C09Ab6225782c6D577',
        '0x1657861bf6B65d9a881763dB28D69078df2ea4a6',
        '0xBaCE94Fa917dbc18DDebAEc03e7bcA9E9588D61a',
        '0x3Fb007fe029D13a07d20aC86ed8e4D126B91f0F1',
        '0x4963c269F48a884B326105E7Ce1a91591Db0C87a',
        '0x80aCDAdfDC65F011c3DDC75F7dbae7d06F5339bf',
        '0x53fea23c6Cd8F81D42fCdFc8F498033a761c5d9D',
        '0xfc0503F7f452D33D207b580D9c9ac86a8b1885dd',
        '0x588230508A21757c625425A0002F57a11b4a4808',
        '0x1441EFcff1Bb20f8A4EEda89991e8DC30bCeb32e',
        '0xd008162778d56B27Bcfb8b7D76d6C87148c715f0',
        '0x74d44D58412C4528E7D0f49d1b1Cdb851a23D193',
        '0xCAAab9f83EFB833AbC1950A93C762f34D4a7fFc1',
        '0x4D1c20E41c3D473D3CbD69D0781a15CFc40F70Cd',
        '0x7e834F5162eCC206172700F81c64ED71A72278AA',
        '0x5318Fa8B0d25D8f5FE3e22F356e394d557383EFC',
        '0x1657861bf6B65d9a881763dB28D69078df2ea4a6',
        '0x4f01e3180D851892A1F03CE91C912084C98b92A5',
        '0x0902AC5792CB80464477E50deF260EF0150f5475',
        '0x59aBb269eacEadA410863C002e208625035eE9a6',
        '0x9114e9F1d511F43150d4fc881CB061Bdfc328Da2',
        '0xA730f692a6a7cc47f59A84987E5469503D23E7D6',
        '0xdC8E1331dB4EdaF366437D3b257325E83c6f92fD',
        '0x2F60346b78b909b05772d9B384C6fA723f531563',
        '0x127570e9f9f1B20E1b3a34542E83351b6C641687',
        '0xaEF81e2Dc1d1f346ddD345f0B8b57D47A2c8A441',
        '0x92C1FC3B8fd73c405d300dF60947393C5933E00E',
        '0x3061867a6399d79fc4Fef9b50a2107F99f80c513',
        '0x154D22E53cEE91F4A9a8aa575889C2c66547beBA',
        '0xBD003872B5ED56c5D60e714d7d8B255B7E7465EE',
        '0x5093bB0638666e637b9447A9a37Fc58169302D4b',
        '0xd9f5DA3fF6213257F8Cd25e3666Bcbd305367F2b',
        '0x4D02e7c717989FB070cF91Ac8f679Ef058551074',
        '0x5DC2E867Af5967730DAeEB514D5F4401e6eb0424',
        '0x7a701c702342E6FaFc3F68a7B0f4a766e0954fCC'
    ]
    full_address_list += ['0x3B51AA7ed6ce2b3c610C8203853544828e33f891']*5
    full_address_list += ['0x79eC8a06C3fF1Db0Fda7E7613CAF6Db122991580']*3
    full_address_list += ['0x666b44656948d918891A0B61a3b0A687bbD921bd']*2
    full_address_list += ['0x310A9fF3881A5C2354f9bfB3e0DEb1190151aFeF']*6
    full_address_list += ['0x374E4F9EF906F3e51df1b3305936Ec18A6797748']*2
    print("The full length of the address list is: " + str(len(full_address_list)))
    address_list_1 = [full_address_list[i] for i in range(0, 50)]
    address_list_2 = [full_address_list[i] for i in range(50, len(full_address_list))]
    launch_uri = 'ipfs://bafybeif35kae2mklkuu7o4f3rvr62formjr64tt5ham6nifg27nwlswxhm/'
    print(network.show_active())
    print(dev)
    publish_source = True
    print("deploying AB Infinity contract...")
    ab_infin = ABInfinityERC721.deploy(
        launch_uri,
        95,
        ['0x310A9fF3881A5C2354f9bfB3e0DEb1190151aFeF', '0xC568C8203278844F5C72b6Aa1EB381e368A4B46e', '0xA730f692a6a7cc47f59A84987E5469503D23E7D6', '0x666b44656948d918891A0B61a3b0A687bbD921bd', '0xd5bCF754660E4908569713D8829381f4935dc152', '0x374E4F9EF906F3e51df1b3305936Ec18A6797748'],
        [18, 18, 16, 16, 16, 16], {"from": dev},
        publish_source=publish_source
    )
    print("minting the first 50 ERC721s...")
    ab_infin.firstBatchMint(address_list_1, {"from": dev}) # should mint 50
    print("minting the remaining ERC721s...")
    ab_infin.firstBatchMint(address_list_2, {"from": dev}) # should mint the remainder
    print(ab_infin.tokenURI(1))
    print(ab_infin.totalSupply())
    # # put some eth into the contract
    # accounts[1].transfer(ab_infin, 100)
    # # testing release() 
    # tx = ab_infin.release(dev.address,{"from": dev})



