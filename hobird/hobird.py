import socket
import os

class HobirdServer():
	def __init__(self, ip, port):
		self.m_ip = ip
		self.m_port = port
		self.m_socket = None
		self.text_content = 'HTTP/1.x 200 OK\r\nContent-Type: text/html\r\n\r\n' 
	
	def run(self):
		self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.m_socket.bind((self.m_ip, self.m_port))
		
		while True:
			self.m_socket.listen(1)
			connect, address = self.m_socket.accept()
			data = connect.recv(1024)
			print address
			fp = open(os.getcwd()+'/www/index.html')
			f = fp.read()
			fp.close()
			connect.sendall(self.text_content + f)
			connect.close()



if __name__ == '__main__':
	server = HobirdServer('127.0.0.1', 5000)
	
	server.run()
		
		
