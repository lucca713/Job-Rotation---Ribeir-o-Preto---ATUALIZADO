qtd_termos = int(input('digite ate que termo voce quer que a sequencia de fibonacci vá: '))
numero = int(input('digite o numero que você acha que vai estar na sequencia de fibonacci: '))
ultimo=1
penultimo=1
lista_termo = ['lista do numero de Fibonacci:']
for count in range(2,qtd_termos):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
    lista_termo.append(termo)

    
print(lista_termo)

if numero in lista_termo:
    print(' o numero está na lista de fibonacci')
else:
    print('o numero nao está na sequencia de fibonacci')

