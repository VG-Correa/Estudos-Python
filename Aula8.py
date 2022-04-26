Tenho_Sede = False
Tenho_Fome = True
Estou_de_Dieta = True


print("---------------------------------------")
if Tenho_Sede:
    print("Tomar coca")
else:
    print("Ficar Nice")

if Tenho_Fome:
    print("Comer Sanduba")
else:
    print("Ficar mais Nice")

print("---------------------------------------")

if Tenho_Sede and Tenho_Fome:
    print("Vou na cozinha tomar coca e fazer um sanduba")
elif not(Tenho_Sede) and Tenho_Fome:
    print("Vou na cozinha apenas preparar um sanduba")
elif Tenho_Sede and not(Tenho_Fome):
    print("Vou na cozinha apenas beber Coquinha Geladinha")
else:
    print("Vou ficar nice aqui no sofá")

print("---------------------------------------")

def OqueEuFarei():
    if Tenho_Sede and Tenho_Fome:
        print("Vou na cozinha tomar coca e fazer um sanduba")
    elif not(Tenho_Sede) and Tenho_Fome:
        print("Vou na cozinha apenas preparar um sanduba")
    elif Tenho_Sede and not(Tenho_Fome):
        print("Vou na cozinha apenas beber Coquinha Geladinha")
    else:
        print("Vou ficar nice aqui no sofá")

if input("Você está com fome? ") == "Sim":
    Tenho_Fome = True
else:
    Tenho_Fome = False

if input("Você tem sede? ") == "Sim":
    Tenho_Sede = True
else:
    Tenho_Sede = False

OqueEuFarei()

print("---------------------------------------")

