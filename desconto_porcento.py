val = float(input('Qual o preço do seu produto?R$'))
desc = val - (val * .05)
print('O preço do seu produto com 5% de desconto é R${:.2f}'.format(desc))
