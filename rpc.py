from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import pandas as pd
import sqlite3


rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%('user', 'pass'))

block_hash=rpc_connection.getblockhash(10000)

print(rpc_connection.getblock(block_hash))
