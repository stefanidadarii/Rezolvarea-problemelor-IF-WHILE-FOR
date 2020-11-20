from fractions import Fraction
a = int(input('Primul numarator = '))
b = int(input('Primul numitor = '))
x = int(input('Al doilea numarator = '))
y = int(input('Al doilea numitor = '))
s = Fraction(a,b) + Fraction(x,y)   
p = Fraction(a,b) * Fraction(x,y)   
print('a) suma =', s)   
print('b) produsul =', p)     