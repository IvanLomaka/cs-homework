import random

# il programma è diviso in blocchi:

# blocco zero: inizializzazione e ordine dell'array
# primo blocco: si chiede il numero degli interrogati all'utente
# secondo blocco: si chiede all'utente le persone assenti quel giorno
# terzo blocco: generazione della nuova lista con gli studenti non chiamati all'interrogazione e assenti

# blocco zero
alunni = [
    "VANIN EMMA + vanin.emma@studenti.liceoduca.it",
    "TADDEI GINEVRA + taddei.ginevra@studenti.liceoduca.it",
    "SANSONETTO ANDREA + sansonetto.andrea@studenti.liceoduca.it",
    "PIOVESAN MATTIA + piovesan.mattia@studenti.liceoduca.it",
    "PIOVESAN ANNA + piovesan.anna19@studenti.liceoduca.it",
    "PETRIN CARLO ALBERTO + petrin.carloalberto@studenti.liceoduca.it",
    "MESTRINER ANDREA + mestriner.andrea@studenti.liceoduca.it",
    "MARTINELLI BENEDETTA + martinelli.benedetta@studenti.liceoduca.it",
    "LOMAKA IVAN + lomaka.ivan@studenti.liceoduca.it",
    "GRIGOLETTO DAVIDE + grigoletto.davide@studenti.liceoduca.it",
    "GRANZOTTO LEONARDO + granzotto.leonardo@studenti.liceoduca.it",
    "FRASSETTO FRANCESCA AURORA + frassetto.francescaaurora@studenti.liceoduca.it",
    "FIOROTTO TOMMASO + fiorotto.tommaso@studenti.liceoduca.it",
    "DIOTALLEVI NICOLO' + diotallevi.nicolo@studenti.liceoduca.it",
    "DE POLI NICOLA + depoli.nicola@studenti.liceoduca.it",
    "DE LAZZARI ALESSANDRO + delazzari.alessandro@studenti.liceoduca.it",
    "CONTE FILIPPO + conte.filippo@studenti.liceoduca.it",
    "BUTTARI IRENE + buttari.irene@studenti.liceoduca.it",
    "BRUNELLO SIMONE + brunello.simone@studenti.liceoduca.it",
    "BOZZO AURORA + bozzo.aurora@studenti.liceoduca.it",
    "BETTETI RICCARDO + betteti.riccardo@studenti.liceoduca.it",
    "BERALDO GRETA + beraldo.greta@studenti.liceoduca.it",
    "BARDI LEONARDO + bardi.leonardo@studenti.liceoduca.it",
    "BANDIERA SARA + bandiera.sara@studenti.liceoduca.it",
    "BALDASSO ALBERTO + baldasso.alberto@studenti.liceoduca.it",
]
# mette in ordine alfabetico la lista alunni
alunni.sort()

# primo blocco
numeroAssenti = int(input("Inserisci il numero di assenti: "))
conteggioNumeroAssenti = 0
alunniAssenti = []

while conteggioNumeroAssenti < numeroAssenti:
    assente = input("Inserire COGNOME NOME dell'assente: ")
    
    for alunno in alunni:
        if alunno.count(assente) > 0 and assente.count(' ') > 0:
            alunni.remove(alunno)
            alunniAssenti.append(alunno)
            conteggioNumeroAssenti = conteggioNumeroAssenti + 1

# secondo blocco
numeroInterrogati = int(input("Inserisci il numero di interrogati: "))

for x in range(numeroInterrogati):
    interrogato = random.choice(alunni)
    alunni.remove(interrogato)
    print(f'L\'alunno interrogato è {interrogato}')

# terzo blocco:
alunni.extend(alunniAssenti)
alunni.sort()

print(alunni)