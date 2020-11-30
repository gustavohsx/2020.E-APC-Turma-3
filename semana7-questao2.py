carros = []
consumo = []

for i in range(5):
    carros.append(input('Digite o modelo do carro: '))
    consumo.append(float(input('Digite o consumo do carro {} em km/L: '.format(carros[i]))))
carro = carros[0]
consumo_carro = consumo[0]
for j in range(5):
    if consumo_carro < consumo[j]:
        consumo_carro = consumo[j]
        carro = carros[j]
print('O carro que apresenta o melhor consumo eh {}, com uma media de {} km/L.'.format(carro.upper(), consumo_carro))

litros_comb = []
custo = []
for i in range(5):
    litros_comb.append(float(1000 / consumo[i]))
    custo.append(float(litros_comb[i]) * 2.25)
    print('O {} ira consumir {:.2f} litros para percorrer 1000 km, com o gasto em gasolina sendo de R$ {:.2f}'.format((carros[i]).upper(), litros_comb[i], custo[i]))
