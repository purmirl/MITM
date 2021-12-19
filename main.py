"""
 MITM (Man In The Middle) by PeTrA 2021 ~
 ARP spoofing Architecture
    . base of Python3.8.2, Scapy2.4.3

 @ main.py
    * MITM/main.py
"""
from src.package import cui

""" @ main function
"""

def main():
    main_cui_engine = cui.Cui()
    main_cui_engine.cui_engine()
    return

""" @ call main
"""
if __name__ == "__main__":
    main()