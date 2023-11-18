#scrivi un programma che utilizzi il ciclo While per calcolare la somma dei primi N numeri pari, dove N è un numero inserito dall'utente

numUser=int(input("Inserisci un numero: "))

#creo una variabile di appoggio chiamata somma
somma=0

i = 1

#finchè il valore i è minore o uguale al numero inserito dall'user
while i <= numUser:

    if i % 2 == 0:    #se il numero è pari, 
        
        #la variabile somma prende il valore di i e ogni giro si somma al successivo numero pari che trova
        somma+=i
    
    i+=1


#alla fine, la variabile somma avra il valore di ogni numero pari presente nell'intervallo che va da 0 al numero inserito dall'utente.

print(f"La somma dei numeri pari contenuti nel numero iniziale è: {somma}")