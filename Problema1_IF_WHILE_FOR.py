n=eval(input('Introduceti numarul de zile:'))
if (n==28) or (n==29):
    print('Luna este februarie')
elif n==30:
    print('Lunile sunt aprilie, iunie, septembrie, noiembrie')
elif n==31:
    print('Lunile sunt ianuarie, martie, mai, iulie, august, octombrie, decembrie')
else: 
    print('Numar de zile inexistent')