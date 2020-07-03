import json
from io import BytesIO
from pycurl import Curl


# Base curl client, with initial parameters for Crown
class Client():
    def __init__(self, user, passwd, host, testnet=False):
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

    # Execute the command set on 'method' with parameters 'params' as with the 'crown-cli' tool
    def execute(self, method, params=[]):
        # Instantiates the buffer just before the request to perform multiple requests per object
        req_buffer = BytesIO()
        # Sets the local buffer to be where the request data is written
        self.client.setopt(self.client.WRITEDATA, req_buffer)
        self.client.setopt(self.client.POSTFIELDS, '{"jsonrpc": "1.0", "id": "crown-pycurl", "method": "%s", "params": %s}' % \
                                                    (method, params))
        print('{"jsonrpc": "1.0", "id": "crown-pycurl", "method": "%s", "params": %s}' % \
                                                    (method, params))                          
        self.client.perform()
        # Returns a JSON object with the response
        return json.loads(req_buffer.getvalue().decode('utf-8'))
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
        return self.execute('getblockchaininfo')
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
    def nftoken_list(self, proto=None, address=None, count=None, skip=None, height=None, regtxonly=False):
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
        if regtxonly:
            args.append(regtxonly)
        data = json.dumps(args)
        return self.execute('nftoken', data)
    # nftproto
    def nftproto_register(self, id, name, owner, sign=2, mimetype='text/plain', schemauri='', transferable=True, embedded=False, size=255):
        data = json.dumps(['register', id, name, owner, sign, mimetype, schemauri, transferable, embedded, size])
        return self.execute('nftproto', data)
    def nftproto_list(self, count=None, skip=None, height=None, regtxonly=False):
        args = ['list']
        if count:
            args.append(count)
        if skip:
            args.append(skip)
        if height:
            args.append(height)
        if regtxonly:
            args.append(regtxonly)
        data = json.dumps(args)
        return self.execute('nftproto', data)
    def nftproto_get(self, id):
        data = json.dumps(['get', id])
        return self.execute('nftproto', data)
    def nftproto_getbytxid(self, txid):
        data = json.dumps(['getbytxid', txid])
        return self.execute('nftproto', data)
    def nftproto_ownerof(self, proto):
        data = json.dumps(['ownerof', proto])
        return self.execute('nftproto', data)
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
        return self.execute('decodescript', data)
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
    # == Wallet ==
    # addmultisigaddress
    def addmultisigaddress(self, nrequired, keysobject, account=None):
        if account:
            data = json.dumps([nrequired, keysobject, account])
        else:
            data = json.dumps([nrequired, keysobject])
        return self.execute('addmultisigaddress', data)
    # backupwallet
    def backupwallet(self, destination):
        data = json.dumps([destination])
        return self.execute('backupwallet', data)
    # convertaddress
    def convertaddress(self, oldaddress):
        data = json.dumps([oldaddress])
        return self.execute('convertaddress', data)
    # dumpprivkey
    def dumpprivkey(self, address):
        data = json.dumps([address])
        return self.execute('dumpprivkey', data)
    # dumpwallet
    def dumpwallet(self, filename):
        data = json.dumps([filename])
        return self.execute('dumpwallet', data)
    # encryptwallet
    def encryptwallet(self, passphrase):
        data = json.dumps([passphrase])
        return self.execute('encryptwallet', data)
    # getaccount
    def getaccount(self, address):
        data = json.dumps([address])
        return self.execute('getaccount', data)
    # getaccountaddress
    def getaccountaddress(self, account):
        data = json.dumps([account])
        return self.execute('getaccountaddress', data)
    # getaddressesbyaccount
    def getaddressesbyaccount(self, account):
        data = json.dumps([account])
        return self.execute('getaddressesbyaccount', data)
    # getbalance
    def getbalance(self, account=None, minconf=None, includewatchonly=None):
        args = []
        if account:
            args.append(account)
        if minconf:
            args.append(minconf)
        if includewatchonly:
            args.append(includewatchonly)
        data = json.dumps(args)
        return self.execute('getbalance', data)
    # getnewaddress
    def getnewaddress(self, account=None):
        if account:
            data = json.dumps([account])
            return self.execute('getnewaddress', data) 
        return self.execute('getnewaddress')
    # getrawchangeaddress
    def getrawchangeaddress(self):
        return self.execute('getrawchangeaddress')
    # getreceivedbyaccount
    def getreceivedbyaccount(self, account, minconf=None):
        if minconf:
            data = json.dumps([account, minconf])
        else:
            data = json.dumps([account])
        return self.execute('getreceivedbyaccount', data)
    # getreceivedbyaddress
    def getreceivedbyaddress(self, address, minconf=None):
        if minconf:
            data = json.dumps([address, minconf])
        else:
            data = json.dumps([address])
        return self.execute('getreceivedbyaddress', data)
    # gettransaction 
    def gettransaction(self, txid, includewatchonly=None):
        if includewatchonly:
            data = json.dumps([txid, includewatchonly])
        else:
            data = json.dumps([txid])
        return self.execute('gettransaction', data)
    # getunconfirmedbalance
    def getunconfirmedbalance(self):
        return self.execute('getunconfirmedbalance')
    # getwalletinfo
    def getwalletinfo(self):
        return self.execute('getwalletinfo')
    # importaddress
    def importaddress(self, address, label='', rescan=True):
        data = json.dumps([address, label, rescan])
        return self.execute('importaddress', data)
    # importprivkey
    def importprivkey(self, privkey, label='', rescan=True):
        data = json.dumps([privkey, label, rescan])
        return self.execute('importprivkey', data)
    # importwallet 
    def importwallet(self, filename):
        data = json.dumps([filename])
        return self.execute('importwallet', data)
    # keypoolrefill
    def keypoolrefill(self, newsize=100):
        data = json.dumps([newsize])
        return self.execute('keypoolrefill', data)
    # listaccounts
    def listaccounts(self, minconf=None, includewatchonly=None):
        args = []
        if minconf:
            args.append(minconf)
        if includewatchonly:
            args.append(includewatchonly)
        data = json.dumps(args)
        return self.execute('listaccounts', data)
    # listaddressgroupings
    def listaddressgroupings(self):
        return self.execute('listaddressgroupings')
    # listlockunspent
    def listlockunspent(self):
        return self.execute('listlockunspent')
    # listreceivedbyaccount
    def listreceivedbyaccount(self, minconf=None, includeempty=None, includewatchonly=None):
        args = []
        if minconf:
            args.append(minconf)
        if includeempty:
            args.append(includeempty)
        if includewatchonly:
            args.append(includewatchonly)
        data = json.dumps(args)
        return self.execute('listreceivedbyaccount', data)
    # listreceivedbyaddress
    def listreceivedbyaddress(self, minconf=None, includeempty=None, includewatchonly=None):
        args = []
        if minconf:
            args.append(minconf)
        if includeempty:
            args.append(includeempty)
        if includewatchonly:
            args.append(includewatchonly)
        data = json.dumps(args)
        return self.execute('listreceivedbyaddress', data)
    # listsinceblock
    def listsinceblock(self, blockhash, confirmations=None, includewatchonly=None):
        args = [blockhash]
        if confirmations:
            args.append(confirmations)
        if includewatchonly:
            args.append(includewatchonly)
        data = json.dumps(args)
        return self.execute('listsinceblock', data)
    # listtransactions
    def listtransactions(self, account=None, count=None, skip=None, includewatchonly=None):
        args = []
        if account:
            args.append(account)
        if count:
            args.append(count)
        if skip:
            args.append(skip)
        if includewatchonly:
            args.append(includewatchonly)
        data = json.dumps(args)
        return self.execute('listtransactions', data)
    # listunspent
    def listunspent(self, minconf=1, maxconf=9999999, addresses=None):
        if addresses:
            data = json.dumps([minconf, maxconf, addresses])
        else:
            data = json.dumps([minconf, maxconf])
        return self.execute('listunspent', data)
    # lockunspent
    def lockunspent(self, unlock, transactions):
        data = json.dumps([unlock, transactions])
        return self.execute('lockunspent', data)
    # move
    def move(self, fromaccount, toaccount, minconf=1, comment=''):
        data = json.dumps([fromaccount, toaccount, minconf, comment])
        return self.execute('move', data)
    # sendfrom
    def sendfrom(self, fromaccount, toaddress, amount, minconf=1, comment='', commentto=''):
        data = json.dumps([fromaccount, toaddress, amount, minconf, comment, commentto])
        return self.execute('sendfrom', data)
    # sendmany
    def sendmany(self, fromaccount, addresses, minconf=1, comment=''):
        data = json.dumps([fromaccount, addresses, minconf, comment])
        return self.execute('sendmany', data)
    # sendtoaddress
    def sendtoaddress(self, address, amount, comment='', commentto=''):
        data = json.dumps([address, amount, comment, commentto])
        return self.execute('sendtoaddress', data)
    # sendtoaddressix
    def sendtoaddressix(self, address, amount, comment='', commentto=''):
        data = json.dumps([address, amount, comment, commentto])
        return self.execute('sendtoaddressix', data)
    # setaccount
    def setaccount(self, address, account):
        data = json.dumps([address, account])
        return self.execute('setaccount', data)
    # settxfee
    def settxfee(self, amount):
        data = json.dumps([amount])
        return self.execute('settxfee', data)
    # signmessage
    def signmessage(self, address, message):
        data = json.dumps([address, message])
        return self.execute('signmessage', data)
    # update
    def update(self, command, passphrase=None):
        if passphrase:
            data = json.dumps([command, passphrase])
        else:
            data = json.dumps([command])
        return self.execute('update', data)
