import socket
import threading

host = '127.0.0.1'
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(0)
# TODO: make new thread upon accept
def receive(conn):
  keepReceiving = True
  while keepReceiving:
    data = conn.recv(1024)
    if not data:
      keepReceiving = False
    else:
      print(data)           

while True:
  conn, addr = s.accept() # conn is new socket for this connection
  conn
  threading.Thread(target = receive, args=(conn,)).start()

