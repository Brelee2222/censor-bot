from encrypt import decrint, encrint
with open('conv.py', 'w') as f:
  with open('totaly just numbers.txt', 'r') as g:
    f.write(f"""{encrint(g.read())}""")
import conv