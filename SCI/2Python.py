# Solicitar 5 números, ao fim, imprimir o número maior e o número menor.

numeros = list(map(int, input("Insira os números desejados: ").split()))

menor = min(numeros)
maior = max(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
