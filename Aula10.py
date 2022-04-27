# frutas = {"maça","laranja","abacaxi"}
#     #Isso é chamado de set ou sets, diferente da [] os dados dentro dele ficam aleatórios e não aceitam valores 
#     # duplicados, iguinorando elas.


# print(frutas)
# frutas.add("pera")
# print(frutas)
# frutas.remove("laranja")
# print(frutas)
# frutas.pop()
# print(frutas)

from calendar import calendar


calendário = {
    "Jan":"Janeiro",
    "Fev":"Fevereiro",
    "Mar":"Março",
    "Abr":"Abril",
    "Mai":"Maio",
    "Jun":"Junho",
    "Jul":"Julho",
    "Ago":"Agosto",
    "Set":"Setembro",
    "Out":"Outubro",
    "Nov":"Novembro",
    "Dez":"Dezembro",
}

print(calendário["Abr"]) #Com colchetes um valor que não tem na lista ele vai "quebrar"
print(calendário.get("Deza")) #Com o .get() se ele não encontrar o valor, ele apenas retorna "none"
print(calendário.get("Deza","Não existe"))

print(len(calendário))