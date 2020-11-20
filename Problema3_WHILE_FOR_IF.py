n = eval(input('Introduceti variabila n: '))
m = eval(input('Introduceti variabila m (m<n): '))
k=n
while (n % m == 0):
    n = n // m
if (n == 1):
    print('Numarul', k, 'este o putere a lui ', m)
else:
    print('Numarul', k, 'nu este o putere a lui ', m)