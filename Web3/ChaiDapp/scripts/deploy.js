
const hre = require("hardhat");

async function main() {

  
  const chai = await hre.ethers.deployContract("Chai");
  await chai.waitForDeployment();

  console.log(
    "Developing",chai.address
  );
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
