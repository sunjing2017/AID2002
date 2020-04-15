from select import select
from socket import socket, timeout
from time import ctime


s=socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
s.setblocking(False)
# s.settimeout(2)
f=open('hello.py','a+')
while True:
    rs,ws,xs=select([s],[],[])
    for i in rs:
        if i is s:
            connnfd,addr=i.accept()
            connnfd.setblocking(2)
            rs.append(connnfd)
        else:
            data=i.recv(1024).decode()
            if not  data:
                rs.remove(i)
                i.close()
                continue
            ws.append(i)
    for w in ws:
        w.send(b'ok')
        ws.remove(w)



