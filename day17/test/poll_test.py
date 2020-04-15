from select import *
from socket import socket, timeout
from time import ctime


s=socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
s.setblocking(False)
print(s.fileno())
# s.settimeout(2)
f=open('geckodriver.log','a+')
print(f.fileno())#file descriptin fuhao  #4
dict_fileno={s.fileno():s,f.fileno():f}
pol=poll()
pol.register(s,POLLIN)
pol.register(f,POLLIN|POLLOUT)

events=pol.poll()
print(events)



