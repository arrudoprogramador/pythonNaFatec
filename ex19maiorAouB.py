## Declaracao de variaveis
numA = int
numB = int
maior = int

## Inicio
numA = int(input("Digite o primeiro valor:"))
numB = int(input("Digite o segundo valor:"))

if(numA > numB):
    maior = numA
elif(numB > numA):
    maior = numB
elif(numB == numA):
    maior = numA

## Saida
print("O maior número é o:", maior)