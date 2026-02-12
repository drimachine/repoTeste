import socket
import threading

def listenServer(c_socket):
    while True: 
        try:
            mensage = c_socket.recv(1024).decode('utf-8')
            if not mensage: 
                break
            
            print(mensage)          
        except:
            print('\nConexão encerrada')
            break

def runClient():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(('localhost', 8081))
    except Exception as e:
        return f'não foi possivel conectar: {e}'
    

    threadListen = threading.Thread(target=listenServer, args=(client,))
    threadListen.daemon = True 
    threadListen.start()

    print('-----Casa de Leilão-----')
    
    while True: 

        bid = input("Lance:\n > ")

        if bid.lower() == 'sair':
            break

        if bid:
            client.send(bid.encode('utf-8'))
    
    client.close()

if __name__ == '__main__':
    runClient()