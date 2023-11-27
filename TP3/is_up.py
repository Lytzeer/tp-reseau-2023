from sys import argv
import os

def ping(ip):
    if (os.name=="posix"):
        response=os.system("ping " + ip+" >/dev/null")
    else:
        upDown=os.system(f"ping {ip} > nul")
    if upDown==0:
        print("UP !")
    else:
        print("DOWN !")
