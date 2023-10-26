from os import system
import psutil


def ip():
    print(psutil.net_if_addrs()["Wi-Fi"][1][1])
    