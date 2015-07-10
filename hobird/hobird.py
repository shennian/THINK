import socket
import os

class HobirdServer():
    def __init__(self, ip, port):
        self.m_ip = ip
        self.m_port = port
        self.m_socket = None
        self.content = 'HTTP/1.x 200 OK\r\n' 
    
    def run(self):
        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m_socket.bind((self.m_ip, self.m_port))
        
        while True:
            self.m_socket.listen(3)
            connect, address = self.m_socket.accept()
            data = connect.recv(1024)
            request_lists = self.handle_http_request(data) 
            self.handle_http_request(data)
            source = '/index.html'
            if request_lists[0][1] != '/':
                source = request_lists[0][1]
                if '.html' in source:
                    self.content += 'Content-Type: text/html\r\n\r\n'
                elif '.css' in source:
                    self.content += 'Content-Type: text/css\r\n\r\n'
                elif '.js' in source:
                    self.content += 'Content-Type: text/js\r\n\r\n'
                elif '.jpg' in source:
                    self.content += 'Content-Type: image/jpg\r\n\r\n'
                elif '.png' in source:
                    self.content += 'Content-Type: image/png\r\n\r\n'
                else:
                    self.content += 'Content-Type: text/html\r\n\r\n'
            else:
                self.content += 'Content-Type: text/html\r\n\r\n'
                source = '/index.html'
            try:
                print os.getcwd()+'/www'+source
                fp = open(os.getcwd()+'/www'+source, 'r')
                f = fp.read()
                fp.close()
                connect.sendall(self.content + f)
            except:
                print "not found"
                fp = open(os.getcwd()+'/www'+'/404.html', 'r')
                f = fp.read()
                fp.close()
                connect.sendall(self.content + f)
            self.content = 'HTTP/1.x 200 OK\r\n'
            connect.close()
    
    def test(self, data):
        s = data.split('\r\n')
        n = []
        for i in s:
            n.append(i.split(' '))
        print n
    
    def command_display(self, address):
        print address
        
    def handle_http_request(self, data):    
        http_request = []
        _data = data.split('\r\n')
        for request in _data:
            http_request.append(request.split(' '))
        return http_request
        

if __name__ == '__main__':
    server = HobirdServer('127.0.0.1', 5000)
    server.run()
        
        
