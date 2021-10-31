"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""

def remove_adjacent(nums):
    lista = []
    for x in nums:
        if x != nums[1]:
            lista.append(x)
    return lista

###############################################################
def findAdjacentElements(test_list):
    res = []
    for idx, ele in enumerate(test_list):

        if idx == 0:
            if test_list[idx] != test_list[idx + 1]:
                res.append(test_list[idx])

        elif idx == len(test_list) - 1:
            if test_list[idx] != test_list[idx - 1]:
                res.append(test_list[idx])

        elif test_list[idx] != test_list[idx + 1]:
            res.append(test_list[idx])

    return res


# Initializing list
input_list = [2, 2, 7, 3, 3, 3, 4, 4, 9, 9]

# printing result
print("The Adjacent elements list:", findAdjacentElements(input_list))


###############################################################




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
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
