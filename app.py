# imports
from flask import Flask, url_for, render_template, redirect # more imports can be added 
# from bitcoin import * 
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# initializers
app = Flask(__name__)
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("username", "password")) # change username and password


@app.route('/')
def index():
    return "Index use / then (get command) to get the command"
@app.route('/<command>')
def cmd(command):
    result = rpc_connection.batch_([["call_function", command]])
    return result

