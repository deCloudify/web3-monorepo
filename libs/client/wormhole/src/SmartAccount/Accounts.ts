import { Client, Presets } from 'userop';
//import config from './config';
import { ethers } from 'ethers';

import * as dotenv from 'dotenv';
dotenv.config();

/**
 * This script will define the workflow for the execution of the swap and transfer of tokens from client.
 * here the client will be going through the following steps:
 * - create Account on the smart contract
 * - deposit multiple tokens in their smart account
 *    - encode the function calldata for multiple token transfer to the destination address
 *    - execute the transaction with paymaster doing the payment for the transaction.
 *
 *
 */

/**
 * function to initialize the client smart contract wallet account.
 *
 *
 */


interface MultiTokenRequest {
  sourceAddress: string[];
  SrcTokenDetails: Map<string, Map<string, number>> // accountAddress, tokenAddress, amount
  ChainId: number;
  destinationAddress: string;
  destinationTokenDetails: Map<string, number>
}


/**
 * fetches the tokens from the given token addresses (all of them have approved the token transfer)
 * 
 * 
 * 
 */

export async function FetchToken(
request: MultiTokenRequest
) {

}


export async function 