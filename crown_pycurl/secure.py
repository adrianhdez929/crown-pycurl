import subprocess
from threading import Thread
from sshtunnel import SSHTunnelForwarder as SSHTunnel

from .client import Client


class SecureClient(Client):
    def __init__(self, rpc_user, rpc_passwd, local_port, remote_port, remote_user, remote_passwd, remote_host, testnet=False):
        # Creates an SSH connection to the RPC host and forwards it into a designed port on your local machine
        self.sshtunnel = SSHTunnel(
            (remote_host, 22), 
            ssh_username=remote_user, 
            ssh_password=remote_passwd,
            remote_bind_address=(remote_host, remote_port),
            local_bind_address=('127.0.0.1', local_port)
        )
        self.sshtunnel.start()
        Client.__init__(self, rpc_user, rpc_passwd, '127.0.0.1:{0}'.format(str(local_port)), testnet)
        self.set_secure_headers(rpc_user, rpc_passwd, local_port)

    # Object destructor, closes the SSHTunnel
    def __del__(self):
        self.sshtunnel.stop()

    # Kind of an override of set_headers in parent, but this time to only set request URL to the local forwarded address
    def set_secure_headers(self, user, passwd, port):
        self.client.setopt(self.client.PORT, port)
        self.client.setopt(self.client.URL, 'http://'+user+':'+passwd+'@127.0.0.1:'+str(port))
