import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("",100))
server.listen(5)

while (1):
  print "joya"

