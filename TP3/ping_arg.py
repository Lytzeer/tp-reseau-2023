from sys import argv
import os


print(os.system(f"ping {argv[0]}"))