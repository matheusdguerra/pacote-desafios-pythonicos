"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
import math

def front_back(a, b):

    # if len(a) % 2 == 0:
    #     af = a[:int(len(a) / 2)]
    #     at = a[int(len(a) / 2):]
    # else:
    #     af = a[:int(len(a) / 2) + 1]
    #     at = a[int(len(a) / 2) + 1:]
    #
    # if len(b) % 2 == 0:
    #     bf = b[:int(len(b) / 2)]
    #     bt = b[int(len(b) / 2):]
    # else:
    #     bf = b[:int(len(b) / 2) + 1]
    #     bt = b[int(len(b) / 2) + 1:]
    # # return af + bf + at + bt
    # return ''.join([af, bf, at, bt])


    # Soluão 2
    #  user "slice" and "divmod" and join
     #a_front_cont, a_back_cont = divmod(len(a), 2)  # divmod(dividend, divisor)
     #b_front_cont, b_back_cont = divmod(len(b), 2)  # divmod(dividend, divisor)
     #a_front_string = a[:a_front_cont + a_back_cont]
     #a_back_string = a[a_front_cont + a_back_cont:]
     #b_front_string = b[:b_front_cont + b_back_cont]
     #b_back_string = b[b_front_cont + b_back_cont:]
     #return (a_front_string + b_front_string + a_back_string + b_back_string)

    ## pos_a = ceil(len(a) / 2)
    ## pos_b = ceil(len(b) / 2)
    ## final_string = a[:pos_a] + b[:pos_b] + a[pos_a:] + b[pos_b:]
    ## return final_string

        def index(s):
            return math.ceil(len(s) / 2)

        def inicio(s):
            return s[:index(s)]

        def fim(s):
            return s[index(s):]

        return ''.join([inicio(a), inicio(b), fim(a), fim(b)])

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
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')

