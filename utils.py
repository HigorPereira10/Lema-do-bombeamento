# utils.py

# Função que aplica o lema do bombeamento a uma determinada linguagem e cadeia.
def lema_do_bombeamento(linguagem, p, cadeia):
    print(f"Analisando a cadeia: {cadeia}")
    print(f"Comprimento de w: {len(cadeia)}, p = {p}")
    print("Testando todas as divisões possíveis w = x + y + z com |xy| ≤ p e |y| ≥ 1...\n")

    # Percorre todas as possíveis divisões de w em x, y, z
    for i in range(p + 1):
        for j in range(i + 1, p + 1):
            x = cadeia[:i]
            y = cadeia[i:j]
            z = cadeia[j:]

            # Garante que y não seja vazio
            if len(y) == 0:
                continue

            print(f"Divisão: x = '{x}', y = '{y}', z = '{z}'")

            # Testa com diferentes valores de i para verificar se a cadeia bombeada ainda pertence à linguagem
            for k in range(0, 4):  # Testa com i = 0 a 3
                bombeada = x + y * k + z
                resultado = linguagem(bombeada)

                status = "PERTENCE à linguagem" if resultado else "NÃO pertence à linguagem"
                print(f"  i = {k}: '{bombeada}' -> {status}")

                if not resultado:
                    print(">> Quebra do lema detectada com essa divisão!\n")
                    return False

            print()

    print("Nenhuma quebra detectada com as divisões possíveis.")
    print(">> Conclusão: A linguagem PODE SER regular (nenhuma quebra encontrada).\n")
    return True
