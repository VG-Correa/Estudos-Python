#def BigMac():
#    print("Sanduiche BigMac")

def fazerBigMac(nome):
    print(f"Sanduíche do {nome}")

def fazerBatata(tamanho):
    print(f"Batata do tamanho {tamanho}")

def prepararRefri(tipo,tamanho):
    print(f"Preparar Refrigerante {tipo} do tamanho {tamanho}")

def fazerComboBigMac(nome_pedido,tamanho_batata,tipo_refri,tamanho_refri):
    fazerBigMac(nome_pedido)
    fazerBatata(tamanho_batata)
    prepararRefri(tipo_refri,tamanho_refri)


Nome_Cleinte = input("Qual o seu nome? ")
TamanhoBatata = input("Qual o tamanho da batata? ")
TipoRefri = input("Qual o refrigerante que você deseja? ")
TamanhoRefri = input("Qual o tamanho do refrigerante? ")

fazerComboBigMac(Nome_Cleinte,TamanhoBatata,TipoRefri,TamanhoRefri)