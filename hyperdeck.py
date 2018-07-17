# Script to start and stop recording on multiple blackmagic hyperdecks.

from telnetlib import Telnet
import sys

TCP_PORT = 9993

# Dictonary containing the hyperdecks
hyperdecks = {
    "Hyperdeck1" : "10.1.1.1",
    "Hyperdeck2" : "10.1.1.2",
    "Hyperdeck3" : "10.1.1.3",
    "Hyperdeck4" : "10.1.1.4",
    "Hyperdeck5" : "10.1.1.5",
    "Hyperdeck6" : "10.1.1.6",
    "Hyperdeck7" : "10.1.1.7",
    "Hyperdeck8" : "10.1.1.8",
    "Hyperdeck9" : "10.1.1.9",
}

def record_start():
    """Telnet to the decks and start recording"""
    status = ""
    for deckname, ipaddress in hyperdecks.items():
        tn = Telnet(ipaddress, TCP_PORT)
        tn.write(b'record' + b'\r\n')
        tn.write(b'quit' + b'\r\n')
        status += tn.read_all().decode('ascii')
        print(status)

def record_stop():
    """Telnet to the decks and stop recording"""
    status = ""
    for deckname, ipaddress in hyperdecks.items():
        tn = Telnet(ipaddress, TCP_PORT)
        tn.write(b'stop' + b'\r\n')
        tn.write(b'quit' + b'\r\n')
        status += tn.read_all().decode('ascii')
        print(status)

    """Enables remote and sets the input"""
def remote_enable():
    status = ""
    for deckname, ipaddress in hyperdecks.items():
        tn = Telnet(ipaddress, TCP_PORT)
        tn.write(b'remote: enable: true' + b'\r\n')
        tn.write(b'configuration: video input: SDI' + b'\r\n')
        tn.write(b'quit' + b'\r\n')
        status += tn.read_all().decode('ascii')
        print(status)

"""Checks for input from the cli"""
if "record_start" in sys.argv[1:]:
    record_start()
elif "record_stop" in sys.argv[1:]:
    record_stop()
elif "remote_enable" in sys.argv[1:]:
    remote_enable()
else:
    print("Please use record_start,record_stop, or remote_enable")



    

