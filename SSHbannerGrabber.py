import socket 

Ports = [21, 22, 25, 3306]

for Port in Ports:
    s = socket.socket()

    print('This is the Banner for the port')

    print(Port) 

    s.connect(("127.0.0.1", Port))
    
    answer = s.recv(1024)

    print(answer)

    s.close()