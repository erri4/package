import argparse
import importlib
import WebsocketServer as ws


def client_left(client):
    print('a client left.')


def new_client(client):
    print('a new client connected.')


def message_received(client, msg):
    print(f'a client sent: {msg}')


def main():
    global client_left
    global new_client
    global message_received
    host = '127.0.0.1'
    port = 5001
    parser = argparse.ArgumentParser(description="a simple command-line websocket server.")
    parser.add_argument('-H', '--host', type=str, help="", required=False)
    parser.add_argument('-p', '--port', type=int, help="", required=False)
    parser.add_argument('-new', '--new-client', type=str, help="", required=False)
    parser.add_argument('-new-mod', '--new-client-module', type=str, help="", required=False)
    parser.add_argument('-msg', '--message-received', type=str, help="", required=False)
    parser.add_argument('-msg-mod', '--message-received-module', type=str, help="", required=False)
    parser.add_argument('-left', '--client-left', type=str, help="", required=False)
    parser.add_argument('-left-mod', '--client-left-module', type=str, help="", required=False)
    args = parser.parse_args()
    if args.host:
        host = args.host
    if args.port:
        port = args.port
    if args.client_left:
        if args.client_left_module:
            try:
                module = importlib.import_module(args.client_left_module)
                client_left = getattr(module, args.client_left)
            except Exception as e:
                print(e)
        else:
            print('you must specify a module for importing.')
            return
    if args.new_client:
        if args.new_client_module:
            try:
                module = importlib.import_module(args.new_client_module)
                new_client = getattr(module, args.new_client)
            except Exception as e:
                print(e)
        else:
            print('you must specify a module for importing.')
            return
    if args.message_received:
        if args.message_received_module:
            try:
                module = importlib.import_module(args.message_received_module)
                message_received = getattr(module, args.message_received)
            except Exception as e:
                print(e)
        else:
            print('you must specify a module for importing.')
            return
        
    try:
        server = ws.WebsocketServer(host, port)
        server.set_fn_client_left(client_left)
        server.set_fn_message_received(message_received)
        server.set_fn_new_client(new_client)
        print(f'server listening on: {host}:{port}')
        server.run_forever()
    except Exception as e:
        print(e)
