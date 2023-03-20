real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.25
euro = real / 5.62
print('Com R${:.2f} você pode comprar US${:.2f} e também EUR€{:.2f}' .format(real, dolar, euro))
