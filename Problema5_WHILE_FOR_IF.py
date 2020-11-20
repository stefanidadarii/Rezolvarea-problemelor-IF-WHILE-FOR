an=int(input('anul = '))
an -= 2000
if an % 12 == 0:
    print('Este anul dragon')
if an % 12 == 1:
    print('Este anul sarpe')
if an % 12 == 2:
    print('Este anul cal')
if an % 12 == 3:
    print('Este anul oaie')
if an % 12 == 4:
    print('Este anul maimuta')
if an % 12 == 5:
    print('Este anul cocos')
if an % 12 == 6:
    print('Este anul caine')
if an % 12 == 7:
    print('Este anul porc')
if an % 12 == 8:
    print('Este anul sobolan')
if an % 12 == 9:
    print('Este anul bou')
if an % 12 == 10:
    print('Este anul tigru')
if an % 12 > 10:
    print('Este anul iepure')