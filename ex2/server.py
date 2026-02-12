import socket   
import threading

highestBid = 0.0
connectedClients = []
lock = threading.Lock() # Serve para evitar race condition 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8081))
server.listen()

print("Servidor de leilão iniciado na porta 8081...")

def manage_client(conn, addr):
    global highestBid
    global connectedClients

    with lock:
        connectedClients.append(conn)
         
    try:
        while True:
            data = conn.recv(1024).decode('utf-8').strip()
            if not data: break
            
            bid = float(data)


            try: 
                bid = float(data)
                with lock:
                    if bid > highestBid:
                        highestBid = bid
                        reply = f'NOVO LANCE: {highestBid} por {bid}'

                        for i in connectedClients:
                            i.send(reply.encode('utf-8'))
                    else:
                        conn.send('LANCE RECUSADO: Valor baixo'.encode('utf-8'))
            except ValueError:
                conn.send("ERRO: Formato invalido".encode('utf-8'))         
    except Exception as e:
        print(f'Erro com o cliente {addr}: {e}')
    finally:
        with lock:
            connectedClients.remove(conn)
        conn.close()

   

while True: 
    conn, addr = server.accept()

    thread = threading.Thread(target=manage_client, args=(conn, addr))
    thread.start()