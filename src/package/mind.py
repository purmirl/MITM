"""
 MITM (Man In The Middle) by PeTrA 2021 ~
 ARP spoofing Architecture
    . base of Python3.8.2, Scapy2.4.3

 @ cui.py
    * MITM/src/package/mind.py
"""
import scapy
from scapy.arch import IFACES
from scapy.compat import raw
from scapy.config import conf
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

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
        get_gateway_information_packet = sr1(IP(dst = "8.8.8.8", ttl = 0) / ICMP(), verbose = 0)
        gateway_ip_address = get_gateway_information_packet.src
        print(get_gateway_information_packet.show())
        # print("gateway ip address : " + str(gateway_ip_address))

        return gateway_ip_address