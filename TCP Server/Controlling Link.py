import time
import TCPServer
TCPServer.start_server(63001)
TCPServer.start_recieve()
while True:
    print('cake')
    time.sleep(10)
    TCPServer.broadcast('did i mention cakes'.encode('ascii'))
