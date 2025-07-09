"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um numero inteiro: ")

try:
    numero_inteiro = int(numero)
    teste_paridade = numero_inteiro%2
    if teste_paridade == 0:
        print (f'({numero_inteiro}) eh um numero par')
    else:
        print (f'({numero_inteiro}) nao eh um numero par')

except:
    print(f'"{numero}" nao eh um inteiro, tente novamente')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario_atual = input("Digite as hora do local que voce esta: ")

try:
    hora_inteira = int(horario_atual)
    dia = hora_inteira >= 5 and hora_inteira <= 11
    tarde = hora_inteira >= 12 and hora_inteira <= 17
    noite = hora_inteira >= 18 and hora_inteira <=23
    madrugada = hora_inteira >= 0 and hora_inteira <= 4

    if dia:
        print("Dia, sô!")

    elif tarde:
        print ("Tarde, ó")

    elif noite:
        print ("Noitchê!")

    else:
        print ("Boa madruga meu fi")

except:
    print ("Por favor, digite apenas horas inteiras")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_usuario = input("Digite APENAS seu primeiro nome: ")

if ' ' in nome_usuario:
    print ("Eh so o primeiro nome, animal")

else:
    if len(nome_usuario) < 1 and len(nome_usuario) <= 4:
        print ("Seu nome eh curto")

    elif len(nome_usuario) >= 5 and len(nome_usuario) <= 6:
        print ("Seu nome eh normal")
        
    elif len(nome_usuario) > 6:
        print ("Seu nome eh muito grande")
    else:
        print ("Digite mais que uma letra, por favor")