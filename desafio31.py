# Desenvolva um programa que pergunte a distância de uma viagem em um Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = float(input('Informe quantos quilômetros tem sua viagem: '))
if km <=200:
    preco = km*0.50
    print(f' A sua viagem tem {km:.2f}km e o valor cobrado por sua rota é de \033[31;41mR${preco:.2f}\033[m.')
else:
    preco = km*0.45
    print(f' A sua viagem tem {km:.2f}km e o valor cobrado por sua rota é de \033[31;41mR${preco:.2f}\033[m.')