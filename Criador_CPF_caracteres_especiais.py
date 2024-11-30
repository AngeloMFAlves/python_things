# Gerar o primeiro dígito de um CPF
import random
nove_digitos = str(random.randint(100000000,999999999))
i = 10
j = 11
soma_resultados_prim = 0
soma_resultados_seg = 0

for digito in nove_digitos:
    digito_inteiro = int(digito)
    indice = digito_inteiro * i
    resultado_final = indice * 10
    soma_resultados_prim += resultado_final
    i -= 1
    
resto = soma_resultados_prim%11
if resto > 9:
    prim_digito = 0

else:
    prim_digito = resto

# Gerar o segundo dígito do CPF

CPF_acrescido_sem_digitos = nove_digitos + str(prim_digito)
for digito in CPF_acrescido_sem_digitos:
    digito_inteiro = int(digito)
    indice = digito_inteiro * j
    resultado_final = indice * 10
    soma_resultados_seg += resultado_final
    j -= 1
    
resto = soma_resultados_seg%11
if resto > 9:
    seg_digito = 0

else:
    seg_digito = resto

CPF_gerado = nove_digitos + str(prim_digito) + str(seg_digito)
CPF_format = ''
for digito in CPF_gerado:
    digito_inteiro = int(digito)
    CPF_format += str(digito_inteiro)
    if len(CPF_format) == 3 or len(CPF_format) == 7:
        CPF_format += "."
    if len(CPF_format) ==11:
        CPF_format += "-"
print(f'O CPF gerado, já com os caracteres especiais, é {CPF_format}')