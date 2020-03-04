import socket
import sys
import os

def main():
    # Main method
    try:
        HOST = sys.argv[1]
    except IndexError:
        sys.stderr.write('ERROR: Host name or IP address must be supplied on the command line\n')
        sys.exit(1)

    try:
        if int(sys.argv[2]) > 1023:
            PORT = int(sys.argv[2])
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


    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

        sock.connect((HOST,PORT)) 

        # Continue implementation


if __name__ == '__main__':
    main()