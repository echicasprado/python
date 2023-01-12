import random
person = 0
computer = 0
options = {'piedra':1,'papel':2,'tijera':3}

while True:
    inputPerson = input('Seleciona una opción: piedra, papel, tijera\n')
    inputComputer = random.choice(list(options.keys()))

    print('Tu elegiste: {0}'.format(inputPerson))
    print('Computadora elegio: {0}'.format(inputComputer))

    personSelect = options.get(inputPerson.lower())
    computerSelect = options.get(inputComputer.lower())

    if(personSelect == None):
        print('Elegiste mal 😥')
    elif(personSelect == computerSelect):
        print('Empate!😶😶😶')
    elif ((personSelect == 1 and computerSelect == 3) or (personSelect == 2 and computerSelect == 1) or (personSelect == 3 and computerSelect == 2)):
        person += 1
        print('Ganaste 🥳🥳🥳')
    else:
        computer += 1
        print('Perdiste ❌❌❌')

    if(person > 2):
        print('Ganaste🎈🎈🎈')
        break
    elif (computer > 2):
        print('Perdiste❌❌❌')
        break
    
    print(f'Marcador\nTu: {person} Computadora: {computer}')
