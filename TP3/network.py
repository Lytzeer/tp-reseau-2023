import get_ip
import lookup
import is_up
from sys import argv

def Network():
    match argv[0]:
        case "lookup":
            lookup.lookup(argv[1])
        case "ping":
            is_up.ping(argv[1])
        case "ip":
            get_ip.ip()
        case _:
            print(f"{argv[0]} is not an available command. Déso.")

Network()