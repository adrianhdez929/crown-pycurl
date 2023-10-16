# crown-pycurl

A simple python lib to interact with CRW nodes RPC using curl

## Usage:

### Standard Client

Example:

    from crown_pycurl.client import Client

    # Set your RPC access info
    RPCUSER = 'your-rpc-user'
    RPCPASS = 'your-rpc-passwd'
    RPCHOST = 'your-rpc-host'
    RPCPORT = 9341

    # Create a new instance of the client with the access info
    client = Client(RPCUSER, RPCPASS, RPCHOST, RPCPORT) # To use testnet just add a fourth boolean parameter as True

    # Then just find the cli command you want to execute (in this example getinfo)
    response = client.getinfo()

    # The response is a JSON object with the same format as the crown-cli response
    print(response['result'])


### Secure Client

This is a beta feature, so it has been tested, but it still may have errors, so any feedback is very appreciated

Example:

    import os
    from crown_pycurl.secure import SecureClient

    # Set your RPC access info
    RPCUSER = 'your-rpc-user'
    RPCPASS = 'your-rpc-passwd'
    RPCHOST = 'your-rpc-host'
    RPCPORT = 9341

    # Get your node SSH login data from environment
    SSHUSER = os.environ.get(SSH_USER)
    SSHPASS = os.environ.get(SSH_PASS)
    SSHPORT = 21

    # Set the local port to forward the SSH tunnel
    LOCAL_PORT = 8000 

    # Create a new instance of the client with the rpc access info and your ssh login data
    client = SecureClient(RPCUSER, RPCPASS, LOCAL_PORT, SSHPORT, SSHUSER, SSHPASS, RPCHOST, RPCPORT) # For testnet add the boolean param

    # Execute the desired cli command just as in the standard client
    response = client.getinfo()

    # The response is a JSON object with the same format as the crown-cli response
    print(response['result'])
