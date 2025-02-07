# files for importing. will do nothing if runnred diractly.

## functions: all of my useful functions.
> (and some less useful)
### here is a list of some of them:
1. isnumber(value):
    checks if value can be converted to int.
2. get_gw():
    get the default gateway.
3. get_ip():
    get the ip address. if there isn't, return 127.0.0.1.

## WebsocketServer: a simple websocket server.
### main features :
1. automaticly calls the event functions.
2. simple client manager.
- sending messages: client().send(msg)
3. set event functions:
- server().set_fn_new_client(fn)
- server().set_fn_client_left(fn)
- server().set_fn_message_recived(fn)

# **important!**
**every reference of a pypackage module in any of my other repositorys is a mention to this repository.**

# installation :
1. functions:
> pip install https://erri4.github.io/package/filesforpip/functions-0.1.1-py3-none-any.whl

2. WebsocketServer:
> pip install https://erri4.github.io/package/filesforpip/WebsocketServer-0.1.4-py3-none-any.whl