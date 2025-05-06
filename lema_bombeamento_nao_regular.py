# lema_bombeamento_nao_regular.py

from utils import lema_do_bombeamento

# Linguagem não regular: a^n b^n (mesmo número de a's e b's)
def linguagem_nao_regular(cadeia):
    # Verifica se só contém 'a' e 'b'
    if set(cadeia) - {'a', 'b'}:
        return False

    i = 0
    while i < len(cadeia) and cadeia[i] == 'a':
        i += 1

    num_a = i  # Quantidade de 'a's
    num_b = 0

    while i < len(cadeia) and cadeia[i] == 'b':
        i += 1
        num_b += 1

    # A cadeia é válida se tiver a mesma quantidade de 'a's e 'b's e não contiver outros símbolos
    return i == len(cadeia) and num_a == num_b

# Exemplo de teste com uma cadeia da linguagem
cadeia = "aaabbb"
p = 3  # Valor de bombeamento (pode ser alterado)

# Aplica o lema
lema_do_bombeamento(linguagem_nao_regular, p, cadeia)
