import socket 
import threading

def receber_mensagem(cliente_socket):
    while True:
        # recebe as mensagens do servidor 
        mensagem = cliente_socket.recv(1024).decode()
        ip_origem, mensagem_recebida = mensagem.split(':')
        print(f'Mensagem recebida do IP {ip_origem}: {mensagem_recebida}')

def cliente():
    # cria um socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # define o endereço IP do servidor
    endereco_servidor = ('10.28.0.132',5000)
    
    try:
        # estabelece a conexao com o servidor 
        cliente_socket.connect(endereco_servidor)
        
        # inicia as threads de conversacao
        thread_receber = threading.Thread(target=receber_mensagem, args = (cliente_socket))
        thread_receber.start()
        
        while True:
            # solicita a mensagem do usuario
            mensagem = input("Digite uma mensagem (exit = sair): ")
            
            if mensagem == 'exit' :
                break
            
            # solicita o IP do destino 
            destino_ip = input("Digite o IP de destino: ")
            
            # combina o IP de destino com a mensagme 
            mensagem_envio = f'{destino_ip}:{mensagem}'
            
            # envia a mensagem ao servidor
            cliente_socket.send(mensagem_envio.encode())
            
    finally:
        #fecha a conexao com o servidor
        cliente_socket.close()

cliente()