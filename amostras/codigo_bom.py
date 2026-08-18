# Calcula a média
def calcular_media(a, b):
    return (a + b) / 2


# Verifica o resultado
def aprovado(media):
    return media >= 7


media = calcular_media(8, 10)

if aprovado(media):
    print('Aprovado')
else:
    print('Reprovado')