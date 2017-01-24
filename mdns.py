#!/usr/bin/env python
import socket
from time import sleep
from zeroconf import ServiceInfo, Zeroconf

if __name__ == '__main__':
    # get machine local IP
    local_hostname = socket.gethostbyname(socket.gethostname())

    info = ServiceInfo(type_="_http._tcp.local.",
                       name="mywebserver._http._tcp.local.",
                       address=socket.inet_aton(local_hostname),
                       port=8080,
                       weight=0, priority=0,
                       properties={"any_key": "any_value"},
                       server="mywebserver.local.")
    zeroconf = Zeroconf()
    print("Registration of a service, press Ctrl-C to exit...")
    zeroconf.register_service(info)
    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Unregistering...")
        zeroconf.unregister_service(info)
        zeroconf.close()
