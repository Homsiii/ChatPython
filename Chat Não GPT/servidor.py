import socket
import threading

def handle_client(conexao, endereco_cliente):
    while True:
        # Recebe os dados do cliente
        dados = conexao.recv(1024).decode()
        if not dados:
            break
        print(f'Dados recebidos do cliente {endereco_cliente}: {dados}')
        
        # Separa o IP e a mensagem recebida
        ip_destino, mensagem = dados.split(':')
        
        # Envia a mensagem para o IP de destino
        enviar_mensagem(ip_destino, mensagem, endereco_cliente)
    
    # Fecha a conexão com o cliente
    conexao.close()
    print(f'Conexão encerrada com {endereco_cliente}')

def enviar_mensagem(ip_destino, mensagem, remetente):
    for cliente in clientes_conectados:
        if cliente['ip'] == ip_destino:
            msg_envio = f'{remetente}:{mensagem}'
            cliente['conexao'].send(msg_envio.encode())

def servidor():
    # Cria um socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define o endereço IP e porta do servidor
    endereco_servidor = ('', 5000)
    
    # Vincula o socket a um endereço e porta
    servidor_socket.bind(endereco_servidor)
    
    # Habilita o servidor para aceitar conexões
    servidor_socket.listen(5)
    
    print('Servidor aguardando conexões...')
    
    while True:
        # Aguarda por uma conexão
        conexao, endereco_cliente = servidor_socket.accept()
        print(f'Conexão estabelecida com {endereco_cliente}')
        
        # Adiciona o cliente à lista de clientes conectados
        cliente = {
            'ip': endereco_cliente[0],
            'conexao': conexao
        }
        clientes_conectados.append(cliente)
        
        # Cria uma nova thread para lidar com o cliente
        client_thread = threading.Thread(target=handle_client, args=(conexao, endereco_cliente))
        client_thread.start()

clientes_conectados = []  # Lista para armazenar os clientes conectados
servidor()
