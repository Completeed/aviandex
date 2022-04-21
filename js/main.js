const http = require("http");
var bitcore = require('bitcore');
var RpcClient = require('bitcoind-rpc');
var fs = require('fs')
// config for bitcoinRPC
var config = {
    protocol: 'http',
    user: 'user',
    pass: 'pass',
    host: '127.0.0.1',
    port: '18332',
  };
var rpc = new RpcClient(config);
var server = http.createServer(function (res, req){
    // create server
    if (req.url == '/'){
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write('Hi');
        res.end()
    }
});
server.listen(5000)
