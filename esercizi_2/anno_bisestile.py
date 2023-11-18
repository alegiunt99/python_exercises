#verifica che un anno sia bisestile

annoUser=int(input("inserisci un anno: "))

if annoUser % 4 == 0:

    print("l'anno è bisestile")
            
else:
    print("l'anno non è bisestile")