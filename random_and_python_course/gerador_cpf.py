# Gerar o primeiro dígito de um CPF
import random
nove_digitos = ''
for n in range(0,9):
    nove_digitos += str(random.randint(0,9))
i = 10
j = 11
CPF_sem_caracteres_especiais = ''
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
print(f'O CPF gerado é {CPF_gerado}')