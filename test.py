from crown_pycurl.client import Client
from crown_pycurl.secure import SecureClient
import os

#cl = Client('dfg45g45wrty6hhgg4ggbdfgdfgbsdfghfgfrw5454434343ttt', 'r9rwe56779h65hhth4f432dcb57j76j6mh54gj65j5trhfgbhgbeg', '92.60.46.21', True)
sc = SecureClient('dfg45g45wrty6hhgg4ggbdfgdfgbsdfghfgfrw5454434343ttt', 'r9rwe56779h65hhth4f432dcb57j76j6mh54gj65j5trhfgbhgbeg',\
                   8000, 9341, 'root', 'B&A8]L&JCj', '92.60.46.21', False)
#print(cl.nftproto_list())
#print(cl.nftproto_get('cubantest'))
#print(cl.getinfo())
print(sc.getinfo())
print(sc.getinfo())
