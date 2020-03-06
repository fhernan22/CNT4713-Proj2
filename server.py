import confundo
import sys
import socket
import signal
import os
from _thread import *
import threading
import struct
import argparse

HOST = '0.0.0.0'

# Example how to use the provided confundo.Header class
sampleInput = b'\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00\x02sample-buffer'
print(sampleInput)
print(sampleInput[0:12])


pkt = confundo.header.Header()
pkt.decode(sampleInput[0:12])

def receiveSignal(signalNumber, frame):
    print('Exiting server with signanl number:', signalNumber)
    sys.exit(0)

def main():
    print(pkt.seqNum, pkt.ackNum, pkt.connId, pkt.isAck, pkt.isSyn, pkt.isFin)

    try:
        if int(sys.argv[1]) > 1023:
            PORT = int(sys.argv[1])
        else:
            PORT = 'n/a'
            sys.stderr.write('ERROR: Port number must be greater than 1023\n')
            sys.exit(1)
    except IndexError:
        sys.stderr.write('ERROR: Port number must be supplied on the command line\n')
        sys.exit(1)
    except ValueError:
        sys.stderr.write('ERROR: Port number must be an integer\n')
        sys.exit(1) 

    if not os.path.exists(sys.argv[2]):
        os.mkdir(sys.argv[2], mode = 0o777) 

    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    conn = confundo.Socket(sock)

    try:
        remote = socket.getaddrinfo(HOST, PORT, family=socket.AF_INET, type=socket.SOCK_DGRAM)
    except (socket.error, OverflowError) as e:
        sys.stderr.write("ERROR: Invalid hostname or port (%s)\n" % e)
        sock.close()
        sys.exit(1)

    (family, type, proto, canonname, sockaddr) = remote[0]


    conn.connect(sockaddr)




if __name__ == '__main__':
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGTERM, receiveSignal)
    main()