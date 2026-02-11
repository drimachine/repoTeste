import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))


while True: 

    mensagem = input("> ")

    if mensagem.lower() == "sair":
        break

    client.send(mensagem.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')
    print(f"Servidor: {response}")

client.close()
