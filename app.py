# imports
from flask import Flask, url_for, render_template, redirect # more imports can be added 
from bitcoin import * # ask peer about these imports
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# initializers
app = Flask(__name__)
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("username", "password")) # change username and password

@app.route('/')
def index():
    return "Index"

