'''coposto = float(input('Comprimento do cateto oposto: '))
cadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (coposto ** 2 + cadjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa)) #essa é a maneira classica de fazer sem importar
'''
'''import math
coposto = float(input('Comprimento do cateto oposto: '))
cadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(coposto, cadjacente)
print('A hipotenusa vai medir {:.2f}' .format(hipotenusa))''' #essa maneira é importando toda a biblioteca
from math import hypot
coposto = float(input('Comprimento do cateto oposto: '))
cadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(coposto, cadjacente) #Assim deve ficar o calculo quando você importa só uma função
print('A hipotenusa vai medir {:.2f}' .format(hipotenusa))