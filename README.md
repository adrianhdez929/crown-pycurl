# crown-pycurl

A simple python lib to interact with CRW nodes RPC using curl

## Usage:

Example:

    from crown_pycurl.client import Client

    # Set your RPC access info
    RPCUSER = 'your-rpc-user'
    RPCPASS = 'your-rpc-passwd'
    RPCHOST = 'your-rpc-host'

    # Create a new instance of the client with the access info
    client = Client(RPCUSER, RPCPASS, RPCHOST)

    # Configure the method to call and the params, both as string
    method = 'getinfo'
    params = '[]'

    # Execute the request
    client.execute(method, params)


