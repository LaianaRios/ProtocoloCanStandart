# ------------ Trabalho de Redes Digitais e Industriais ------------
# ---------------- Professor: Diego Stéfano (Dinho) ----------------
# ----------------- Atividade: Formação de Quadros -----------------
# ----------------- Protocolo: CAN 2.0A - STANDART -----------------
# --------- Equipe: Laiana Rios, Robson Barbosa, Samuel Dias -------
# --------------------- Código do Transmissor ----------------------

import socket

from fGeral import *

HOST = "127.0.0.1"                         # Endereco IP do Servidor
PORT = 5000                                # Porta que o Servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (HOST, PORT)
tcp.connect(dest)

print ("PARA SAIR USE CTRL+X\n")

flag = True

while flag:

    print(("-")*150)
    # Envia uma mensagem para o servidor
    msg = input("DIGITE A MENSAGEM EM BINARIO QUE VOCÊ DESEJA ENVIAR: ")

    if(msg == "\x18"):
        flag = False
        break

    print("MENSAGEM RECEBIDA:    ",msg)

    #ENTRA COM O VERIFICADOR DE SEGURANCA
    paridades(msg)

    #DEFINE A CHAVE
    key = "1100010110011001"

    #CODIFICA O CODIGO
    ans = encodeData(msg, key)

    print("MENSAGEM COM CRC:    ",ans)
    
    encap = "0100110001000001000"
    encap2 = "011111111"
    
    ans = str(encap) + ans + str(encap2)
    
    print("MENSAGEM ENCAPSULADA E ENVIADA:    ",ans)

    tcp.send(ans.encode('UTF-8'))
    
    print (str(tcp.recv(1024),"UTF-8"))

tcp.close()
