import socket
import threading

host = '127.0.0.1'
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(0)
# TODO: make new thread upon accept
def receive(conn):
  while True:
    print(conn.recv(10))           # receive 10 bytes


while True:
  conn, addr = s.accept() # conn is new socket for this connection
  threading.Thread(target = receive, args=(conn,)).start()


# print(conn.recv(10))           # receive 10 bytes
