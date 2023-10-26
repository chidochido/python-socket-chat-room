import socket
import threading
import time
import random
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-join', action='store_true')
parser.add_argument('-host', type=str)
parser.add_argument('-port', type=int)
parser.add_argument('-username', type=str)
parser.add_argument('-passcode', type=str)
args = parser.parse_args()

host = args.host
port = args.port
username = args.username
passcode = args.passcode
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.send(passcode.encode())
res = s.recv(1024).decode()

if res == "Incorrect passcode.":
  print(res)
  exit()

print(f"Connected to {host} on port {port}")
s.setblocking(False)


displayPrompt = '<' + username + '>'

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

  data = displayPrompt + ': ' + userInput
  s.send(data.encode())

