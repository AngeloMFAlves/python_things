palavra_secreta = "brutal"
letras_certas = ''
tentativas = 0
nao_acertou = True

while nao_acertou:
    tentativa = input("Digite uma letra: ")

    if len(tentativa) > 1:
        print('Digite apenas uma letra!')
        continue

    if tentativa in palavra_secreta:
        letras_certas += tentativa

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta

        if letra_secreta not in letras_certas:
            palavra_formada += '*'
    tentativas += 1
    print (palavra_formada)

    if palavra_formada == palavra_secreta:
        nao_acertou = False

    else:
        continue
    
print (f'Parabéns! Você precisou de {tentativas} para acertar')
