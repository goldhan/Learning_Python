# -*- coding: utf-8 -*-
# 导入socket库:
import socket,threading,time

class Client(object):
    # 创建一个socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ipAdd, port):
        # 建立连接:
        self.s.connect((ipAdd, port))
        # 接收欢迎消息:
        print(self.s.recv(1024).decode('utf-8'))

    def closeSocket(self):
        self.s.send(b'exit')
        self.s.close()

    def send(self, mes):
        self.s.send(mes)
        # 接收数据:
        print(self.s.recv(1024).decode('utf-8'))
        # buffer = []
        # while True:
        #     # 每次最多接收1k字节:
        #     d = self.s.recv(1024)
        #     if d:
        #         buffer.append(d)
        #     else:
        #         break
        # data = b''.join(buffer)
        # # 关闭连接:
        # self.s.close()
        # header, message = data.split(b'\r\n\r\n', 1)
        # print(message)

class Service(object):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setConig(self,ipAdd,port):
        self.s.bind((ipAdd, port))

    def listen(self):
        self.s.listen(5)
        print('Waiting for connection...')

    def receive(self):
        def tcplink(sock, addr):
            print('Accept new connection from %s:%s...' % addr)
            sock.send(b'Welcome!')
            while True:
                data = sock.recv(1024)
                time.sleep(1)
                if not data or data.decode('utf-8') == 'exit':
                    break
                sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
            sock.close()
            print('Connection from %s:%s closed.' % addr)

        def receiveTread():
            while True:
                # 接受一个新连接:
                sock, addr = self.s.accept()
                # 创建新线程来处理TCP连接:
                t = threading.Thread(target=tcplink, args=(sock, addr))
                t.start()

        t = threading.Thread(target=receiveTread)
        t.start()
        

ipAdd = '127.0.0.1'
port = 8888
service = Service()
service.setConig(ipAdd,port)
service.listen()
service.receive()

print('初始化客户端')

client = Client()
client.connect(ipAdd,port)
client.send('hi1 ------')
client.send('hi2 ------')
