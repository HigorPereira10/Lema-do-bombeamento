# lema_bombeamento_regular.py

from utils import lema_do_bombeamento

# Linguagem regular: a^n b^m (qualquer número de a's seguidos de qualquer número de b's)
def linguagem_regular(cadeia):
    # Verifica se só contém 'a' e 'b'
    if set(cadeia) - {'a', 'b'}:
        return False

    i = 0
    while i < len(cadeia) and cadeia[i] == 'a':
        i += 1
    while i < len(cadeia) and cadeia[i] == 'b':
        i += 1

    # A cadeia é válida se só tiver 'a's seguidos por 'b's, sem outros caracteres
    return i == len(cadeia)

# Exemplo de teste com uma cadeia da linguagem
cadeia = "aaabbbbbb"
p = 4  # Valor de bombeamento (pode ser alterado)

# Aplica o lema
lema_do_bombeamento(linguagem_regular, p, cadeia)
