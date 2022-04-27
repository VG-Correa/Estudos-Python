# r = Read de leitura
# a = Append de Incrementar
# w = write = escrita
# x = Criar arquivo
# r+ = Leitura + escrita

# arquivo = open("aula12.txt","w")
# arquivo = open("aulateste12.txt","x")


# print(arquivo.readable())
# print(arquivo.writable())

# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines() #readline le apenas a primeira linha, já readlines lê todas


# print(lista)

# arquivo.write("C\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")


# arquivo.close()

import os

# if os.path.exists("aula12.txt"):
#     os.remove("aula12.txt")
# else:
#     print("O arquivo não foi encontrado!")

# os.rmdir("testeaula12")