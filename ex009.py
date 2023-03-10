n = float(input('Digite um número para saber sua tabuada de 1 a 10:'))
n2 = n*1
# print(' A sua tabuada é \n 1x{1}={2} \n 2x{1}={3} \n 3x{1}={4} \n 4x{1}={5} \n 5x{1}={6} \n 6x{1}={7} \n 7x{1}={8} \n 8x{1}={9} \n 9x{1}={10} \n 10x{1}={11}' .format(n, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10))
print(' A sua tabuada é \n 1x{n}={1} \n 2x{n}={2} \n 3x{n}={3} \n 4x{n}={4} \n 5x{n}={5} \n 6x{n}={6} \n 7x{n}={7} \n 8x{n}={8} \n 9x{n}={9} \n 10x{n}={10}'.format(n2, n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9, n * 10, n=n))