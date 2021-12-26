"""
 MITM (Man In The Middle) by PeTrA 2021 ~
 ARP spoofing Architecture
    . base of Python3.8.2, Scapy2.4.3

 @ cui.py
    * MITM/src/package/mind.py
"""
from scapy.config import conf

""" @ Mind class
"""
class Mind:
    def __init__(self):
        self.reset_value()
        return

    def reset_value(self):
        return

    def mind_engine(self):
        self.get_local_area_network_information()
        return

    def get_local_area_network_information(self):
        gateway_ip_address = conf.route.route("0.0.0.0")[2]

        print("gateway ip address : " + str(gateway_ip_address))

        return gateway_ip_address