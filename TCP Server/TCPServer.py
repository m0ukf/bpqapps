import socket 
import threading
# Connection Data
host = '127.0.0.1'

# Start Server    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []

def start_server(port):
    server.bind((host, port))
    server.listen()



# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            strmessage = message.decode('ascii')
            if strmessage.find('/kill') != -1:
                broadcast('Bye Friend'.encode('ascii'))
                server.close()
                
            else:
                broadcast('Someone said: '.encode('ascii') +message)
        except:

            index = clients.index(client)
            clients.remove(client)
            client.close()

            break
# Receiving / Listening Function
def acceptclients():
    while True:
        try:
            # Accept Connection
            client, address = server.accept()
            print("Connected with {}".format(str(address)))
            clients.append(client)
            client.send('Connected to server!\n'.encode('ascii'))
            # creates thread to manage client
            clientinstance = threading.Thread(target=handle, args=(client,))
            clientinstance.start()
        finally:
            print ('meh')
            
def start_recieve():
    newconnectionmonitor = threading.Thread(target=acceptclients,)
    newconnectionmonitor.start()

#startserver()
#receive()


