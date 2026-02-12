import socket 

dataBase = {
    "HGLG11": {"preco": "160.00", "provento": "1.10"},
    "KNRI11": {"preco": "155.50", "provento": "0.80"},
    "MXRF11": {"preco": "10.50", "provento": "0.12"}
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8080))
server.listen(1)

while True:
    conn, addr = server.accept()
    try:
        while True:
            
            data = conn.recv(1024).decode('utf-8').strip()

            if not data:
                break

            resposta = "ERRO: Requisição inválida"

            if ";" in data:
                partes = data.split(";", 1)
                comando = partes[0].strip().upper()
                ticker = partes[1].strip().upper()

                if ticker in dataBase:
                    fii = dataBase[ticker]

                    if comando == "PREÇO" or comando == "PRECO":
                        resposta = fii["preco"]
                    elif comando == "PROVENTO":
                        resposta = fii["provento"]
                    elif comando == "STATUS":
                        resposta = f"{ticker}: R${fii['preco']} Div: R${fii['provento']}"
                    else:
                        resposta = "ERRO: Comando invalido"
                else:
                    resposta = "ERRO: FII nao encontrado"

            conn.send(resposta.encode('utf-8'))

    except Exception as e:
        print(f"Erro no processamento: {e}")
    finally:
        conn.close()