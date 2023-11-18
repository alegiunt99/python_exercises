#Verifica il valore massimo tra 3 numeri

numeroUser1=int(input("inserisci un numero: "))
numeroUser2=int(input("inserisci un numero: "))
numeroUser3=int(input("inserisci un numero: "))

#creo una condizione che metta a confronto i 3 numeri inseriti

if (numeroUser1 > numeroUser2 and numeroUser1 > numeroUser3):  #se il primo è maggiore del secondo e del terzo

    print(f"il numero massimo è: {numeroUser1}") 
    
elif (numeroUser2 > numeroUser1 and numeroUser2 > numeroUser3) : #se il secondo è maggiore del primo e del terzo

    print(f"il numero massimo è: {numeroUser2}")
    
elif (numeroUser3 > numeroUser1 and numeroUser3 > numeroUser2) : #se il terzo è maggiore del secondo e del primo

    print(f"il numero massimo è: {numeroUser3}")
    
elif (numeroUser1 > numeroUser2 and numeroUser1 == numeroUser3) : #se il primo è maggiore del secondo e uguale al terzo
    print(f"i numeri massimi sono: {numeroUser1} e {numeroUser3}")
    
elif (numeroUser1 > numeroUser3 and numeroUser1 == numeroUser2) : #se il primo è maggiore del terzo e uguale al secondo
    print(f"i numeri massimi sono: {numeroUser1} e {numeroUser2}") 
    
elif (numeroUser2 > numeroUser1 and numeroUser2 == numeroUser3) : #se il secondo è maggiore del primo e uguale al terzo
    print(f"i numeri massimi sono: {numeroUser2} e {numeroUser3}")
    
else:                                                             #infine, condizione in cui tutti i numeri inseriti siano uguali
    print(f"i numeri sono tutti uguali")

