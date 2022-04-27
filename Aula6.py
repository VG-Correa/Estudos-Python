from unittest.result import failfast


familia = ["Victor","Larissa","Paulo","Margarete","Henrique"]
            #  0        1        2         3          4

#Qual_Nome = int(input("Qual o nome você quer? "))


#print(familia[0])
#print(familia[-1])
#print(f"Este é o nome escolhido: {familia[Qual_Nome]}")
#print(familia[2:])
#print(familia[1:4])

#print(familia)
#Troca_nome = int(input("Qual nome você quer trocar? "))
#Novo_Nome = input("Qual o novo nome? ")
#familia[Troca_nome] = Novo_Nome
#print(familia)

familia.extend(["Geralda","Thiago"])
print(familia)
print()

familia.append("Marcos")
print(familia)
print()

familia.insert(2,"Neguinha")
print(familia)
print(familia.index(input("Qual nome quer saber o índice? ")))

familia.remove(input("Qual nome quer remover? "))

print(familia)
print()

familia.pop()
print(familia)
print()

familia.clear()
print(familia)

print(familia.count("Victor"))