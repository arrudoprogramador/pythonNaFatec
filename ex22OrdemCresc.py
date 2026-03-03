## Declaracao de variaveis
numA = int
numB = int

## Inicio
numA = int(input('Digite o primeiro valor:'))
numB = int(input('Digite o segundo valor:'))

## Saida
if(numA < numB):
    print(numA, ",", numB)
elif(numA > numB):
    print(numB, ",", numA)
else:
    print(numA, ",", numB)

