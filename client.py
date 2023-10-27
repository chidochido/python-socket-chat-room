import socket
import threading
import time
import random
import sys
import argparse
import datetime


def getDayOfWeek(weekday):
  if weekday == 0:
    return 'Mon'
  elif weekday == 1:
    return 'Tues'
  elif weekday == 2:
    return 'Wed'
  elif weekday == 3:
    return 'Thurs'
  elif weekday == 4:
    return 'Fri'
  elif weekday == 5:
    return 'Sat'
  elif weekday == 6:
    return 'Sun'
  
def getMonth(month):
  if month == 1:
    return 'Jan'
  elif month == 2:
    return 'Feb'
  elif month == 3:
    return 'Mar'
  elif month == 4:
    return 'Apr'
  elif month == 5:
    return 'May'
  elif month == 6:
    return 'Jun'
  elif month == 7:
    return 'Jul'
  elif month == 7:
    return 'Aug'
  elif month == 9:
    return 'Sep'
  elif month == 10:
    return 'Oct'
  elif month == 11:
    return 'Nov'
  elif month == 12:
    return 'Dec'

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
  sys.stdout.flush()
  exit()
s.send(username.encode())
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
  elif userInput == ":(":
    userInput = "[Feeling Sad]"
  elif userInput == ":mytime":
    now = datetime.datetime.now()
    mytime = getDayOfWeek(now.weekday()) + ' ' + getMonth(now.month) + ' ' + str(now.day) + ' ' + str(now.strftime('%H:%M:%S')) + ' ' + str(now.year)
    userInput = mytime
  elif userInput == ":+1hr":
    now = datetime.datetime.now()
    mytime = getDayOfWeek(now.weekday()) + ' ' + getMonth(now.month) + ' ' + str(now.day) + ' ' + str((now + datetime.timedelta(hours=1)).strftime('%H:%M:%S')) + ' ' + str(now.year)

    userInput = mytime
  data = displayPrompt + ': ' + userInput
  s.send(data.encode())

