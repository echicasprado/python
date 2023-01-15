import random

options = {'piedra':1,'papel':2,'tijera':3}

def printScore(person,computer):
    print('*'*20)
    print(f'Marcador\nTu: {person} Computadora: {computer}')

def printWinner(score_person,score_computer):
    breakGame = False
    
    print('*'*20)
    
    if(score_person > 2):
        print('Ganaste🎈🎈🎈')
        breakGame = True
        
    elif (score_computer > 2):
        print('Perdiste❌❌❌')
        breakGame = True
        
    print(f'Marcador\nTu: {score_person} Computadora: {score_computer}')
    
    return breakGame
    
def printRound(round):
    print('*'*20)
    print(f'ROUND {round}')
    print('*'*20)
    
def chooseOptions():
    inputPerson = input('Seleciona una opción: piedra, papel, tijera\n')
    inputComputer = random.choice(list(options.keys()))

    print('Tu elegiste: {0}'.format(inputPerson))
    print('Computadora elegio: {0}'.format(inputComputer))

    personSelect = options.get(inputPerson.lower())
    computerSelect = options.get(inputComputer.lower())
    return personSelect, computerSelect

def winner(personSelect, computerSelect,person,computer):
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
    
    return person, computer
   
def run_game():
    person = 0
    computer = 0
    round = 1
            
    while True:
        printRound(round)
        personSelect, computerSelect = chooseOptions()
        person, computer = winner(personSelect,computerSelect,person,computer)
    
        if(printWinner(person,computer)):
            break
    
        printScore(person,computer)
        round +=1

run_game()