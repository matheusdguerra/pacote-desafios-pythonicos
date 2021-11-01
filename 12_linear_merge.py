"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

from heapq import merge
from collections import deque

def linear_merge(list1, list2):
    # +++ SUA SOLUÇÃO +++

    # l = list1
    # m = list2
    # result = []
    # i = j = 0
    # total = len(l) + len(m)
#
    # while len(result) != total:
    #     if len(l) == i:
    #         result += m[j:]
    #         break
    #     elif len(m) == j:
    #         result += l[i:]
    #         break
    #     elif l[i] < m[j]:
    #         result.append(l[i])
    #         i += 1
    #     else:
    #         result.append(m[j])
    #         j += 1
    # return result

    # def mergeArray(arr1, arr2):
    #     return list(merge(arr1, arr2))

    # arr1 = list1
    # arr2 = list2
    # return(mergeArray(arr1, arr2))

    #['aa', 'xx', 'zz'], ['bb', 'cc']
    res = deque()
    while len(list1 + list2) > 0:
        if list1[-1:] > list2[-1:]:
            res.appendleft(list1.pop())
            print(res)
            print(list1)
        else:
            res.appendleft(list2.pop())
            print(res)
            print(list2)
    return list(res)



    # lista_combinada = list1 + list2
    # lista_combinada.sort()
    # return lista_combinada


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
