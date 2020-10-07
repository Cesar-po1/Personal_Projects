print('============================')
print('Piedra, paple o tijera setup')
while True:
    username = input('Escoge un usuario: ')
    password = input('Escoge una contraseña: ')
    passwordconf = input('Vuelve a introducir contraseña: ')
    
    if password!=passwordconf:
        print('No son las mismas contraseñas. Intente de nuevo')
    
    if password == passwordconf:
        print('Cuenta creada exitosamente')
        print()
        print()
        print()
        print()
        print()
        textfile = open('cuentas1.txt', 'a')
        textfile.write('\n')
        textfile.write(username)
        textfile.write('\n')
        textfile.write(password)
        textfile.close()
        import Programa.py
