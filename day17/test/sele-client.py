from select import select
from socket import socket, timeout
from time import ctime

from django.conf.locale import el

s=socket()
s.connect(('0.0.0.1',8888))

# s.settimeout(2)
while True:
    msg=input(">>")
    if not msg:
        break
    s.send(msg.encode(),)
    data=s.recv(20)
    print('recive:%s'%data)




