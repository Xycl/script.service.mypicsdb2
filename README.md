# script.service.mypicsdb


## Automatically updates MyPicsDB

You can call itover JSON-RPC:
invoke-webrequest -uri 192.168.0.10/jsonrpc?request='{"jsonrpc":"2.0","id":1,"method":"Addons.ExecuteAddon","params":{"addonid" : "script.service.mypicsdb"}}'