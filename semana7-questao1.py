res = []
res.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
cont = 0

for i in range(5):
    if res[i] == '1' or res[i] == 'Sim':
        cont += 1
if cont == 2:
    print('Analise: Suspeito')
elif 3 <= cont <= 4:
    print('Analise: Cumplice')
elif cont == 5:
    print('Analise : Assassino')
else:
    print('Analise: Inocente')
