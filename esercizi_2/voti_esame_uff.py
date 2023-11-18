#creo 2 variabili di appoggio
votoTeoria=0
votoPratica=0


while True:
    print("\n_______________________\n")
    votoTeoria=int(input("\nInserisci il voto di teoria compreso tra -8 e 8: "))
    votoPratica=int(input("Inserisci il voto di pratica compreso tra 0 e 24: "))

    
    if votoTeoria < -8 or votoTeoria > 8:
    
        print("\nERRORE: Devi inserire un voto di Teoria compreso tra -8 e 8!")
        
       
        
        if votoPratica < 0 or votoPratica > 24:                    
            
            print("ERRORE: Devi inserire un voto di Pratica compreso tra 0 e 24!")
       
    elif votoPratica < 0 or votoPratica > 24:
    
        print("\nERRORE: Devi inserire un voto di Pratica compreso tra 0 e 24!")
    
    else: 
        break 

#creo una variabile che somma i 2 voti
sommaVoti = votoTeoria + votoPratica

messaggio=""

if votoTeoria <= 0:
        #bocciato
    messaggio="bocciato"

elif votoTeoria > 0 and sommaVoti < 18:   #se il voto di teoria è superiore a 0 e la somma dei 2 voti è minore di 18
        
    #bocciato
    messaggio="bocciato"

elif sommaVoti > 30:   #se il voto di teoria è superiore a 0 e la somma dei 2 voti è minore di 18
        
    #bocciato
    messaggio="Promosso, 30 e lode"
        
else:
        
    messaggio="Promosso, voto finale: " + str(sommaVoti)
        

print(messaggio)

