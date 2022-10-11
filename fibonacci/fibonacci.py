def fibonacci(number):
    if(number == 0):
        return 0
    if(number == 1 or number == 2):
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)

while True:
    try:
        num = int(input("Bella inserisci un numero: "))
        if num > 0:
            break
        print("numero non valido")
    except ValueError:
        print("L'input non è un numero")

# for n in range(num): lo fa partire da 0
#     print("Il numero " + str(n) + " della serie è: " + str(fibonacci(n)))

for n in range(num): 
    print("Il numero " + str(n + 1) + " della serie è: " + str(fibonacci(n + 1)))