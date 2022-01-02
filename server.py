import socket


s = socket.socket()
print('Socket Created')


s.bind(('localhost',9999))

s.listen(8)
print('waiting for connections')

while True:
    client_socket, address = s.accept()
    name = client_socket.recv(1024).decode()
    print('Connected with',address,name)
    client_socket.send(bytes('Welcome','utf-8'))
    
    client_socket.close()
