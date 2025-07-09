nome = input("Digite seu nome:\n")
idade = (input("Digite sua idade:\n"))

if nome and idade:
    print (f'Seu nome invertido eh {nome[::-1]}')
    if ' ' in nome:
        print (f'Seu nome contem espaços')
    if ' ' not in nome:
        print (f'Seu nome nao contem espacos')
    print (f'Seu nome tem {len(nome)} letras')
    print (f'A primeira letra do seu nome eh {nome[0]}')
    print (f'A ultima letra do seu nome eh {nome[len(nome)-1]}')
if not nome and not idade:
    print ("Desculpe, voce deixou campos vazios")