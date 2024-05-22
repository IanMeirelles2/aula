distancias = [
    [0,2,11,6,15,11,1], 
    [2,0,7,12,4,2,15], 
    [11,7,0,11,6,3,13], 
    [6,12,11,0,10,2,1], 
    [15,4,8,10,0,5,13], 
    [11,2,3,2,5,0,14], 
    [1,15,13,1,13,14,0]
    ]

cidades = []
part = int(input("Digite a cidade de partida: "))
quant = int(input("Digite a quantidade de cidades: "))
for i in range(quant):
    cidades.append(int(input("Digite as cidades: ")))

def menor(a):
    caminho = 20
    for cidade in cidades:
        if distancias[a][cidade] < caminho:
            caminho = distancias[a][cidade]
            return cidade, caminho
        else:
            continue

ordem = []
while len(cidades) > 0:
    ddel, cmenor = menor(part)
    cidades.remove(ddel)
    ordem.append(ddel)
    ddel, cmenor2 = menor(ddel)
    cidades.remove(ddel)
    ordem.append(ddel)
    ddel, cmenor3 = menor(ddel)
    cidades.remove(ddel)
    ordem.append(ddel)
    ddel, cmenor4 = menor(ddel)
    cidades.remove(ddel)
    ordem.append(ddel)
    ddel, cmenor5 = menor(ddel)
    cidades.remove(ddel)
    ordem.append(ddel)
    ddel, cmenor6 = menor(ddel)
    cidades.remove(ddel)
    ordem.append(ddel)

total = cmenor + cmenor2 + cmenor3 + cmenor4 + cmenor5 + cmenor6
print("Ordem: ", ordem)
    


    