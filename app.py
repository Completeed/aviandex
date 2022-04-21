# imports
from flask import Flask, url_for, render_template, redirect # more imports can be added 
from bitcoin import * # ask peer about these imports
# from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# initializers
app = Flask(__name__)
# def connect_to_bitcoind_rpc(self):
#         for i in range(1,settings.rcp_reconnect_max_retry+1):
#             try:
#                 self.proxy = bitcoin.rpc.Proxy()
#                 return
#             except http.client.HTTPException:
#                 print("Caught a connection error from Bitcoind RCP, Reconnecting...(%d/%d)" %(i,settings.rcp_reconnect_max_retry)) 
# Peer can set this up, not sure how to

@app.route('/')
def index():
    return "Index"

