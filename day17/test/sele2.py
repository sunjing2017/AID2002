from select import select
from socket import socket, timeout
from time import ctime

s=socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

s.settimeout(2)
f=open('hello.py','a+')
while True:
    try:
        connfd,addr=s.accept()
        print('connect:',addr)
        rs,ws,xs=select([s],[f],[])
    except timeout as e:
        f.write('%s :%s'%(ctime(),e))
        f.flush()
    except BlockingIOError as e:
        f.write('%s :%s'%(ctime(),e))
        f.flush()
    else:
        data=connfd.recv(1024)
        print(data)

