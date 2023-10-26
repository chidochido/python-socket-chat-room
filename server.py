import socket
import threading

host = '127.0.0.1'
port = 8002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(0)
print(f'Server started on port {port}. Accepting connections')
# TODO: make new thread upon accept

data = 0
socketArray = []

def processClient(conn):
  keepReceiving = True
  while keepReceiving:
    
    try:
      data = conn.recv(1024)
      print(data.decode())
    except IOError as e:
      continue
    if not data:
      keepReceiving = False
    else:
      for socket in socketArray:
        if socket != conn:
          socket.send(data)      

while True:
  conn, addr = s.accept() # conn is new socket for this connection
  socketArray.append(conn)
  threading.Thread(target = processClient, args=(conn,)).start()

