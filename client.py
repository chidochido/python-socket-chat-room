import socket
import random
import time

host = '127.0.0.1'
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
num = random.randint(0, 100)
print(num)
s.connect((host, port))
while True:
  time.sleep(2)
  s.send(str(num).encode())