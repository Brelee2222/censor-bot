import time 
with open('uptime.txt', 'a') as file:
  with open('time.txt', 'r') as filet:
    file.write((', ' + str(round(time.time()) - float(filet.read()))))
with open('time.txt', 'w') as file:
  file.write(str(time.time()))
from encrypt import decrint, encrint
with open('conv.py', 'w') as f:
  with open('totaly just numbers.txt', 'r') as g:
    f.write(f"""{encrint(g.read())}""")
import conv