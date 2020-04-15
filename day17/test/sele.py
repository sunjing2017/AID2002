from select import select
from socket import socket

s=socket()
s.bind(('127.0.0.1',8888))
s.listen(3)
f=open('hello.py','a+')

print('begin=====')
rs,ws,xs=select([s],[f],[])
print('rslist:',rs)
print('wslist:',ws)
print('xslist:',xs)

