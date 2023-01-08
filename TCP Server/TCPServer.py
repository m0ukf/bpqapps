import socket 
import threading
# Connection Data
host = '127.0.0.1'
# Start Server    
AppServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []
global lastmessage
global lastclient

def start_server(port):  #connect to specified port and start listening
    AppServer.bind((host, port))
    AppServer.listen()
    global lastmessage
    global lastclient
    lastmessage='cake'.encode('ascii')
    lastclient=1

# Start listening for new connection in a thread 
def start_recieve():
    newconnectionmonitor = threading.Thread(target=start_accepting_connections,) # create a thread that will listen out for connections in the background
    newconnectionmonitor.start() # start that thread

#thread that accepts new clients and creates a thread to manage them
def start_accepting_connections():
    while True:
        
            client, address = AppServer.accept()             # Accept Connection
            clients.append(client) # add to client list
            client.send('Connected to server!\n'.encode('ascii'))  # welcome to server
            clientinstance = threading.Thread(target=handle, args=(client,)) # creates thread to manage client
            clientinstance.start() # start thread
        
#Handle incoming messages
def handle(client,): 
    while True:
        try:
            global lastclient
            message = client.recv(1024)
            queueup(message)
            lastclient = clients.index(client)
        except: #deal with a disconnect
            index = clients.index(client)
            clients.remove(client)
            client.close()
  #      break
# Send a copy of the message to each client
def broadcast(message):
    for client in clients:
        client.send(message)

def DirectMessage(message,client):
    clients[client].send(message)

def queueup(message):
    global lastmessage    
    lastmessage=message
    
def returnmessage():
    global lastmessage
    return lastmessage
def returnclient():
    global lastclient
    return lastclient