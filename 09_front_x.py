"""
09. front_x

Dada uma lista de strings, retorne a lista com as strings
ordenadas, porém agrupe todas as strings que começam com 'x' primeiro.

Exemplo: ['mix', 'banana' ,'xyz', 'apple', 'xanadu', 'aardvark']
Irá retornar: ['xanadu', 'xyz', 'aardvark', 'apple', 'banana' ,'mix']

Dica: Isso pode ser resolvido criando 2 listas e ordenando cada uma
antes de combina-las.
"""


def front_x(words):
#     return solution_1(words)
#
#
# def solution_1(words):
#     list_init_x = []
#     list_not_init_x = []
#
#     [list_init_x.append(y) for y in words if y.startswith('x')]
#     [list_not_init_x.append(y) for y in words if not y.startswith('x')]
#     return sorted(list_init_x) + sorted(list_not_init_x)


    # new_list_x = []
    # new_list_nao_x = []
    # for string in words:
    #     #print (words,n)
    #     for x in string[0]:
    #         #print(n, x)
    #         if x[0] == 'x' :
    #             new_list_x.append(string)
    #             #print(new_list_x)
    #         else:
    #             new_list_nao_x.append(string)
    #             #print(new_list_a)
    #     new_list_x.sort()
    #     new_list_nao_x.sort()
    # return new_list_x + new_list_nao_x


    # return sorted(words, key=lambda word : word if word[0] == 'x' else f'z{word}')

    new_list_x = [x for x in words if x[:1] == 'x' ]
    new_list_nao_x = [nao_x for nao_x in words if nao_x[:1] != 'x']
    #new_list_x.sort()
    #new_list_nao_x.sort()
    #return new_list_x+new_list_nao_x
    return sorted(new_list_x) + sorted(new_list_nao_x)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_x, ['bbb', 'ccc', 'axx', 'xzz', 'xaa'],
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x, ['ccc', 'bbb', 'aaa', 'xcc', 'xaa'],
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'],
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
