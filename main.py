import sys
import argparse
from netaddr import *

class nettool:

    def debug():
        print ("Entrypoint module = ",__name__)

def main():
        try:
            print ("This is main", __name__)
            cli = argparse.ArgumentParser()
            cli.add_argument("-c",action="store",dest="cidr")
            args = cli.parse_args()
            print ("CIDR", args.cidr)
            ip = IPNetwork(args.cidr)
            ip_list = [ ip for ip in IPNetwork(args.cidr) ]
            print(ip_list)
            # cd /usr/share/nmap/nselib/data 
            # http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
            # gunzip -d 
            
            #Find from the list which hosts are up (ping, may be blocked), send TCP SYN on port 22.    

            

        except:
            print("Unexpected error occured, trace follows", sys.exc_info()[0])

if __name__ == "__main__":
    main()
    
