## Variáveis
numVoltas: int = 0

## Início
numVoltas = int(input("Digite o número de voltas:"))
distancia = int(input("Digite a extensão do circuito em metros:"))
tempo = int(input("Digite a duração em minutos:"))

velocidadeMedia = ((distancia * numVoltas) / 1000) / (tempo / 60)

print("Velocidade média:", velocidadeMedia, "km/h")
## Fim