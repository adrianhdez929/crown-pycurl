import json
from io import BytesIO
from pycurl import Curl


# Base curl client, with initial parameters for Crown
class Client():
    def __init__(self, user, passwd, host, testnet=False):
        self.req_buffer = BytesIO()
        self.client = Curl()
        self.set_headers(user, passwd, host, testnet=testnet)

    # Sets the connection headers
    def set_headers(self, user, passwd, host, testnet=False):
        if testnet:
            self.client.setopt(self.client.PORT, 19341)    
            self.client.setopt(self.client.URL, 'http://'+user+':'+passwd+'@'+host+':19341')
        else:
            self.client.setopt(self.client.PORT, 9341)
            self.client.setopt(self.client.URL, 'http://'+user+':'+passwd+'@'+host+':9341')
        
        self.client.setopt(self.client.ENCODING, '')
        self.client.setopt(self.client.MAXREDIRS, 10)
        self.client.setopt(self.client.TIMEOUT, 30)
        self.client.setopt(self.client.SSL_VERIFYHOST, 0)
        self.client.setopt(self.client.SSL_VERIFYPEER, 0)
        self.client.setopt(self.client.CUSTOMREQUEST, 'POST')
        self.client.setopt(self.client.HTTPHEADER, ["cache-control: no-cache","content-type: application/json","user: {0}:{1}".format \
                                                    (user, passwd),])
        self.client.setopt(self.client.WRITEDATA, self.req_buffer)

    # Execute the command set on 'method' with parameters 'params' as with the 'crown-cli' tool
    def execute(self, method, params=[]):
        self.client.setopt(self.client.POSTFIELDS, '{"jsonrpc": "1.0", "id": "crown-pycurl", "method": "%s", "params": %s}' % \
                                                    (method, params))
        print('{"jsonrpc": "1.0", "id": "crown-pycurl", "method": "%s", "params": %s}' % \
                                                    (method, params))                          
        self.client.perform()
        # Returns a JSON object with the response
        return json.loads(self.req_buffer.getvalue().decode('utf-8'))

    # A set of commands implementations
    # == Blockchain == 
    # getbestblockhash
    def getbestblockhash(self):
        return self.execute('getbestblockhash')
    # getblock
    def getblock(self, hash, verbose=True):
        data = json.dumps([hash, verbose])
        return self.execute('getblock', data)
    # getblockchaininfo
    def getblockchaininfo(self):
        return self.execute('getbestblockhash')
    # getblockcount
    def getblockcount(self):
        return self.execute('getblockcount')
    # getblockhash
    def getblockhash(self, index):
        data =json.dumps([index])
        return self.execute('getblockhash', data)
    # getblockheader
    def getblockheader(self, hash, verbose):
        data = json.dumps([hash, verbose])
        return self.execute('getblockheader', data)
    # getchaintips
    def getchaintips(self):
        return self.execute('getchaintips')
    # getdifficulty
    def getdifficulty(self):
        return self.execute('getdifficulty')
    # getmempoolinfo
    def getmempoolinfo(self):
        return self.execute('getmempoolinfo')
    # getrawmempool
    def getrawmempool(self, verbose=False):
        data = json.dumps([verbose])
        return self.execute('getrawmempool', data)
    # gettxout
    def gettxout(self, txid, n, includemempool=False):
        data = json.dumps([txid, n, includemempool])
        return self.execute('gettxout', data)
    # gettxoutsetinfo
    def gettxoutsetinfo(self):
        return self.execute('gettxoutsetinfo')
    # verifychain
    def verifychain(self, checklevel=3, numblocks=288):
        data = json.dumps([checklevel, numblocks])
        return self.execute('verifychain', data)
    # == Control ==
    # getinfo
    def getinfo(self):
        return self.execute('getinfo')
    # help
    def help(self, command=None):
        data = json.dumps([command])
        return self.execute('help', data)
    # restart
    def restart(self):
        return self.execute('restart')
    # stop
    def stop(self):
        return self.execute('stop')
    # == Crown ==
    # getstakepointers
    def getstakepointers(self):
        return self.execute('getstakepointers')
    # masternode
    def masternode(self, command, passphrase=None):
        data = json.dumps([command, passphrase])
        return self.execute('masternode', data)
    # masternodebroadcast
    def masternodebroadcast(self, command, passphrase=None):
        data = json.dumps([command, passphrase])
        return self.execute('masternodebroadcast', data)
    # masternodelist
    def masternodelist(self, mode="status", filter=None):
        data = json.dumps([mode, filter])
        return self.execute('masternodelist', data)
    # mnbudget
    def mnbudget(self, command, passphrase=None):
        data = json.dumps([command, passphrase])
        return self.execute('mnbudget', data)
    # mnbudgetvoteraw
    # def mnbudgetvoteraw(self, mntxhash, mntxindex, prophash, vote, time, votesig):
    # Pending due lack of info
    # mnfinalbudget
    def mnfinalbudget(self, command, passphrase=None):
        data = json.dumps([command, passphrase])
        return self.execute('mnfinalbudget', data)
    # mnsync
    # Pending because it can be done manually
    # node
    def node(self, command, passphrase=None):
        data = json.dumps([command, passphrase])
        return self.execute('node', data)
    # snsync
    # Same as line 131
    # spork
    # Same as line 125
    # systemnode
    def systemnode(self, command, passphrase=None):
        data = json.dumps([command, passphrase])
        return self.execute('systemnode', data)
    # systemnodebroadcast
    def systemnodebroadcast(self, command, passphrase=None):
        data = json.dumps([command, passphrase])
        return self.execute('systemnodebroadcast', data)
    # systemnodelist
    def systemnodelist(self, mode="status", filter=None):
        data = json.dumps([mode, filter])
        return self.execute('systemnodelist', data)
