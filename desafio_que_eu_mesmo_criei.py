# OBJETIVO = FAZER UM CÓDIGO QUE TRABALHE COM OS INTEIROS DENTRO DE UMA LISTA
# 1) FAÇA A MÉDIA x
# 2) O PRODUTO x 
# 3) A SOMA DOS DOIS ÚLTIMOS

lista_inteiros = [1,2,3,4,5,6,7,8,9]
somatoria = 0
produto_termos = 1

for item in range(len(lista_inteiros)):
    somatoria += lista_inteiros[item]
    media = somatoria /len(lista_inteiros)
    produto_termos *= lista_inteiros[item]
    soma_ultimos = lista_inteiros[0] + lista_inteiros[(len(lista_inteiros)-1)]
    
print (f'A media dos valores é {media}, sua somatoria total é {somatoria},\
 o produto entre eles todos é {produto_termos} e a soma dos dois últi\
mos é {soma_ultimos}')