"""
 MITM (Man In The Middle) by PeTrA 2021 ~
 ARP spoofing Architecture
    . base of Python3.8.2, Scapy2.4.3

 @ cui.py
    * MITM/src/package/cui.py
"""
from src.package import mind

""" @ Cui class
"""
class Cui:
    def __init__(self):
        return

    def cui_engine(self):
        while True:
            self.run_arp_spoofing()
            cui_main_command = self.get_command("main")


        return

    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@mindarrow:~# ")
        return result

    def run_arp_spoofing(self):
        mind_arp_spoofing_instance = mind.Mind()
        mind_arp_spoofing_instance.mind_engine()

        return