### Chat Não GPT
Este conjunto de códigos implementa um chat em rede simples. O chat consiste em um servidor e vários clientes, cada um conectado a uma única instância do servidor.

O servidor é responsável por receber as mensagens enviadas pelos clientes e encaminhá-las para o destinatário correto. O cliente, por sua vez, pode enviar mensagens para outro cliente conectado ao servidor.

### Requisitos
Este código foi escrito em Python 3 e utiliza o módulo socket para realizar a comunicação em rede. Certifique-se de que o Python 3 está instalado em seu sistema para executar este código.

### Utilização
##  Servidor
Para iniciar o servidor, execute o arquivo servidor.py. O servidor aguardará por conexões de clientes na porta 5000. Quando um cliente se conecta, o servidor adiciona o cliente à lista de clientes conectados e cria uma nova thread para lidar com as mensagens enviadas por esse cliente.

## Cliente
Para iniciar um cliente, execute o arquivo cliente.py. O cliente solicitará que você digite o endereço IP do servidor para se conectar. Em seguida, você poderá enviar mensagens para outros clientes conectados ao servidor. Para enviar uma mensagem, digite o endereço IP do destinatário e a mensagem, separados por dois pontos. Por exemplo: 192.168.0.2:Olá, tudo bem?. O cliente também receberá mensagens enviadas por outros clientes conectados ao servidor.

Para sair do chat, digite exit quando solicitado a digitar uma mensagem.

###Limitações
Este chat em rede simples é apenas uma implementação básica e não possui muitos recursos avançados, como autenticação de usuário, criptografia de mensagens, suporte a múltiplas salas de bate-papo, entre outros. Além disso, não há tratamento de erros robusto, o que pode fazer com que o programa pare de funcionar se ocorrer algum problema durante a execução. Portanto, este código deve ser considerado apenas como uma demonstração de como criar uma aplicação de chat em rede básica.
