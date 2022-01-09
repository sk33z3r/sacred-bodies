async function main() {
    const SacredBodiesNFT = await ethers.getContractFactory("SacredBodiesNFT")

    // Start deployment, returning a promise that resolves to a contract object
    const SBT = await SacredBodiesNFT.deploy()
    console.log("Contract deployed to address:", SBT.address)
  }

  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error)
      process.exit(1)
    })