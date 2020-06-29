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
        if command:
            data = json.dumps([command])
        else:
            data = json.dumps([])
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
        if passphrase:
            data = json.dumps([command, passphrase])
        else:
            data = json.dumps([command])
        return self.execute('masternode', data)
    # masternodebroadcast
    def masternodebroadcast(self, command, passphrase=None):
        if passphrase:
            data = json.dumps([command, passphrase])
        else:
            data = json.dumps([command])
        return self.execute('masternodebroadcast', data)
    # masternodelist
    def masternodelist(self, mode="status", filter=None):
        if filter:
            data = json.dumps([mode, filter])
        else:
            data = json.dumps([mode])
        return self.execute('masternodelist', data)
    # mnbudget
    def mnbudget(self, command, passphrase=None):
        if passphrase:
            data = json.dumps([command, passphrase])
        else:    
            data = json.dumps([command])
        return self.execute('mnbudget', data)
    # mnbudgetvoteraw
    # def mnbudgetvoteraw(self, mntxhash, mntxindex, prophash, vote, time, votesig):
    # Pending due lack of info
    # mnfinalbudget
    def mnfinalbudget(self, command, passphrase=None):
        if passphrase:
            data = json.dumps([command, passphrase])
        else:
            data = json.dumps([command])
        return self.execute('mnfinalbudget', data)
    # mnsync
    # Pending because it can be done manually
    # node
    def node(self, command, passphrase=None):
        if passphrase:
            data = json.dumps([command, passphrase])
        else:
            data = json.dumps([command])
        return self.execute('node', data)
    # snsync
    # Same as line 131
    # spork
    # Same as line 125
    # systemnode
    def systemnode(self, command, passphrase=None):
        if passphrase:
            data = json.dumps([command, passphrase])
        else:
            data = json.dumps([command])
        return self.execute('systemnode', data)
    # systemnodebroadcast
    def systemnodebroadcast(self, command, passphrase=None):
        if passphrase:
            data = json.dumps([command, passphrase])
        else:
            data = json.dumps([command])
        return self.execute('systemnodebroadcast', data)
    # systemnodelist
    def systemnodelist(self, mode="status", filter=None):
        if filter:
            data = json.dumps([mode, filter])
        else:
            data = json.dumps([mode])
        return self.execute('systemnodelist', data)
    # == Generating ==
    # getauxblock
    def getauxblock(self, hash=None, auxpow=None):
        if hash and auxpow:
            data = json.dumps([hash, auxpow])
        else:
            return self.execute('getauxblock')
        return self.execute('getauxblock', data)
    # getgenerate
    def getgenerate(self):
        return self.execute('getgenerate')
    # gethashespersec
    def gethashespersec(self):
        return self.execute('gethashespersec')
    # setgenerate
    def setgenerate(self, generate, genproclimit=None):
        if genproclimit:
            data = json.dumps([generate, genproclimit])
        else:
            data = json.dumps([generate])
        return self.execute('setgenerate', data)
    # == Mining ==
    # getblocktemplate
    def getblocktemplate(self, jsonrequestobject=None):
        if jsonrequestobject:
            data = json.dumps([jsonrequestobject])
        else:
            return self.execute('getblocktemplate')
        return self.execute('getblocktemplate', data)
    # getmininginfo
    def getmininginfo(self):
        return self.execute('getmininginfo')
    # getnetworkhashps
    def getnetworkhashps(self, blocks=120, height=-1):
        data = json.dumps([blocks, height])
        return self.execute('getnetworkhashps', data)
    # prioritisetransaction
    def prioritisetransaction(self, txid, priority, fee):
        data = json.dumps([txid, priority, fee])
        return self.execute('prioritisetransaction', data)
    # submitblock
    def submitblock(self, hexdata, jsonparametersobject=None):
        if jsonparametersobject:
            data = json.dumps([hexdata, jsonparametersobject])
        else:
            data = json.dumps([hexdata])
        return self.execute('submitblock', data)
    # == Network ==
    # addnode
    def addnode(self, node, command):
        data = json.dumps([node, command])
        return self.execute('addnode', data)
    # getaddednodeinfo
    def getaddednodeinfo(self, dns, node=None):
        if node:
            data = json.dumps([dns, node])
        else:
            data = json.dumps([dns])
        print(data)
        return self.execute('getaddednodeinfo', data)
    # getconnectioncount
    def getconnectioncount(self):
        return self.execute('getconnectioncount')
    # getnettotals
    def getnettotals(self):
        return self.execute('getnettotals')
    # getnetworkinfo
    def getnetworkinfo(self):
        return self.execute('getnetworkinfo')
    # getpeerinfo 
    def getpeerinfo(self):
        return self.execute('getpeerinfo')
    # ping
    def ping(self):
        return self.execute('ping')
    # == Platform ==
    # agents
    # Same as line 140
    # nftoken
    def nftoken_issue(self, proto, id, owner, metadataAdmin='0', metadata=''):
        data = json.dumps(['issue', proto, id, owner, metadataAdmin, metadata])
        return self.execute('nftoken', data)
    def nftoken_get(self, proto, id):
        data = json.dumps(['get', proto, id])
        return self.execute('nftoken', data)
    def nftoken_getbytxid(self, txid):
        data = json.dumps(['getbytxid', txid])
        return self.execute('nftoken', data)
    def nftoken_totalsupply(self, proto):
        data = json.dumps(['totalsupply', proto])
        return self.execute('nftoken', data)
    def nftoken_balanceof(self, address, proto=None):
        if proto:
            data = json.dumps(['balanceof', address, proto])
        else:
            data = json.dumps(['balanceof', address])
        return self.execute('nftoken', data)
    def nftoken_ownerof(self, proto, id):
        data = json.dumps(['ownerof', proto, id])
        return self.execute('nftoken', data)
    def nftoken_list(self, proto=None, address=None, count=None, skip=None, height=None, rgtxonly=False):
        args = ['list']
        if proto:
            args.append(proto)
        if address:
            args.append(address)
        if count:
            args.append(count)
        if skip:
            args.append(skip)
        if height:
            args.append(height)
        if rgtxonly:
            args.append(rgtxonly)
        data = json.dumps(args)
        print(data)
        return self.execute('nftoken', data)
    # nftproto
    # == Rawtransactions == 
    # createrawtransaction
    def createrawtransaction(self, transactions, addresses):
        data = json.dumps([transactions, addresses])
        return self.execute('createrawtransaction', data)
    # decoderawtransaction
    def decoderawtransaction(self, hex):
        data = json.dumps([hex])
        return self.execute('decoderawtransaction', data)
    # decodescript
    def decodescript(self, hex):
        data = json.dumps([hex])
        return self.execute('decodescript')
    # getrawtransaction
    def getrawtransaction(self, txid, verbose=0):
        data = json.dumps([txid, verbose])
        return self.execute('getrawtransaction', data)
    # sendrawtransaction
    def sendrawtransaction(self, hex, allowhighfees=False):
        data = json.dumps([hex, allowhighfees])
        return self.execute('sendrawtransaction', data)
    # == Utils ==
    # createmultisig
    def createmultisig(self, nrequired, keys):
        data = json.dumps([nrequired, keys])
        return self.execute('createmultisig', data)
    # estimatefee
    def estimatefee(self, nblocks):
        data = json.dumps([nblocks])
        return self.execute('estimatefee', data)
    # estimatepriority
    def estimatepriority(self, nblocks):
        data = json.dumps([nblocks])
        return self.execute('estimatepriority', data)
    # validateaddress
    def validateaddress(self, address):
        data = json.dumps([address])
        return self.execute('validateaddress', data)
    # verifymessage
    def verifymessage(self, address, signature, message):
        data = json.dumps([address, signature, message])
        return self.execute('verifymessage', data)
