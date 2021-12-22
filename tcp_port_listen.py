#!/usr/bin/env python

import socket
import sys
import os

class PortListen:

    """
    Listen on an unused TCP port to test layer 4 connectivity

    ...

    Attributes
    ----------
    host : str
        hostname or IP
    port : int
        unused TCP port number

    Methods
    -------
    no public methods
    """

    def __init__(self, host: str, port: int, max_count: int = 1):
        self.host = host
        self.port = port
        self.max_count = max_count
        # Create a TCP/IP socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__bind()
        self.__listen()

    def __bind(self):
        # Bind the socket to the port
        server_address = (self.host, self.port)
        print('Starting up on {} port {}'.format(*server_address))
        self.socket.bind(server_address)

    def __listen(self):
        # Listen for incoming connections
        self.socket.listen(1)
        # Wait for a connection
        print('waiting for a connection')

        count = 0
        while True:
            connection, client_address = self.socket.accept()
            try:
                print('connection from', client_address)
                count += 1
                if self.max_count > 0 and count >= self.max_count:
                    break
                # uncomment this line to exit after a connection is made
                #break

            finally:
                # Clean up the connection
                # print("Closing current connection")
                connection.close()


def usage(exit_code=0) -> int:
    """ Display help message if invalid syntax. """
    print(os.path.basename(__file__) + ' <tcp_port>')
    print(os.path.basename(__file__) + ' <ip_address:tcp_port>')
    sys.exit(exit_code)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Exactly 1 argument required.")
        usage(1)

    host_port = sys.argv[1].split(':')
    if len(host_port) == 2:
        host = host_port[0]
        port = host_port[1]
    else:
        host = '0.0.0.0'
        port = host_port[0]

    port = int(port)
    
    l = PortListen(host, port, max_count = 2)
