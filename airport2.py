x1 = 10
x2 = 10
x3 = 10
x4 = 10
x5 = 10


def main():
    while True:
        print("Voos disponíveis: AS7012, QX2002, AS2002, 8E880, 8E890")
        voo = input("Qual voo a ser consultado: ")
        if voo == "AS7012":
            resp, x = sis(x1)
            if resp == "Sim":
                continue
            else:
                break
        elif voo == "QX2002":
            resp, x = sis(x2)
            if resp == "Sim":
                continue
            else:
                break
        elif voo == "AS2002":
            resp, x = sis(x3)
            if resp == "Sim":
                continue
            else:
                break
        elif voo == "8E880":
            resp, x = sis(x4)
            if resp == "Sim":
                continue
            else:
                break
        elif voo == "8E890":
            resp, x = sis(x5)
            if resp == "Sim":
                continue
            else:
                break
        else:
            print("Voo inválido")


def sis(x):
    print(f"Este voo possui {x} passagens")
    quant = int(input("Quantidade de passagens: "))
    x -= quant
    if x < 0:
        print("Passagens insuficientes")
        x += quant
    else:
        if x <= 5:
            valor = (quant * 100) + (quant * 100) * 0.20
            print(f"O valor a ser pago é de R${valor}")
        else:
            valor = quant * 100
            print(f"O valor a ser pago é de R${valor}")
        cont = input("Quer continuar sua compra? ")
        return cont, x



main()