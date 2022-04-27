#i = 0

#while i < 10:
#    print(i)
#    i +=1

#print("Terminou")
#print(i)

#print("--------------------------------------------------")

#crianças = ["Frederico","Bryan","Rodrigo"]

#for item in crianças:
#    print(item)

#print("--------------------------------------------------")

#canal = "Refatorando"

#for letra in canal:
#    print(letra)

#print("--------------------------------------------------")

#teste individual

# Lista_de_nomes = []


# def AdicionarNome():
#     Lista_de_nomes.append(input("Qual nome quer colocar na lista? "))
#     print(Lista_de_nomes)

# while len(Lista_de_nomes) < 5: 
#     if input("Quer adicionar um novo nome? ") == "Sim":
#         AdicionarNome()
#         print(len(Lista_de_nomes))

# print("Terminou")

#print("--------------------------------------------------")

sabores = ["Chocolate","Morango","Abacaxi"]

# for sabor in sabores:
#     print(sabor)

print("--------------------------------------------------")

canal = "Refatorando"

# for letra in canal:
#     print(letra)

# for index in range(20): #range conta quantos índices exitem.
#     print(index)

# for index2 in range(6,12,2):
#     print(index2)

# for index3 in range(len(sabores)):
#     print(sabores[index3],index3)
    
# for index4 in range(5):
#     if index4 == 0:
#         print(f"primeira linha {index4}")
#     else:
#         print(f"outras linhas {index4}")

matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
      [0]
]

for linha in matrix_numeros:
    # print(linha)
    for coluna in linha:
        print(coluna)