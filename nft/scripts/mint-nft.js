//step 1: You define your variables from .env file
require('dotenv').config();
const API_URL = process.env.API_URL;
const PUBLIC_KEY = process.env.PUBLIC_KEY;
const PRIVATE_KEY = process.env.PRIVATE_KEY;

const { createAlchemyWeb3 } = require("@alch/alchemy-web3");
const web3 = createAlchemyWeb3(API_URL);

//sleep function
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

//step 2: Define our contract ABI (Application Binary Interface) & adresses

const contract = require("../artifacts/contracts/SacredBodiesNFT.sol/SacredBodiesNFT.json");
const contractAddress = "0xb5493C39B6a2A7Fc7ddDD874dE0d73d586De3666";
const nftContract = new web3.eth.Contract(contract.abi, contractAddress);

//step 3: Define the minting function
async function mintNFT(tokenURI) {
  const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY, 'latest'); //get latest nonce

  //the transaction
  const tx = {
    'from': PUBLIC_KEY,
    'to': contractAddress,
    'nonce': nonce,
    'gas': 500000,
    'maxPriorityFeePerGas': 1999999987,
    'data': nftContract.methods.mintNFT(PUBLIC_KEY, tokenURI).encodeABI()
  };

  //step 4: Sign the transaction
  const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);
  const transactionReceipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

  console.log(`Transaction receipt: ${JSON.stringify(transactionReceipt)}`);

  return nonce;
}

//step 5: Call the mintNFT function
var startID = 5;
const whileLoop = async _ => {
  while (startID < 1000) {
    var oldNonce = await web3.eth.getTransactionCount(PUBLIC_KEY, 'latest');
    var newNonce = oldNonce;
    mintNFT(`https://gateway.pinata.cloud/ipfs/QmVpLSoYak1N8pasuxLrNZLbnvrNvLTJmY8ncMBjNRPBtQ/${startID}.json`);
    startID = startID + 1;
    console.log(`Old nonce: ${oldNonce}. New nonce: ${newNonce}.`);
    console.log("Waiting for transactions to clear and show up on the chain...");
    while (oldNonce === newNonce) {
      await sleep(50000);
      newNonce = await web3.eth.getTransactionCount(PUBLIC_KEY, 'latest');
      if (oldNonce !== newNonce) {
        console.log(`New nonce: ${newNonce}`);
        console.log("New nonce is different, attempting to mint the next NFT...");
      } else {
        console.log(`New nonce: ${newNonce}`);
        console.log("New nonce is the same as the old, retrying in a few seconds...");
      }
    }
  }
}

whileLoop();