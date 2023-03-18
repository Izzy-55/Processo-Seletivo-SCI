# Solicitar a inserção de 5 números, ao final, imprimir os números pares, números ímpares e a média geral desses números.

numeros_usuario = list(map(int, input("Insira 5 números, separados por espaço: ").split()))

soma = sum(numeros_usuario)
media = soma / len(numeros_usuario)
print(f"Esta é a média: {media}")

for numeros in numeros_usuario:
    if numeros % 2 == 0:
        print(numeros, "É um número par") 
    elif numeros % 3 == 0:
        print(numeros, "É um número ímpar")
    else:
        print(numeros, "É um número ímpar")
        