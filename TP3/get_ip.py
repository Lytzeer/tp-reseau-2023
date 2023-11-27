from os import system
import psutil


def ip():
    if(os.name=="posix"):
        return(psutil.net_if_addrs()[list(psutil.net_if_addrs().keys())[1]][0][1])
    else:
        print(psutil.net_if_addrs()["Wi-Fi"][1][1])
    
