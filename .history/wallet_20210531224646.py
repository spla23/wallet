# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
# YOUR CODE HERE
 
 
# Create a function called `derive_wallets`
# Use the subprocess library to create a shell command that calls the ./derive script from Python. 
# Make sure to properly wait for the process. Windows Users may need to prepend the php command in front of ./derive like so: php ./derive.
# The following flags must be passed into the shell command as variables:
# Mnemonic (--mnemonic) must be set from an environment variable, or default to a test mnemonic
# Coin (--coin)
# Numderive (--numderive) to set number of child keys generated
# Format (--format=json) to parse the output into a JSON object using json.loads(output)
# You should now be able to select child accounts (and thus, private keys) by accessing items in the coins dictionary like so: coins[COINTYPE][INDEX]['privkey'].

def derive_wallets(mnemonic, coin, numderive):
    command = php ./derive -g --mnemonic="{mnemonic}" --numderive="{numderive}" --coin="{coin}" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return  keys

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {"eth", "btc-test", "btc"}
numderive = 3
keys = {}
for coin in coins:
    keys[coin]= derive_wallets(os.getenv('mnemonic'), coin, numderive=3)

eth_PrivateKey = keys["eth"][0]['privkey']
btc_PrivateKey = keys['btc-test'][0]['privkey']

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
#This function will convert the privkey string in a child key to an account object that bit or web3.py can use to transact.
#This function needs the following parameters:
#coin -- the coin type (defined in constants.py).
#priv_key -- the privkey string will be passed through here.
#You will need to check the coin type, then return one of the following functions based on the library:
#For ETH, return Account.privateKeyToAccount(priv_key)
# This function returns an account object from the private key string. You can read more about this object here.
#For BTCTEST, return PrivateKeyTestnet(priv_key)
#This is a function from the bit libarary that converts the private key string into a WIF (Wallet Import Format) object. WIF is a special format bitcoin uses to designate the types of keys it generates.
#You can read more about this function here.

def priv_key_to_account(coin, priv_key):
    # YOUR CODE HERE

    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
eth_acc = priv_key_to_account(ETH,eth_PrivateKey)
btc_acc = priv_key_to_account(BTCTEST,btc_PrivateKey)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
# This function will create the raw, unsigned transaction that contains all metadata needed to transact.
#This function needs the following parameters:
#coin -- the coin type (defined in constants.py).
#account -- the account object from priv_key_to_account.
#to -- the recipient address.
#amount -- the amount of the coin to send.
#You will need to check the coin type, then return one of the following functions based on the library:
#For ETH, return an object containing to, from, value, gas, gasPrice, nonce, and chainID.
#Make sure to calculate all of these values properly using web3.py!
#For BTCTEST, return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def create_tx(coin, account, recipient, amount):
    global tx_data
    if coin ==ETH:
        gasEstimate = w3.eth.estimateGas(
           {"from": account.address, "to": recipient, "value": amount}
        )
        tx_data = {
            "to": recipient,
            "from": account.address,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)
        }
        return tx_data
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)]) 

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
#This function will call create_tx, sign the transaction, then send it to the designated network.


#This function needs the following parameters:


#coin -- the coin type (defined in constants.py).

#account -- the account object from priv_key_to_account.

#to -- the recipient address.

#amount -- the amount of the coin to send.



#You may notice these are the exact same parameters as create_tx. send_tx will call create_tx, so it needs all of this information available.


#You will need to check the coin, then create a raw_tx object by calling create_tx. Then, you will need to sign the raw_tx using bit or web3.py (hint: the account objects have a sign transaction function within).


#Once you've signed the transaction, you will need to send it to the designated blockchain network.

#For ETH, return w3.eth.sendRawTransaction(signed.rawTransaction)

#For BTCTEST, return NetworkAPI.broadcast_tx_testnet(signed)

def send_tx(coin, account, recipient, amount):
    # YOUR CODE HERE
    if coin == "eth": 
        trx_eth = create_trx(coin,account, recipient, amount)
        sign = account.signTransaction(trx_eth)
        result = w3.eth.sendRawTransaction(sign.rawTransaction)
        print(result.hex())
        return result.hex()
    else:
        trx_btctest= create_trx(coin,account,recipient,amount)
        sign_trx_btctest = account.sign_transaction(trx_btctest)
        from bit.network import NetworkAPI
        NetworkAPI.broadcast_tx_testnet(sign_trx_btctest)       
        return sign_trx_btctest
