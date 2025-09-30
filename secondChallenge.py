# Criar uma função que recebe um número inteiro e retorna a decomposição em números primos em um mapeamento de números, 
# em que a chave é o número primo e o valor a quantidade de ocorrências desse número
# Obs: números primos de até 1 casa


from collections import Counter

def contarPrimos(num: int) -> dict[int, int]:
    primos = {'2', '3', '5', '7'}
    num_str = str(abs(num))  # Ignorar o sinal
    contador = Counter(d for d in num_str if d in primos)
    return {k: v for k, v in contador.items()}

# Exemplos:
print(contarPrimos(2445))     # {2: 1, 5: 1}
print(contarPrimos(1431))     # {3: 1}
print(contarPrimos(1232357))  # {2: 2, 3: 2, 5: 1, 7: 1}
print(contarPrimos(101010))   # {}
