frase = str(input("Digite a frase que você quer contar: ")).lower()
i = 0
letra_mais_contada = ''
qtd_mais_contada = 0

while i < len(frase):
    letra = frase[i]
    i +=1
    contador = frase.count(letra)

    if letra == ' ':
        i += 1
        continue

    elif contador > qtd_mais_contada:
        letra_mais_contada = letra
        qtd_mais_contada = contador

print (f'A letra que mais aparece na frase é {letra_mais_contada}\
 e a quantidade da mesma é {qtd_mais_contada}')