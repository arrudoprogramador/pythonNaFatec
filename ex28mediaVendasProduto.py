## Declaracao de variaveis
precoAtual: float = 0
mediaMensal: float = 0
precoNovo: float = 0

## Inicio
precoAtual = float(input("Digite o preço atual do produto: "))
mediaMensal = float(input("Digite a média mensal : "))

if (mediaMensal < 500) and (precoAtual < 30.00):
    precoNovo = precoAtual + (precoAtual * 10 /100)
elif ((mediaMensal >= 500) and (mediaMensal < 1000)) and ((precoAtual >= 30.00) and (precoAtual < 80.00)):
    precoNovo = precoAtual + (precoAtual * 15 /100)
elif (mediaMensal >= 1000) and (precoAtual >= 80.00):
    precoNovo = precoAtual - (precoAtual * 5 /100)
else:
    precoNovo = precoAtual

print("O novo preço será de:", precoNovo)

## Fim
