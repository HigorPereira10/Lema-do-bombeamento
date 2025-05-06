# Lema do Bombeamento para Linguagens Regulares

Este projeto tem como objetivo demonstrar, por meio de testes automatizados em Python, a aplicação do **Lema do Bombeamento** para verificar se uma linguagem formal é **regular** ou **não regular**.

## Descrição

O lema do bombeamento é uma ferramenta teórica usada para provar que certas linguagens **não são regulares**. O código deste projeto realiza testes com cadeias e verifica, conforme o lema, se há uma violação ao bombear partes da cadeia — o que indicaria que a linguagem é não regular.

Foram implementados dois arquivos principais:

- `lema_regular.py` → Aplica o lema a uma **linguagem regular**.
- `lema_nao_regular.py` → Aplica o lema a uma **linguagem não regular**.

Ambos os scripts recebem como entrada uma cadeia `w` e um valor de bombeamento `p`, e exibem todas as divisões possíveis de `w = xyz`, testando os valores de `i` para `xy^i z`.

## 📌 Linguagens utilizadas

- Python 3.x




