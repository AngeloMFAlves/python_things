while True:
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")
    operador = input("Qual operação quer? (+-/*): ")
    numero_1_float = 0
    numero_2_float = 0
    numeros_validos = False
    operadores_permitidos = "+-/*"
    restricao_para_operar = operador not in operadores_permitidos or len(operador) > 1

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = False
    
    impossibilidade = (numero_2_float == 0 and numero_1_float != 0 and operador == "/")
    indeterminacao = (numero_1_float == 0 and numero_2_float == 0 and operador == "/")

    if numeros_validos is False:
        print(f'Um ou ambos numeros é(são) inválidos')
        continue

    elif restricao_para_operar:
        print (f'Operação inválida')

    elif indeterminacao:
        print (f'Indeterminado! {numero_1_float}/{numero_2_float} é indeterminado, pois admite infinitas soluções. Tente novamente')

    elif impossibilidade:
        print (f'Impossível dividir por 0! Tente novamente')

    elif restricao_para_operar is not True:
        if operador == '+':
            resultado = numero_1_float + numero_2_float
            print(f'({numero_1_float}) + ({numero_2_float}) = {resultado}')
            
        elif operador == '-':
            resultado = numero_1_float - numero_2_float
            print(f'({numero_1_float}) - ({numero_2_float}) = {resultado}')

        elif operador == '*':
            resultado = numero_1_float*numero_2_float
            print(f'({numero_1_float}) * ({numero_2_float}) = {resultado}')

        elif operador == '/':
            resultado = numero_1_float/numero_2_float
            print(f'({numero_1_float}) / ({numero_2_float}) = {resultado}')

        else:
            print(f'Tu fez alguma coisa errada, {operador} nao existe')
        sair = input(f'Quer sair? [s]im: ').lower().startswith('s')

        if sair:
            break