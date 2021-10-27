"""
08. match_ends

Dada uma lista de strings, retorne a contagem do número de
strings onde o comprimento da cadeia é 2 ou mais e o primeiro
e o último caracteres da cadeia são os mesmos.

PS: Python não possui o operador ++, porém += funciona.
"""

def match_ends(words):
    # +++ SUA SOLUÇÃO +++
    # count = 0
    # for x in words:
    #     if len(x) > 1:
    #         a = x[0]
    #         b = x[-1]
    #         if a == b and len(x) > 1:
    #             count += 1
    # return count

    # new_list = []
    # for n in words:
    #     if len(n) > 1 and n[0] == n[-1] :
    #         new_list.append(n)
    # return len(new_list)

    # M = [x for x in words if len(x) > 1 and x[0] == x[-1]]
    # return len(M)

    def is_even(x):
        return len(x) > 1 and x[0] == x[-1]
    even_numbers = (number for number in words if is_even(number))
    lt = len(list(even_numbers))
    return lt

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
    test(match_ends, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends, ['aaa', 'be', 'abc', 'hello'], 1)
