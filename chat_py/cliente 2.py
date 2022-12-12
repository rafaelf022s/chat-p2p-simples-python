import socket
import random


def main():
    print("Bem vindo ao chat TCP em Pyton\n")
    print("[ 1 ] Iniciar uma sala local \n[ 2 ] Conectar em uma sala local \n[ 3 ] Sair\n")
    opcao = input("Digite a opcao desejada: ")
    if opcao == '1':
        cria_servidor()
    elif opcao == '2':
        conecta_cliente()
    elif opcao == '3':
        print("Programa finalizado, volte sempre")
        exit(0)


def cria_servidor():
    ip = input("Digit o ip do servidor: ")
    porta = random.randint(1000, 9999)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((ip, porta))
    print(f"Servidor inicializado! IP: {ip}, Porta: {porta}")
    servidor.listen()
    client, addr = servidor.accept()
    print(f'{addr}, conectou-se ao servidor')

    while True:
        msg = client.recv(2048).decode('utf-8')
        if msg == '/q':
            break
        else:
            print(f'{addr} diz: {msg}')
        client.send(input('Mensagem: ').encode('utf-8'))
    client.close()
    servidor.close()


def conecta_cliente():
    ip = input('Digite o ip do servidor que deseja conectar: ')
    porta = int(input('Digite a porta do servidor que deseja conectar: '))
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ip, porta))
    while True:
        cliente.send(input('Mensagem: ').encode('utf-8'))
        msg = cliente.recv(2048).decode('utf-8')
        if msg == '/q':
            cliente.close()
            break
        else:
            print(f'{ip,porta} diz: {msg}')


main()
