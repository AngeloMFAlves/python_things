# Gerar o primeiro dígito de um CPF
CPF = "233.942.570-09"
i = 10
CPF_sem_caracteres_especiais = ''
soma_resultados = 0


for caractere in CPF:
    if caractere == '.':
        continue

    elif caractere == '-':
        continue

    else:
        digito = caractere
        CPF_sem_caracteres_especiais += digito
        CPF_sem_digitos = CPF_sem_caracteres_especiais[:9]
        digitos = CPF_sem_caracteres_especiais[9:]

for digito in CPF_sem_digitos:
    CPF_inteiro = CPF_sem_digitos
    digito_inteiro = int(digito)
    indice = digito_inteiro * i
    resultado_final = indice * 10
    soma_resultados += resultado_final
    i -= 1
    
resto = soma_resultados%11
if resto > 9:
    prim_digito = 0

else:
    prim_digito = resto

print(f'O primeiro digito do CPF é {prim_digito}')
