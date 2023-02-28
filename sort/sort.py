#inizializzazione delle due liste 
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "George", "Hannah", "Ivan", "Jack", "Karen", "Luke", "Mike", "Nina", "Oscar", "Paul", "Quincy", "Rachel", "Steve", "Tina"]

grades = [9, 5, 9, 7, 9, 8, 3, 5, 10, 8, 4, 6, 4, 9, 3, 4, 2, 6, 7, 8]

# creazione di una lista in cui in ogni spazio ci sono due variabili
# [('Alice', 9), ('Bob', 5), ('Charlie', 9), ('David', 7), ('Eve', 9), ('Frank', 8), ('George', 3), ('Hannah', 5), ('Ivan', 7), ('Jack', 8), ('Karen', 4), ('Luke', 6), ('Mike', 10), ('Nina', 9), ('Oscar', 3), ('Paul', 4), ('Quincy', 2), ('Rachel', 6), ('Steve', 7), ('Tina', 8)]
# quindi ad ogni nome è associato un voto e stanno nella stessa lista in modo tale da poterli ordinare meglio
# in questo caso specifico si crea quello che in inglese è chiamato tuple
# i tuple sono come le liste con alcune differenze
# una tra quelle è che sono immutabili e che a differenza delle liste che si segnano con [] i tuples sono rappresentati da ()
# per accedere ad una variabile in un touple si usano sempre le parentesi quadre il primo elemento del primo tuple si rappresenta così class_members[0][0] => Alice 
class_members = list(zip(names, grades))

# ordina in ordine alfabetico gli elementi della lista class_members in base al primo elemento di ogni tuple (quindi al nome)
class_members.sort(key=lambda x: x[0])

print("Nomi in ordine alfabetico:")
# loop per ogni elemento in class_members
for member in class_members:
    # member ha ogni volta un tuple diverso partendo dal primo elemento della lista fino al'lultimo
    # ti ricordo che ogni elemento di class_members è un tuple (simile a una lista) quindi ha più di una variabile es: ('Alice', 9)
    # prendiamo il primo elemento del tuple nella variabile name (quindi 'Alice' sara memorizzata in name) e il secondo elemento del tuple sarà memorizzato in grade (il voto di 'Alice' => 9)
    # name ha il nome della persona e grade il suo voto
    name, grade = member
    # qui si fa solo il print del nome e del voto
    print("Nome:", name, "\t", "Voto:", grade)

# ordina in ordine numerico gli elementi della lista class_members in base al secondo elemento di ogni tuple (quindi il voto)
# di base gli ordina dal più basso al più alto
# reverse = True è usato in modo tale da fare "l'inversione" totale della lista
# fare il reverse della lista serve in modo tale da ordinare i voti dal più alto al più basso
# vedi consegna su classroom 
class_members.sort(key=lambda x: x[1], reverse = True)

# Print the grades in ascending order with respective names
print("Voti in ordine decrescente:")
for member in class_members:
    name, grade = member
    print("Nome:", name, "\t" ,"Voto:", grade)