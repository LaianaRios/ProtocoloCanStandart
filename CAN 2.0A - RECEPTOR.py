# ------------ Trabalho de Redes Digitais e Industriais ------------
# ---------------- Professor: Diego Stéfano (Dinho) ----------------
# ----------------- Atividade: Formação de Quadros -----------------
# ----------------- Protocolo: CAN 2.0A - STANDART -----------------
# --------- Equipe: Laiana Rios, Robson Barbosa, Samuel Dias -------
# --------------------- Código do Receptor -------------------------

# Importar o Socket para poder se comunicar com o servidor
import socket

# Do arquivo fGeral irá importar todas as funções e anexar ao arquivo 
from fGeral import *

# Endereco IP do Servidor
HOST = "127.0.0.1"  

# Porta que o Servidor estar
PORT = 5000                                 

# Irá se conectar ao servidor e permanecerá conectado
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz conexão ao servidor
orig = (HOST, PORT)

# Informa que está aberto para receber dados 
tcp.bind(orig)

print("SERVER INICIADO")

# Fica a espera dos dados
# 1 = Só irá aceitar 1 cliente 
tcp.listen(1)

# Irá executar o código enquanto o servidor estiver aberto
while True:
    
    # Variáveis definidas quando se estabelece uma conexão
    con, cliente = tcp.accept()
    print ('CONECTADO POR', cliente)

    # Recebimento dos dados
    while True:
        
        # 1024 = Faixa de comunicação
        msg = con.recv(1024)
        
        # Se a mensagem não existir, o código dará um break
        if not msg: break

        print("MENSAGEM RECEBIDA: ", cliente, msg)

        #-(Recebe os dados)-

        #-(Analisa a paridade)-

        #-(Retira os Bits)-

        # Mudar a chave EM 16BITS
        key = "1100010110011001"

        # TIRA O BIT INSERIDO!!!!

        ans = decodeData(str(msg, "ascii"), key)
        print("RESTANTE APÓS A DECODIFICAÇÃO: " + ans)
        #-(Verificação de erro - CRC)-

        temp = "0" * (len(key) - 1)

        if ans == temp:
            print("THANKS. DADOS: <SAIDA>" + str(msg, "ascii") + "</SAIDA> NENHUM ERRO ENCONTRADO")
            con.send("OBRIGADA POR CONECTAR -> NENHUM ERRO ENCONTRADO".encode())
        else:
            print("ERRO NOS DADOS")
            con.send("OBRIGADA POR CONECTAR -> ERRO NOS DADOS".encode())
        #-(Comparar)-

    print('FINALIZANDO CONEXÃO DO CLIENTE', cliente)

    con.close()

print("SERVER FECHADO")
