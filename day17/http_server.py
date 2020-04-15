from select import select
from socket import *


class HTTPserver:
    def __init__(self, host='0.0.0.0', port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        # 创建套接字和地址绑定
        self.create_socket()
        self.bind()
        self.rslist = []
        self.wslist = []
        self.xslist = []
    # 启动服务
    def start(self):
        self.socket.listen(3)
        print('port%s' % (self.port))
        # select tcp并发
        self.rslist.append(self.socket)
        while True:
            rs,ws,xs= select(self.rslist, self.wslist, self.xslist)
            for r in rs:
                if r is self.socket:
                    confd, addr = r.accept()
                    confd.setblocking(2)
                    self.rslist.append(confd)
                else:
                    #处理客户端套接字
                    self.handle(r)


    def create_socket(self):
        self.socket = socket()
        self.socket.settimeout(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.socket.bind(self.address)

    def handle(self, confd):
        request=confd.recv(1024).decode()
        list_req=request.split(' ')
        try:
            info=list_req[1]
        except:
            self.rslist.remove(confd)
            confd.close()
            return
        else:
            self.send_html(confd,info)

    def send_html(self, confd, info):
        if info=='/':
            filename=self.html+'index.html'
        else:
            filename=self.html+info
        try:
            #打开网页
            f=open(filename,'rb')
        except:
            #网页不存在的情况考虑
            respose_content="sorry------"
            response_headers = "HTTP/1.1 200 OK\r\n"
            response_headers+= "Content-Type:text/html\r\n"
            response=(response_headers+respose_content).encode()
        else:
            respose_content = f.read()
            response_headers = "HTTP/1.1 200 OK\r\n"
            response_headers += "Content-Type:text/html\r\n"
            response = (response_headers ).encode()+respose_content
            f.close()
        finally:
            confd.send(response)


if __name__ == '__main__':
    # / home / tarena / PycharmProjects / tarenasj
    host = '0.0.0.0'
    port = 80
    # day17 / test / static
    dir = 'static'
    httpd = HTTPserver(host=host, port=port, html=dir)
    httpd.start()
