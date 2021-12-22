#!/usr/bin/env python

from time import sleep
from tcp_port_listen import PortListen
from tcp_port_check import PortTest

import threading


if __name__ == '__main__':

    t = PortTest('www.google.com', 443)
    result = t.test()
    assert result, "PortTest to www.google.com failed"

    host_port_string = '10402'
    host_port = host_port_string.split(':')
    if len(host_port) == 2:
        host = host_port[0]
        port = host_port[1]
    else:
        host = '0.0.0.0'
        port = host_port[0]

    port = int(port)
    t = threading.Thread(target=PortListen, name="Listener", args=[host, port])
    t.start()
    sleep(1)

    t = PortTest('localhost', 10402)
    result = t.test()
    assert result

    t.join()
    assert not t.isAlive()
