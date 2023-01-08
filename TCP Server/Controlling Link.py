import time
import TCPServer #link to TCP Server
TCPServer.start_server(63000) #start tcp server on port 6300x
TCPServer.start_recieve() # start monitoring connections
global getlast
getlast = 'nowt'

while True:
    previous = getlast
    getlast = TCPServer.returnmessage()
    if getlast != previous:
            output = getlast.decode('ascii')[:-2] + ' is a thing\n'
            output = output.encode('ascii')
            TCPServer.broadcast(output)
            TCPServer.broadcast('or is it\n'.encode('ascii'))
