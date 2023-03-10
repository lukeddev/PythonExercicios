v1 = input('Digite o que quiser:')
print ('Essa informação é Alfa-numerica? {}' .format(v1.isalnum()))
print ('Essa informação é ASCII? {}' .format(v1.isascii()))
print ('Essa informação é um digito? {}' .format(v1.isdigit()))
print ('Essa informação está em letra minuscula? {}' .format(v1.islower()))
print ('Essa informação é em caixa alta? {}' .format(v1.isupper()))
print ('Essa informação só tem espaços?', v1.isspace())
print ('Essa informação está capitalizada(quando tem maiuscula e minuscula)?', v1.istitle())

