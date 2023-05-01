// SPDX-License-Identifier: MIT

pragma solidity ^0.8.10;

/// @title Uniswap create pool contract.
/// @notice This contract is used to create a pool on uniswap v3 using the AA contract and wormwhole for crosschain operation (if needed).
/// @dev pattern taken from the defisaver contract.


import "../../../node_modules/@uniswap/v3-core/contracts/interfaces/callback/IUniswapV3FlashCallback.sol";
import '../../../node_modules/@uniswap/v3-core/contracts/libraries/LowGasSafeMath.sol';

import "../../../node_modules/@uniswap/v3-periphery/contracts/base/PeripheryPayments.sol";

import "../../interface/IWormhole.sol";




// for creation of pool.
struct Params {
  address token0;
  address token1;
  uint24 fee;
  int24 tickLower;
  int24 tickUpper;
  uint256 amount0Desired;
  uint256 amount1Desired;
  uint256 amount0Min;
  uint256 amount1Min;
  address recipient;
  uint256 deadline;
  address from;
  uint160 sqrtPriceX96;
}

contract UniswapActions is IUniswapV3FlashCallback, PeripheryPayments {




  




}