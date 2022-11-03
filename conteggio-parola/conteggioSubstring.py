string = input("Bella, inserisci una frase: ")
find = input("Bella, inserisci la parola da cercare: ") or 'perchè'
for n in range(len(string)):
    if(string[n:(n + len(find))] == find): 
        print(str(n) + string[n:(n + len(find))])