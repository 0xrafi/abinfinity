// contracts/ABInfinity.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/finance/PaymentSplitter.sol";

contract ABInfinityERC721 is ERC721, Ownable, PaymentSplitter {
    using Counters for Counters.Counter;
    using Strings for uint256;

    address[] public artists;
    string private _firstLaunchURI;
    uint8 private _maxInitialMintCount;
    Counters.Counter private _tokenIds;
    string private _futureSetbaseURI;
    uint96 royaltyFeesInBips = 250; // 2.5%

    constructor(string memory firstLaunchURI, uint8 maxInitialMintCount, address[] memory _artists, uint256[] memory _shares) ERC721("ABInfinity","ABI") PaymentSplitter(_artists, _shares) {
        artists = _artists;
        _firstLaunchURI = firstLaunchURI;
        _maxInitialMintCount = maxInitialMintCount;
    }

    function firstBatchMint(address[] memory toAddressList) external onlyOwner {
        require(toAddressList.length <= 50, "Too many addresses provided at once.");
        for (uint i = 0; i < toAddressList.length; i++) {
            uint256 newItemId = _tokenIds.current();
            require(newItemId < _maxInitialMintCount, "First batch mint limit exceeded");
            _mint(toAddressList[i], newItemId);
            _tokenIds.increment();
        }
    }
    
    function updateLaunchURI(string memory newURI) external onlyOwner {
        _firstLaunchURI = newURI;
    }

    function setBaseURI(string memory newURI) external onlyOwner {
        _futureSetbaseURI = newURI;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        require(bytes(_futureSetbaseURI).length != 0, "Base URI has not been set.");
        return _futureSetbaseURI;
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(tokenId <= _tokenIds.current(), 'invalid tokenId');
        if (tokenId < _maxInitialMintCount) // tokens 0-94 are first batch.
            return _firstLaunchURI;
        else {
            string memory baseURI = _baseURI();
            return bytes(baseURI).length > 0 ? string(abi.encodePacked(baseURI, tokenId.toString())) : "";
        }
    }

    function updateRoyaltyFee(uint96 _royaltyFeesInBips) external onlyOwner {
        royaltyFeesInBips = _royaltyFeesInBips;
    }

    // standard function called by markets (OpenSea, etc) to execute royalties
    function royaltyInfo(uint256 _tokenId, uint256 _salePrice)
        external
        view
        virtual
        returns (address, uint256)
    {
        return (address(this), _calculateRoyalty(_salePrice));
    }

    function _calculateRoyalty(uint256 _salePrice) view private returns (uint256) {
        return (_salePrice / 10000) * royaltyFeesInBips;
    }

    function getBalance() public view returns(uint) {
        return address(this).balance;
    }

}
