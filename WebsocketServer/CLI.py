import code
import sys
import argparse
import WebsocketServer as ws


def new_client(client):
    print('a new client connected')


def client_left(client):
    print('a client left')


def message_received(client, msg):
    print(f'a client sent: {msg}')


def main():
    parser = argparse.ArgumentParser(description="Start a WebSocket server.",
                                     usage='''\n
websocketserver myserver 127.0.0.1 5001
>>>from mymodule import new_client, message_received, client_left
>>>myserver.set_fn_client_left(client_left)
>>>myserver.set_fn_message_received(message_received)
>>>myserver.set_fn_new_client(new_client)
>>>server.start()
server running on 127.0.0.1:5001...
                                    ''')
    parser.add_argument('server_name', type=str, help="The name of the server instance (e.g., 'MyServer').")
    parser.add_argument('host', help="The host address for the WebSocket server.")
    parser.add_argument('port', type=int, help="The port number for the WebSocket server.")
    args = parser.parse_args()
    server_name = args.server_name
    host = args.host
    port = args.port
    globals()[server_name] = ws.WebsocketServer(host, port)
    globals()[server_name].set_fn_client_left(client_left)
    globals()[server_name].set_fn_message_received(message_received)
    globals()[server_name].set_fn_new_client(new_client)
    banner = f"python {sys.version} on {sys.platform}\nImporting WebsocketServer..."
    console = code.InteractiveConsole(locals=globals())
    console.interact(banner=banner)
