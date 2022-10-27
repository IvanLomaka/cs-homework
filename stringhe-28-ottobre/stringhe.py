check = True

while True:
    string = input("Bella inserisci una frase: ")
    newstring = ''
    for a in string:
        if (a.isalpha() and check):
            newstring += a.capitalize()
            check = not check
        else:
            newstring += a
    if not check:
        print(newstring)
        break