count = 0
string = input("Bella, inserisci una frase: ")
stringaDivisa = string.split()
   
for i in stringaDivisa:
    if i == 'perchè':
        print(i + str(count))
    count += len(i)
    while True:
        try:
            if string[count] == ' ': count += 1
            else: break
        except IndexError: break