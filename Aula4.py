minha_string = " hello World  "
               #01234567891111
               #          0123
               #Todas as Strings iniciam em 0!



print(minha_string)
    #Printa ou escreve no console o que estiver armazenado na variável "minha_string"

print(minha_string.upper())
    #Printa o que estiver na variável, mas com todas as letras em MAIÚSCULO.

print(minha_string.lower())
    #Printa todas as letras em minúsculo

print(minha_string.capitalize())
    #Printa apenas a primeira letra em MAIÚSCULO e as demais em minúsculo

print(minha_string.isupper())
    #isupper verificar se a variável é uma String que está com todos seus caracteres em MIÚSCULO  e retorna Verdadeiro ou Falso

print(minha_string.islower())
    #lower faz a mesma coisa que o isupper, mas com minúsculas

print(minha_string.strip())
    #Strip retira os espaços das extremidades da variável

print(minha_string.replace("hello","Bye"))
    #Procura dentro da variável a chave que pode ser uma string e substitui ela pelo segundo argumento

print(minha_string.replace("o","O",1))
    #Colocando o terceiro argumento, você limita a quantidade de chaves que serão mudadas dentro da variável.

print(len(minha_string))
    #Faz a contagem de quantos caracteres existem dentro da variável

print(minha_string[2:5]) 
    #Printa no console apenas o caractere respectivo do número entre []
    #Colocando ":" você deixa um intervalo entre um número e outro que vai ser printado
    #Colocando os números em negativo, ele pesquisa de trás para frente (considerando que o último caractere não é 0)

print(minha_string.index("o"))
    #Retorna o n° do caractere que está pesquisando dentro de uma variável

#--------------------------------------------------------------------------------------------------------------------
x = "World" in minha_string
    #Verifica se o texto "World" pode ser encontrado na variável minha_string

print(x)

#--------------------------------------------------------------------------------------------------------------------
lista_exemplo = "Linha1\nLinha2\nLinha3"
    #o "\" é um caractere de escape, utilizando ele junto com o "n" ele faz com que o console printe um "Enter"

print(lista_exemplo)
#--------------------------------------------------------------------------------------------------------------------


