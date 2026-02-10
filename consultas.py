import socket 

dataBase = {
    "HGLG11": {"preco": "160.00", "provento": "1.10"},
    "KNRI11": {"preco": "155.50", "provento": "0.80"},
    "MXRF11": {"preco": "10.50", "provento": "0.12"}
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("0.0.0.0", 8080))
socket.listen(1)

while True:
    conn, addr = server.accept()
    try:
        dataBase = conn.recv(1024).decode('utf-8').strip()

        if ";" in dataBase: 
            comando, ticker = dataBase.split(";")
            
    except: