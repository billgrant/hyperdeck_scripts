# Script to start and stop recording on multiple blackmagic hyperdecks.

from telnetlib import Telnet
import sys
from multiprocessing import Process

TCP_PORT = 9993

# Dictonary containing the hyperdecks
hyperdecks = {
    "Hyperdeck1" : "10.5.241.44",
    "Hyperdeck2" : "10.5.241.45",
    "Hyperdeck3" : "10.5.241.46",
    "Hyperdeck4" : "10.5.241.47",
    "Hyperdeck5" : "10.5.241.48",
    "Hyperdeck6" : "10.5.241.49",
    "Hyperdeck7" : "10.5.241.50",
    "Hyperdeck8" : "10.5.241.51",
    "Hyperdeck9" : "10.5.241.52",
}

def record_start():
     p1 = Process(target = record_start_mp(hyperdecks['Hyperdeck1']))
     p2 = Process(target = record_start_mp(hyperdecks['Hyperdeck2']))
     p3 = Process(target = record_start_mp(hyperdecks['Hyperdeck3']))
     p4 = Process(target = record_start_mp(hyperdecks['Hyperdeck4']))
     p5 = Process(target = record_start_mp(hyperdecks['Hyperdeck5']))
     p6 = Process(target = record_start_mp(hyperdecks['Hyperdeck6']))
     p7 = Process(target = record_start_mp(hyperdecks['Hyperdeck7']))
     p8 = Process(target = record_start_mp(hyperdecks['Hyperdeck8']))
     p9 = Process(target = record_start_mp(hyperdecks['Hyperdeck9']))
     p1.start()
     p2.start()
     p3.start()
     p4.start()
     p5.start()
     p6.start()
     p7.start()     
     p8.start()
     p9.start()





def record_start_mp(ipaddress):
    """Telnet to the decks and start recording"""
    status = ""
    #for deckname, ipaddress in hyperdecks.items():
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