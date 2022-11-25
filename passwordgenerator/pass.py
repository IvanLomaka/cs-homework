import string
import random

password_l = 0
password = ''
password2= ''
contatore = 0

print('\nGENERATORE DI PASSWORD CASUALI\n ')

password_l = int(input('Lunghezza password: '))

for i in range(password_l):
    if (random.randint(1, 10) % 2 == 0): 
        password = password + random.choice(string.ascii_letters)
    else:
        if random.randint(1, 10) % 2 > 0 and random.randint(1, 10) % 2 < 3:
            password = password + random.choice(string.digits)
        elif random.randint(1, 10) % 2 > 3 and random.randint(1, 10) % 2 < 6:
            password = password + random.choice(string.ascii_upperletters) 
        else:
            password = password + "_"

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

def cracker(password):
    guess = ''
    tests = 1

    for i in range(len(password)):
        for j in range(len(chars)):
            tests = tests + 1
            print(guess + chars[j])
            if(chars[j] == password[i]): 
                guess = guess + chars[j]
                break
    
    print(f'The generated password is {guess} the algorithm got this result in {tests} tries')

cracker(password)

print('\nla tua password generata è: ' + password + '\n\n\n')