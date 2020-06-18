import json
from io import BytesIO
from pycurl import Curl


# Base curl client, with initial parameters for Crown
class Client():
    def __init__(self, user, passwd, host):
        self.req_buffer = BytesIO()
        self.client = Curl()
        self.client.setopt(self.client.PORT, 9341)
        self.client.setopt(self.client.URL, 'http://'+user+':'+passwd+'@'+host+':9341')
        self.client.setopt(self.client.ENCODING, '')
        self.client.setopt(self.client.MAXREDIRS, 10)
        self.client.setopt(self.client.TIMEOUT, 30)
        self.client.setopt(self.client.SSL_VERIFYHOST, 0)
        self.client.setopt(self.client.SSL_VERIFYPEER, 0)
        self.client.setopt(self.client.CUSTOMREQUEST, 'POST')
        self.client.setopt(self.client.HTTPHEADER, ["cache-control: no-cache","content-type: application/json","user: {0}:{1}".format(user, passwd),])
        self.client.setopt(self.client.WRITEDATA, self.req_buffer)

    # Execute the command set on 'method' with parameters 'params' as with the 'crown-cli' tool
    def execute(self, method, params):
        self.client.setopt(self.client.POSTFIELDS, '{"jsonrpc": "1.0", "id":"crwpycurl", "method": "{0}", "params": {1} }'.format(method, params))
        self.client.perform()
        # Returns a JSON object with the response
        return json.loads(self.req_buffer.getvalue().decode('utf-8'))
