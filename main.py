import socket
import random
def gethip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(hostname)
    print(IPAddr)
print('''
[1] show my ip & hostname

[2] info
''')


chinput = input('select number : ')
if chinput == '1':
   gethip()