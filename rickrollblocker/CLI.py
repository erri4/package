from .blocker import process_packet, blacklist
import argparse
from scapy.all import *
import os
import subprocess


def start():
    sniff(filter='tcp', prn=process_packet, store=0)


def stop():
    os.system('taskkill /f /im rickrollblocker.exe')


def viewblacklist(args):
    if args.add:
        blacklist.append(args.add)
    else:
        for url in blacklist:
            print(url)


def main():
    parser = argparse.ArgumentParser(description="Service management tool.")
    
    subparsers = parser.add_subparsers(help="Available commands", dest="command")

    subparsers.add_parser("stop", help="Stop the service.")
    subparsers.add_parser("start", help="not for deploy. for development.")

    blacklist_parser = subparsers.add_parser("blacklist", help="Manage the blacklist.")
    blacklist_parser.add_argument("-add", metavar="URL", help="Add a URL to the blacklist.")

    args = parser.parse_args()

    if args.command == "stop":
        stop()
    elif args.command == "blacklist":
        viewblacklist(args)
    elif args.command == 'start':
        start()
    elif args.command == None:
        subprocess.Popen('rickrollblocker start')
