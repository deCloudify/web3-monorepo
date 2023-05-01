// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;

/// @title Core Storage Contract
/// @author Dhruv Malik
/// @notice this contract acts as the core interface of the generated notifications and the wormwhole bridge contract on the corresponding chain 
/// for instance allowing creation of the notification
/// @dev This contract is meant to be inherited only by the admin and corresponding communication protocol.


// this is used for defining the fees  paid by the user to create channel and approve specific operation.
struct UserFeesInfo {
uint256 totalFeesInvested;
uint256 lastTimeFeesInvested;  
}

// this defines the chains the user is subscribed (using CAIP_2 format) and the corresponding stats of subscription (in order to extract fees).
struct SubscriptionInfo {
string namespace;
string referrence;
uint256 operationsSubscribed;

}

contract CoreStorage {

// state variables hashes for function interfaces of EIP712 & creating new notif channel

bytes32 public constant DOMAIN_TYPEHASH = keccak256("EIP712Domain(string name,uint256 chainId,address verifyingContract)");
bytes32 public constant CREATE_NOTIF_TYPEHASH = keccak256("CreateNotifChannel(ChannelType channelType, bytes identity, uint256 amount, uint256 channelExpiryTime, uint256 nonce, uint256 expiry)");

// mapping struct storing the state of all the functions in notification.

mapping(address => uint256) public nonces; // defines the number of channels active by the user for the corresponding chain.
mapping(address => uint256) public channelUpdateCounter;
mapping(address => uint256) public userFeesClaimed;
mapping(address => UserFeesInfo) public userFeesInfo;

// now handling the information corresponding to the wormwhole details.

address public wormholeAddress;
address public paymasterAddress; // this is the address of the paymaster contract which pays the fees for the operations submitted by user (via AA).


}
