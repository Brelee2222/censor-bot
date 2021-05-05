import time 

with open('uptime.txt', 'a') as file:
  with open('time.txt', 'r') as filet:
    file.write((', ' + str(round(time.time()) - float(filet.read()))))
with open('time.txt', 'w') as file:
  file.write(str(time.time()))
import os




from dhooks import Webhook

hook = Webhook(os.getenv('WEBHOOKTOKEN'))
with open('uptime.txt', 'r') as file:
  uptime = file.read().split(', ')
hook.send(('Censor bot has been down for at most ' + uptime[len(uptime) - 1] + ' seconds')) 
from encrypt import decrint, encrint
with open('conv.py', 'w') as f:
  with open('totaly just numbers.txt', 'r') as g:
    f.write(f"""{encrint(g.read())}""")
import conv