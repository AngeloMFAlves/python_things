# FAZER UMA LISTA DE COMPRAS QUE DEVOLVA O NOME DO ITEM, SEU INDICE E PERMITA EDIÇÕES

lista_compras = [] # definindo uma lista vazia inicial
editar_listas = True # só uma condição pra manter o while rolando
indice_valido = False
import os #usar isso só pra limpar o terminal vez ou outra

while editar_listas: #enquanto o usuario quiser editar a lista
    edita_lista = input("Digite [a]dicionar. Digite [d]eletar. Digite [l]istar. Digite [s]air: ")
    edita_lista_str = str(edita_lista).lower() #coloca tudo em minúsculo pra padronizar as entradas do usuário

    if edita_lista_str.startswith('a'):
        adicionar_lista = input("Digite o item que deseja adicionar: ")
        lista_compras.append(adicionar_lista)

    elif edita_lista_str.startswith('d'):
        deletar_lista = input("Digite o indice do item que deseja deletar da lista: ")

        try:
            deletar_lista_int = int(deletar_lista) #testo se o usuário escreveu mesmo um numero
            lista_compras[deletar_lista_int] in range((len(lista_compras)-1)) #só pra não explodir em erro
            indice_valido = True

        except:
            os.system('cls')
            print ("Digite um valor inteiro e valido para a lista atual!")
            continue
        lista_compras.remove(lista_compras[deletar_lista_int])
        print ("Compra removida com sucesso!")

    elif edita_lista_str.startswith('l'):
        lista_compras_enumeradas = list(enumerate(lista_compras)) #enumero e faço o objeto enumerado ser uma lista
        for item in lista_compras_enumeradas:
            print(item)
            
    elif edita_lista_str.startswith('s'):
        editar_listas = False

    # cada if e elif mais externo só testa com qual letra a frase do usuário começa. dependendo de com letra começar,
    # uma determinadada função é chamada

    else:
        os.system('cls')
        print ("Digite um comando válido!")
        continue

os.system('cls')
print(f'Obrigado por usar nosso programa! Sua lista final é {lista_compras_enumeradas}')