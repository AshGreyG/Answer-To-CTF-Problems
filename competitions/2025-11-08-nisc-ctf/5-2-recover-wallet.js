// Mnemonic: ankle assume estate permit (???) eye fancy spring demand dial awkward hole
// Ethereum Address: 0x**********************************700f80

const bip39 = require("bip39");
const { hdkey } = require("ethereumjs-wallet");

async function wrapper() {
  const mnemonicPart1 = "ankle assume estate permit ";
  const mnemonicPart2 = " eye fancy spring demand dial awkward hole";

  for (const word of bip39.wordlists.english) {
    const mnemonic = mnemonicPart1 + word + mnemonicPart2;
    const seed = await bip39.mnemonicToSeed(mnemonic, "");
    const hdWallet = hdkey.fromMasterSeed(seed);

    const wallet = hdWallet.derivePath("m/44'/60'/0'/0/0").getWallet();
    const ethAddress = wallet.getAddressString();

    if (ethAddress.endsWith("700f80")) {
      console.log(word);
      console.log(ethAddress);
    }
  }
}

wrapper()

// gallery
// 0x7e93e8eeeee122abf300904ebc446d31d8700f80
