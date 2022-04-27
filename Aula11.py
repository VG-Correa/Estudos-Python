
def Contadedividir():
    try:
        numero1 = int(input("Digite um número: "))
        numero2 = int(input("Digite um outro número para dividir: "))
        print(f"{numero1} dividido por {numero2} é igual a {numero1 / numero2}")
    
    except ZeroDivisionError:
        print("Impossível dividir por zero")
        Contadedividir()
    except ValueError:
        print("Insira um número válido")
        Contadedividir()
    except:
        print("Ocorreu um erro inesperado: ")
        Contadedividir()

    finally:
        print("Sempre executa idependente do que aconteça acima")
        
Contadedividir()

print("----------------------------------------------------------------------------")

