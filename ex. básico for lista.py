# fazer um codigo que exiba os indices dos itens de dentro de uma lista
# mas e se eu quiser fazer diferente?
# pensei em algo só pra testar conhecimento, fazer com strings

lista = ["Maria", "Helena", "Ana", "Angelo", "Brutal"]

for item in range(len(lista)):
    concatenacao_entre_os_ultimos_itens = lista[0]+lista[(len(lista)-1)]
    concatenaçao_entre_o_segundo_e_o_penultimo = lista[1]+lista[(len(lista))-2]
    print(f'O item atual é {lista[item]} e seu indice é {item}')
    
print(f'o primeiro e o ultimo concatenado é\
 {concatenacao_entre_os_ultimos_itens}, a concatenacao entre o segundo e o penultimo é\
 {concatenaçao_entre_o_segundo_e_o_penultimo} e o item do meio é {lista[2]}')