#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import os
import time

class PortTest:

    """
    Test TCP port connectivity to a remote host or IP

    ...

    Attributes
    ----------
    host : str
        hostname or IP
    port : int
        unused TCP port number
    timeout: int
        timeout in seconds to wait for a response (default is 2)
    duration: int
        Default when host/port is not reachable is -1
        After test is complete, the response time is set in milliseconds

    Methods
    -------
    test():
        Test connection and return boolean (True = successful connection).
    """

    duration = -1  # default duration, set to actual timing in milliseconds if successful

    def __init__(self, host: str, port: int, timeout: int = 2):
        self.host = host
        self.port = port
        self.socket = socket.socket()
        self.socket.settimeout(timeout)

    def test(self) -> bool:
        start = time.time()
        try:
            self.socket.connect((self.host, self.port))
        except socket.error:
            # print("Connection to %s on port %s failed: %s" % (address, port, e))
            return False
        end = time.time()
        self.duration = round((end - start) * 1000)
        return True

def usage(exit_code=0):
    """ Display help message if invalid syntax. """
    print(os.path.basename(__file__) + ' <hostname/IP> <tcp_port>')
    sys.exit(exit_code)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Exactly 2 arguments required.")
        usage(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    t = PortTest(host, port)
    result = t.test()
    if result:
        print('%s:%s is %s (%s ms)' % (host, port, 'UP', t.duration))
        sys.exit(0)
    else:
        print('%s:%s is %s' % (host, port, 'DOWN'))
        sys.exit(1)   

