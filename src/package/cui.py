"""
 MITM (Man In The Middle) by PeTrA 2021 ~
 ARP spoofing Architecture
    . base of Python3.8.2, Scapy2.4.3

 @ cui.py
    * MITM/src/package/cui.py
"""

""" @ Cui class
"""
class Cui:
    def __init__(self):
        return

    def cui_engine(self):
        while True:
            cui_main_command = self.get_command("main")

        return

    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@mindarrow:~# ")
        return result