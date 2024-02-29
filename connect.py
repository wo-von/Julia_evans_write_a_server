import socket
s = socket.socket()
s.connect(("93.184.216.34", 80))
s.send(b"GET / HTTP/1.1\r\nHOST: example.com\r\n\n")
print((s.recv(4096)))