string = input("Bella, inserisci una frase: ")
find = input("Bella, inserisci la parola da cercare: ") or 'perchè'
for n in range(len(string)):
    if(string[n:(n + len(find))] == find): 
        print(str(n) + string[n:(n + len(find))])

#string = input("Bella, inserisci una frase: ")
#for n in range(len(string)): print((str(n) + '\n') if string[n:(n + len('perchè'))] == 'perchè' else "", end='')