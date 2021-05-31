# Generate Bitcoin Wallet
The goal of this library is to generate private keys and create Bitcoin wallet addresses from them.

*Note: this is a lightly modified version of Timur Badretdinov's fantastic [Blocksmith library](https://github.com/Destiner/blocksmith). I've simply commented out anything referencing the Ethereum module, changed the output formatting, renamed a few things, and added support for command line user input.*

**Run the following commands:**
```
pipenv install
python main.py
```

**When prompted, mash your keyboard in order to generate the requisite entropy. Hit enter when finished.**

## TO DO

Write tool to convert hex encoded private key to WIF