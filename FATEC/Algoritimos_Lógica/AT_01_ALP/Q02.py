import os


valor_imovel = float(input('Digite o valor do imóvel a ser adquirido: '))

salario_bruto = float(input('Digite o valor do salário Bruto atual: '))

meses = int(input("Digite a quantidade de meses para a prestação: "))



if meses > 240:
    print('A quantidade de meses supera 240 prestações!')
elif meses <= 0:
    print('Digite um número de prestações maior que zero e menor ou igual a 240')

prestações = round(valor_imovel / meses,2)

proporção = salario_bruto * 0.30

if prestações > proporção:
    os.system('clear')
    print('O valor da prestação supera 30% do salário bruto! impossível adquirir o imóvel.')
    print(f'''##########################################################################################
Para conseguir o empréstimo de {valor_imovel} por {meses} meses:

É preciso um salário de R${round(((valor_imovel/meses)/30)*100,2)}
Com prestações de R${round((valor_imovel/meses)*0.3,2)}

##########################################################################################

Para conseguir o empréstimo com o salário mencionado, seria preciso parcelar o imóvel em {round((valor_imovel/(salario_bruto*0.3)))} vezes''')

else:
    os.system('clear')
    print(f"""##########################################################################################
    
Empréstimo APROVADO!!

Salário Bruto: R${round(salario_bruto,2)}
Valor do imóvel: R${round(valor_imovel,2)}

Meses: {meses} meses
Prestação: R${prestações}

##########################################################################################""")
