from web3 import Web3

# Call the API using the API url and store the connection in a variable
API_URL = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 =  Web3( Web3.HTTPProvider(API_URL))

# Define a function to get the gas price from the API
def getGasPrices():
    try:
        gasPrices={}
        gweiPrices={}
        etherPrices={}
        dollarPrices={}

        # Retrieve the current gas price from the API and store it in a variable.
        gasPrices["current"] =  web3.eth.gas_price


        # Convert the gas prices as per their speed and store it.
        gasPrices["slow"] =   int(gasPrices["current"] * 0.9) 
        gasPrices["standard"] = int(gasPrices["current"] * 1.0) 
        gasPrices["fast"] = int(gasPrices["current"] * 1.1)     
        gasPrices["rapid"] = int(gasPrices["current"] * 1.2)
        
        # Convert gas prices from Wei to Gwei
        gweiPrices["current"] = web3.from_wei(gasPrices["current"], 'gwei')
        gweiPrices["slow"] = web3.from_wei(gasPrices["slow"], 'gwei')
        gweiPrices["standard"] = web3.from_wei(gasPrices["standard"], 'gwei')
        gweiPrices["fast"] = web3.from_wei(gasPrices["fast"], 'gwei')
        gweiPrices["rapid"] = web3.from_wei(gasPrices["rapid"], 'gwei')
        
        # Conversion of gas price into ether
        etherPrices["current"] = web3.from_wei(gasPrices["current"], 'ether')
        etherPrices["slow"] = web3.from_wei(gasPrices["slow"], 'ether')
        etherPrices["standard"] = web3.from_wei(gasPrices["standard"], 'ether')
        etherPrices["fast"] = web3.from_wei(gasPrices["fast"], 'ether')
        etherPrices["rapid"] = web3.from_wei(gasPrices["rapid"], 'ether')

        # Conversion of gas price into ether to dollars
        conversionRate = 1826.33
        dollarPrices["current"] = etherPrices["current"] * int(conversionRate)
        dollarPrices["slow"] = etherPrices["slow"] * int(conversionRate)
        dollarPrices["standard"] = etherPrices["standard"] * int(conversionRate)
        dollarPrices["fast"] = etherPrices["fast"] * int(conversionRate)
        dollarPrices["rapid"] =  etherPrices["rapid"] * int(conversionRate)

        return gasPrices, gweiPrices, etherPrices, dollarPrices

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None
