import time
import TCPServer #link to TCP Server
TCPServer.start_server(63000) #start tcp server on port 6300x
TCPServer.start_recieve() # start monitoring connections
global getlast
getlast = ''


def InitialiseApp():
    waitforinput()

def waitforinput():
    while True:
       global getlast 
       previous = getlast
       getlast = TCPServer.returnmessage()
       getlastc = TCPServer.returnclient()
       if getlast != previous:
            takeAction(getlast,getlastc)

def takeAction(input,userid):    
    output = 'User ' + str(userid) + ': '+ getlast.decode('ascii')[:-2] + ' is a thing\n'
    output = output + 'OR IS IT\n'
    output = output.encode('ascii')
    TellAll(output)
    waitforinput()


def TellAll(message):
    TCPServer.broadcast(message)

def TellOne(message,client):
    TCPServer.DirectMessage(message,client)

InitialiseApp()
