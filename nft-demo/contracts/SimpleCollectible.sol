// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

// Storing entire images on chain is super costly, more gas, more costly transactions.
// That's why we have metadata, token uri (unique id).
// If we are storing the image off chain, how it is decentralized?

// So there are a lot of different platforms which allows to store the data in
// decentralized way (e.g IPFS).
contract SimpleCollectible is ERC721 {
    uint256 public tokenCounter;

    constructor() public ERC721("SuperCat", "CAT") {
        tokenCounter = 0; // tokenId should be unique
    }

    function createCollectible() public returns (uint256) {
        uint256 newTokenId = tokenCounter;

        // _safeMint verifies that the tokenId is actually new and does not override the existing one
        _safeMint(msg.sender, newTokenId);
        ++tokenCounter;
        return newTokenId;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not onwer"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
