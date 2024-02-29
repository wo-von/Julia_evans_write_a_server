import socket
import time
import _thread
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8080))
s.listen(10) # 10 is the backlog
http_response = b"""HTTP/1.1 200 OK\r
Content-Length: 10\r

hi NAME!\n\r\n"""
def respond(conn):
    request = conn.recv(4096)
    name = request.split(b'/')[1]
    time.sleep(0.5)
    conn.send(http_response.replace(b"NAME", name))
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
while True:
    # wait for a connection
    conn, address = s.accept()
    _thread.start_new_thread(respond, (conn,))
s.close()