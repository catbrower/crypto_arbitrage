require('dotenv').config();

const { ethers } = require('ethers');
const UniswapV2Pair = require('./abis/IUniswapV2Pair.json');
const UniswapV2Factory = require('./abis/IUniswapV2Factory.json');
const provider = new ethers.providers.InfuraProvider('ropsten', process.env.PROJECT_ID);

const privateKey = process.env.PRIVATE_KEY
const wallet = new ethers.Wallet(privateKey, provider);

const runBot = async() => {

}

