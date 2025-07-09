frase = 'angelo miguel'

frase_facilitada = frase.lower()
i = 0
guarda_letra = ' '
qtd_apareceu = 0
letra_apareceu_mais_vezes = ' '

while i < len(frase_facilitada):
    letra = frase_facilitada[i]
    contador_letras = frase_facilitada.count(letra)

    if contador_letras > qtd_apareceu:

        if letra == ' ':
            i += 1
            continue

        else:
            qtd_apareceu = contador_letras
            letra_apareceu_mais_vezes = letra

    i += 1

print(f'A letra que mais aparece na frase dada é "{letra_apareceu_mais_vezes}"',\
      f'e a quantidade dessa é ({qtd_apareceu})')   