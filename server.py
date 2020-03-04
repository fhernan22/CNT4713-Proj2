import sys
import socket
import signal
import os
from _thread import *
import threading
import struct

HOST = '0.0.0.0'
establishedConnections = 0

# Function used to capture exit signal
def receiveSignal(signalNumber, frame):
    print('Exiting server with signanl number:', signalNumber)
    sys.exit(0)


def main():
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

    
    # Create a folder if it doesn't exist
    if not os.path.exists(sys.argv[2]):
        os.mkdir(sys.argv[2], mode = 0o777) 


    # Continue implementation





if __name__ == '__main__':
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGTERM, receiveSignal)
    main()