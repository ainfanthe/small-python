import random

NUM_DIGITS = 3 # Puede variar entre 1 o 10
MAX_GUESSES = 10

def main():
    print('''Bagels, deducción lógica. 
Se piensa en un {}-digito sin números repetidos.
Intenta adivinar cual es. Aquí algunas pistas:
Cuando se diga:       That means:
    Pico              Un digito es correcto pero en la posición erronea
    Fermi             Un digito es correcto y en posición correcta
    Bagels            Ningún digito es correcto
    
Por ejemplo, si el número secreto fuese 248 y la respuesta 843, la
pista será Fermi Pico.'''.format(NUM_DIGITS))
    
    while True: # Menú de juego loop
        # Esto almacena el número secreto
        secretNum = getSecretNum()
        print('He pensado un número')
        print('Tienes {} intentos para adivinarlo'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Mantiene el loop hasta el ingreso de input valido
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Adivina #{}: '.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            
            numGuesses += 1
            
            if guess == secretNum:
                break # Es correcto, ergo, salimos del loop
            if numGuesses > MAX_GUESSES:
                print('Se acabaron los intentos')
                print('La respuesta era {}'.format(secretNum))
                
            # Preguntar al jugador si quiere comenzar de nuevo
            print('¿Quieres comenzar de nuevo? (si o no)')
            if not input('> ').lower().startswith('s'):
                break
            print('¡Gracias por jugar!')
            
def getSecretNum():
    """Retorna un string hecho de NUM_DIGITS"""
    numbers = list('0123456789') # Crea una lista de 0 a 9
    random.shuffle(numbers)
    
    # Obtenemos el primer NUM_DIGITS in la lista para el n secreto:
    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Retorna un string con el Pico, Fermi o Bagels pistas, y el par de números secretos"""
    if guess == secretNum:
        return '¡Lo tienes!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Un digito correcto está en el lugar correcto
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Un digito correcto en lugar incorrecto
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # No hay digitos correctos
    else:
        # Organiza las pistas en orden alfabetico
        clues.sort()
        # Realiza un solo string
        return ''.join(clues)
    
if __name__ == '__main__':
    main()