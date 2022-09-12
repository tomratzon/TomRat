#!/bash/python3

import os
from time import sleep
import sys
print("checking if container is up and working\n")
sleep(2)
#thisIP=os.system("hostname -I|awk '{print $1}'")
#print(thisIP)
#print("bla bla")
os.system('telnet "hostname -I|awk '{print $1}'" 49153')
#os.system('telnet 192.168.68.110 49153')

