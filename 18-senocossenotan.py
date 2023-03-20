'''import math
angulo = float(input('Digite um angulo: '))
math.radians(angulo)
print('O ângulo {} tem o seno de {:.2f}' .format(angulo, math.sin(math.radians(angulo))))
print('O ângulo {} tem o cosseno de {:.2f}' .format(angulo, math.cos(math.radians(angulo))))
print('O ângulo {} tem a tangente de {:.2f}' .format(angulo, math.tan(math.radians(angulo))))'''
#Nesses casos precisamos usando o math.radians para converter a medida para radianos,
# isso é coisa de matematica,
# mas pra fazer esse calculo precisa estar em radianos..
from math import sin, radians, cos, tan
angulo = float(input('Digite um angulo: '))
print('O ângulo {} tem o seno de {:.2f}' .format(angulo, sin(radians(angulo))))
print('O ângulo {} tem o cosseno de {:.2f}' .format(angulo, cos(radians(angulo))))
print('O ângulo {} tem a tangente de {:.2f}' .format(angulo, tan(radians(angulo))))