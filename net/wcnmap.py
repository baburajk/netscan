import subprocess
from os import system

class wcnmap:

    def __init__(self):
        cmd = "nmap"
        args = ["192.168.3.2", "2210"]
        print(type(args))
        sp = subprocess.run(cmd,   shell=True)
        print(sp)


#<<EOC_wcnmap

def main():
    wc = wcnmap()


main()
