#Piedra, papel y tijeras
import time
print('Hecho por cesar Ponce')
print('Juego piedra, papel o tijera')
print()
loose = ('La computadora gana')
win = ('Tu ganas')
lives = 3
score = 0
drew = 0
complives = 3
passwordlist=[]
while True:
    print ('Para empezar llena la siguiente informacion')
    cuenta = input('''Si ya tienes cuenta escribe 'y' y si no tienes escribe 'n'  ''')
    print()
    if cuenta == 'y' or cuenta == 'n':
        
        if cuenta == 'n':
            import cuentassetup.py

        if cuenta == 'y':
            username = input('Pon tu nombre de usuario: ')
            password = input('Pon tu contraseña: ')
            searchfile = open('cuentas1.txt','r')
            for line in searchfile:
                passwordlist.append(line.strip())
                if username and password in passwordlist:
                    print('cargando...')
                    time.sleep(0.9)
                    print('cargando...')
                    time.sleep(0.9)
                    print('cargando...')
                    time.sleep(0.9)
                    print('Acceso concedido')
                    print()
                    print()
                    print()
                    time.sleep(0.9)
                    print ('PIEDRA'.center(50,' '))
                    print('PAPEL'.center(51,' '))
                    print('O'.center(50,' '))
                    print('TIJERA'.center(50,' '))
                    time.sleep(1.3)
                    print()
                    print()
                    print()
                    print('Bienvenido al juego')
                    print()
                    time.sleep(0.5)
                    print('''Escribe 'reglas' para ver las reglas ''')
                    print('''Escribe 'puntuacion' para ver tu puntuacion hasta el momento ''')
                    print('''Escribe 'vidas' para ver las vidas que te quedan ''')
                    print('''O escribe 'jugar' para empezar a jugar ''')
                    print('''O escribe 'salir' para salir del juego ''')
                    print('-------------------------------------------------')
                    print('TODAS las instrucciones se escriben en minusculas')
                    print('-------------------------------------------------')
                    print()

                    while True:
                        print('Estas en el menu principal')
                        print()
                        rps = input('¿Que quieres hacer? ')
                        print()
                        if rps == 'salir':
                            print('Gracias por jugar')
                            print('El juego se reiniciara en unos segundos')
                            print()
                            print()
                            print()
                            print()
                            print()
                            print()
                            print()
                            print()
                            print()
                            print()
                            print()
                            import time
                            time.sleep(5)
                            import Programa.py
                        if rps == 'reglas':
                            print()
                            print('+++++++++++++++++++++++++++++++++')
                            print('REGLAS   REGLAS   REGLAS   REGLAS')
                            print()
                            print('Estas son las reglas')
                            print('*****************************')
                            print()

                        if rps == 'vidas':
                            print(lives)
                            print()
                            
                        if rps == 'puntuacion':
                            print(score)
                            print()
                            
                        if rps == 'empates':
                            print(drew)
                            print()
                            
                        if rps == 'jugar':
                            while True:
                                rps=input ('Piedra, papel o tijera? ')
                                import random
                                computer = ('piedra', 'papel', 'tijera',)
                                computer = random.choice(computer)
                                #piedra
                                if rps == 'piedra' and computer == 'papel':
                                    print('La computadora escogio',computer)
                                    print()
                                    print(loose)
                                    print()
                                    print()
                                    lives-=1
                                if rps == 'piedra' and computer == 'tijera':
                                    print('La computadora escogio',computer)
                                    print()
                                    print(win)
                                    complives-=1
                                    print()
                                    print()
                                    score+=1
                                #papel
                                if rps == 'papel' and computer == 'piedra':
                                    print('La computadora escogio',computer)
                                    print()
                                    print(win)
                                    complives-=1
                                    print()
                                    print()
                                    score+=1
                                if rps == 'papel' and computer == 'tijera':
                                    print('La computadora escogio',computer)
                                    print()
                                    print(loose)
                                    print()
                                    print()
                                    lives-=1
                                #tijeras
                                if rps == 'tijera' and computer == 'papel':
                                    print('La computadora escogio',computer)
                                    print()
                                    print(win)
                                    complives-=1
                                    print()
                                    print()
                                    score+=1
                                if rps == 'tijera' and computer == 'piedra':
                                    print('La computadora escogio',computer)
                                    print()
                                    print(loose)
                                    print()
                                    print()
                                    lives-=1
                                 #duplicados
                                if rps == computer:
                                    print('La computadora escogio',computer)
                                    print()
                                    print('Empate')
                                    print()
                                    print()
                                    drew+=1
                                #sistema
                                if rps == 'reglas':
                                    print()
                                    print('+++++++++++++++++++++++++++++++++')
                                    print('REGLAS   REGLAS   REGLAS   REGLAS')
                                    print()
                                    print('Estas son las reglas')
                                    print('*****************************')
                                if rps == 'vidas':
                                    print('Te restan ', lives ,' vidas.')
                                if rps == 'puntuacion':
                                    print('Tu puntuacion hasta el momento es ',score)
                                if rps == 'empates':
                                    print(drew)
                                #lives
                                if lives == 0 or rps == 'test':
                                    print('Gracias por jugar')
                                    print('Has perdido , te quedaste sin vidas')
                                    print('Ganaste ', score, ' veces')
                                    print('Tuviste ', drew, ' empates')
                                    stop = input('Presiona enter para salir y regresar al menu principal')
                                    import time
                                    time.sleep(3)
                                    print()
                                    print()
                                    break
                                if complives == 0:
                                    print('Ganaste')
                                    print('La computadora perdio todas las vidas')
                                    print('Ganaste ', score, ' veces')
                                    print('Tuviste ', drew, ' empates')
                                    stop = input('Presiona enter para salir y regresar al menu principal')
                                    import time
                                    time.sleep(3)
                                    print()
                                    print()
                                    break
                                #exit
                                if rps == 'salir':
                                    print()
                                    print()
                                    break
                    
            else:
                print('Acceso denegado')
                print('Tu usuario o contraseña son incorrectos')
                print('---------------------------------------')
                print()
