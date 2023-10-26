import socket
import threading
import sys
import argparse

host = '127.0.0.1'

parser = argparse.ArgumentParser()
# Optional argument
parser.add_argument('-start', action='store_true')
parser.add_argument('-port', type=int)
parser.add_argument('-passcode', type=str)
args = parser.parse_args()

port = args.port
passcode = args.passcode


if (len(passcode) > 5):
  exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(0)
print(f'Server started on port {port}. Accepting connections')
sys.stdout.flush()
# TODO: make new thread upon accept

data = 0
socketArray = []

def processClient(conn):
  keepReceiving = True
  attemptedPass = conn.recv(1024).decode()
  if attemptedPass != passcode:
    keepReceiving = False
    conn.send("Incorrect passcode.".encode())
  else:
    conn.send("Good pass".encode())
  print("responded to client")
  while keepReceiving:
    
    try:
      data = conn.recv(1024)
      print(data.decode())
      sys.stdout.flush()
    except IOError as e:
      continue
    if not data:
      keepReceiving = False
    else:
      for socket in socketArray:
        if socket != conn:
          socket.send(data)    
  conn.close()  

while True:
  conn, addr = s.accept() # conn is new socket for this connection
  socketArray.append(conn)
  threading.Thread(target = processClient, args=(conn,)).start()

