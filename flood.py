import sys
import os
import subprocess
import sys

import sock as sock

os.system('clear')

ip = raw_input("Please provide the IP address of the Test Server: ")
#ip = sys.argv[1]

#Does an Initial NMAP Scan of TCP ports and writes the result to TCPSCAN.xml file
print("")
print ("++++++++++Starting TCP Protocol Scan +++++++++++++")
tcpScan = os.system("/usr/bin/nmap -sT -vvv -p- -Pn --webxml -oA TCPSCAN %s" %ip)
print ("++++++++++ END OF TCP Protocol Scan ++++++++++++++")


#Read the open port list from the TCPSCAN.xml file and store in a variable 
for port in range(0, 999):
  sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  hostfound = sockets.connect_ex((IP(dst="142.164.54.1"), port))
  if hostfound == 0:
   ports = print("Port {}: c	 Open".format(port))
   sock.close()
   openPorts = []
   openPorts.append(port)

#For each open port run the HPING3 tool. This command is used to test the TCP-SYN handshake only. Can be further modified to other Flags of TCP.


for port in openPorts.split():
    flood = os.system("/usr/sbin/hping3 %s -p {openPorts} -S -c 10000 -d 120 -w 64" %(ip))
    #print port

print ("")
print ("End of Flooding attack. ")

#Again do a Nmap scan and comare the results from the initial scan to see if the ports reported open earlier are still open.
print ("Now lets do a Fresh nmap scan again and compare the results")
print("")
print ("++++++++++Starting TCP Protocol Scan +++++++++++++")
newTcpScan = os.system("/usr/bin/nmap -sT -vvv -p- -Pn --webxml -oA -T5 TCPSCAN %s" %ip)
print ("++++++++++ END OF TCP Protocol Scan ++++++++++++++")

newPorts = os.popen("/bin/cat  $PWD/TCPSCANnew.xml | grep 'portid' |cut -d '=' -f 3 | cut -d '>' -f 1 | cut -d '\"' -f 2 ").read()
print ("")

print ("The list of open ports after flood are: "),
print newPorts.split()
print ("The list of open ports before flood are: "),
print openPorts.split()

if openPorts.split() == newPorts.split():
        print ("Flooding Test is passed. All ports seems to be OPEN after the tests")
else:
        print ("Some ports are not open. Please verify if the ports are reachable")
