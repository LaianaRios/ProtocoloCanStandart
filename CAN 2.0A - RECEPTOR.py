# ------------ Trabalho de Redes Digitais e Industriais ------------
# ---------------- Professor: Diego Stéfano (Dinho) ----------------
# ----------------- Atividade: Formação de Quadros -----------------
# ----------------- Protocolo: CAN 2.0A - STANDART -----------------
# --------- Equipe: Laiana Rios, Robson Barbosa, Samuel Dias -------
# --------------------- Código do Receptor -------------------------

import socket

from fGeral import *

HOST = "127.0.0.1"                         # Endereco IP do Servidor
PORT = 5000                                 # Porta que o Servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)
tcp.bind(orig)

print("SERVER INICIADO")
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print ('CONECTADO POR', cliente)

    while True:
        msg = con.recv(1024)
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
