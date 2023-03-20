dias = int(input('Por quantos dias você alugou o carro?'))
km = float(input('Quantos km você rodou com o carro?'))
pago = (60 * dias) + (0.15 * km)
print('O valor total a pagar é R${:.2f}'.format(pago))