"""
 MITM (Man In The Middle) by PeTrA 2021 ~
 ARP spoofing Architecture
    . base of Python3.8.2, Scapy2.4.3

 @ cui.py
    * MITM/src/package/mind.py
"""
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import sr1


def arp_spoofing(_target_ip_address):
    target_ip_address = _target_ip_address
    print("target_ip_address = " + target_ip_address)
    target_mac_address = get_ip_mac_address(target_ip_address)
    print("target_mac_address = " + target_mac_address)
    local_area_network_gateway_ip_address = get_local_area_network_gateway_ip_address()
    print("local_area_network_gateway_ip_address = " + local_area_network_gateway_ip_address)
    local_area_network_gateway_mac_address = get_ip_mac_address(local_area_network_gateway_ip_address)
    print("local_area_network_gateway_mac_address = " + local_area_network_gateway_mac_address)
    return


def get_local_area_network_gateway_ip_address():
    get_local_area_network_gateway_information_packet = sr1(IP(dst = "8.8.8.8", ttl = 0) / ICMP(), verbose = 0)
    local_area_network_gateway_ip_address = get_local_area_network_gateway_information_packet.src
    return local_area_network_gateway_ip_address

def get_local_area_network_information(self):
    get_gateway_information_packet = sr1(IP(dst = "8.8.8.8", ttl = 0) / ICMP(), verbose = 0)
    gateway_ip_address = get_gateway_information_packet.src
    print("gateway ip address : " + str(gateway_ip_address))

    self.get_target_mac_address(str(gateway_ip_address))

    return gateway_ip_address


def get_ip_mac_address(_ip_address):
    arp_response_packet = sr1(Ether(dst = "ff:ff:ff:ff:ff:ff") / ARP(pdst = str(_ip_address)), verbose = 0)
    result = arp_response_packet[0][1][ARP].hwsrc
    print(result)
    return result


def get_my_mac_address(self):

    return


