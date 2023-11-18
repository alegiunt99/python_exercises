#dati 3 lati di un triangolo determinare se il triangolo è scaleno, isoscele o equilatero

lato1=int(input("Inserisci la lunghezza di un lato: "))
lato2=int(input("Inserisci la lunghezza di un lato: ")) 
lato3=int(input("Inserisci la lunghezza di un lato: "))

if lato1 == lato2 and lato1 == lato3:

    print("Il triangolo è EQUILATERO")
    
elif lato1 == lato2 or lato1 == lato3 or lato2 == lato3:

    print("Il triangolo è ISOSCELE")
    
else:
    
    print("Il triangolo è SCALENO")
    
    
 