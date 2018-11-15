import socket   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit() 
host = 'redes.catedras.linti.unlp.edu.ar';
port=1233
print socket.gethostname()
s.bind(("192.168.0.2",5000))

#Set the whole string
 
s.sendto("Grupo Ac", (host, port))
    # receive data from client (data, addr)
d,server = s.recvfrom(4096)
print >>sys.stderr, 'received "%s"'%d
print d
   
     
   
