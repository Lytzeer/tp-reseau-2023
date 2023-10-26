from sys import argv
import os

def ping(ip):
    upDown=os.system(f"ping {ip} > nul")
    if upDown==0:
        print("UP !")
    else:
        print("DOWN !")