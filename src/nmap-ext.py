#/usr/bin/python3

import nmap

nm = nmap.PortScanner()
print "Enter the IP"
ip=input("@>")
print 'Enter the port or port range'
print 'Usage - 40 or 40-100'
port = input("@>")
nn.scan(ip, port)
nn.command_line()