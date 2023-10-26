import socket
import threading
import time
import random
import sys
import argparse

host = '127.0.0.1'
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
s.setblocking(False)

username = '<user' + str(random.randint(0, 1000)) + '>'

def receiveMessages():
  while True: 
    try:
      res = s.recv(1024).decode()
      print(res)
      sys.stdout.flush()
    except IOError as e:
      continue

threading.Thread(target = receiveMessages).start()
while True:
  userInput = input("")
  data = None
  if userInput == ":)":
    userInput = "[Feeling Happy]"

  data = username + ': ' + userInput
  s.send(data.encode())

