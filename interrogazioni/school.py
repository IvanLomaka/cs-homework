import random

alunni = []

with open("elencoalunni.txt" , "r") as f:
    alunni = f.read().split('\n')

print(alunni)

numeroassenti = int(input('Inserisci il numero degli studenti assenti: '))
a = 0
while a < numeroassenti:
    nomeassente = input('Inserisci il nome dell\'assente: ')
    if nomeassente in alunni:
        a = a + 1
        alunni.remove(nomeassente)
    else:
        print('nome inserito non valido')


interrogati = int(input('Inserisci il numero degli studenti interrogati: '))
interr = 0

while interr < interrogati:
    alunnoInterrogato = random.choice(alunni)

    if alunnoInterrogato in alunni:
        print('Studente/Studentessa interrogato/a:', alunnoInterrogato)
        alunni.remove(alunnoInterrogato)
        interr = interr + 1