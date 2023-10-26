import socket
import random
import time

host = '127.0.0.1'
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(num)
s.connect((host, port))
while True:
  userInput = input("Enter something: ")
  s.send(userInput.encode())