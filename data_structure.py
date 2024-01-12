list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print('a) imprima o maior elemento \n')
maior = list[0]
for num in range(0, len(list)):
    if list[num] > maior:
        maior = list[num]
print(f'O maior elemento da lista é: {maior} \n')

print('b) imprima o menor elemento \n')
menor = list[0]
for num in range(0, len(list)):
    if list[num] < menor:
        maior = list[num]
print(f'O menor elemento da lista é: {menor} \n')

print('c) imprima os números pares \n')
pares = []
for num in list:
    if num % 2 == 0:
        pares.append(num)
print(f'Números pares: {pares} \n')

print('d) imprima o número de ocorrências do primeiro elemento da lista \n')
ocorrencias = 0
for num in list:
    if num == list[0]:
        ocorrencias += 1
print(f'O número de ocorrências do número {list[0]} na lista é de: {ocorrencias} \n')

print('e) imprima a média dos elementos \n')
#Contador de itens
divisor = 0
for num in list:
    divisor += 1
#Faz a soma
soma = 0
for num in list:
    soma += num
print(f'A média dos itens da lista é: {soma / divisor} \n')

print('f) imprima a soma dos elementos de valor negativo \n')
#Lista de Negativos
negativos = []
for num in list:
    if num < 0:
        negativos.append(num)
#Soma os itens
soma = 0
for num in negativos:
    soma += num

print(f'A soma dos negativos da lista é: {soma}')