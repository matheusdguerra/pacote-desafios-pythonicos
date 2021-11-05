"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys

from operator import itemgetter

# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
def print_words(filename):

    # Lê arquivo TXT
    arquivo = open('letras.txt', 'r')
    lista = arquivo.readlines()
    lista_repalce = []

    # Remove \n
    for string in lista:
        new_string = string.replace("\n", "")
        lista_repalce.append(new_string)

    # lower em todos os caracteres
    for i in range(len(lista_repalce)):
        lista_repalce[i] = lista_repalce[i].lower()

    # Converte lista em string
    lista_srt = ''.join(lista_repalce)

    # Remove ',' e espaço em branco
    # Gera string final
    lista_srt = lista_srt.replace(",", "").replace(" ","")

    # Coleta distinct da string
    # Ordena distinct em ordem alfabetica
    distinct_char = "".join(set(lista_srt))
    sorted_characters = sorted(distinct_char)
    a_string = "".join(sorted_characters)

    for char in a_string:
        x = lista_srt.count(char)
        print(char, x)

    arquivo.close()


def print_top(filename):
    # Lê arquivo TXT
    arquivo = open('letras.txt', 'r')
    lista = arquivo.read()

    lista = lista.lower()
    lista = lista.split()


    # Coleta distinct da string
    distinct_char = "".join(set(lista))


    # conta char e cria dicionario
    lista_append = []
    for char in distinct_char:
        count = lista.count(char)
        lista_nova = [char, count]
        lista_append.append(lista_nova)

    lista_append = sorted(lista_append, key=itemgetter(1), reverse=True)
    print(lista_append)

    for x in lista_append:
        print(x)

    arquivo.close()
    # b 4
    # c 3
    # a 2

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
