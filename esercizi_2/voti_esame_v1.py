#calcola se l'alunno è promosso o bocciato

#creo le variabili dei voti di Teoria e Pratica
votoTeoria=int(input("\nInserisci il voto di teoria compreso tra -8 e 8: "))
votoPratica=int(input("Inserisci il voto di pratica compreso tra 0 e 24: "))

#creo una variabile che somma i 2 voti
sommaVoti = votoTeoria + votoPratica

#creo un pulsante, che inizializzo a True
promosso=True


#creo una prima condizione di controllo, che garantisca il corretto inserimento dei voti da parte dell'utente
if votoTeoria < -8 or votoTeoria > 8:
    
    print("\nDevi inserire un voto di Teoria compreso tra -8 e 8!")
    
elif votoPratica < 0 or votoPratica > 24:
    
    print("\nDevi inserire un voto di Pratica compreso tra 0 e 24!")
    
else:           #da qui in poi, la condizione in cui l'utente abbia inserito i voti correttamente
    
    if votoTeoria <= 0 and sommaVoti > 18:    #se il voto di teoria è inferiore a 0 e la somma dei 2 voti è maggiore di 18
        
        #bocciato
        promosso=False                        
    
    elif votoTeoria <= 0 and sommaVoti < 18:  #se il voto di teoria è inferiore a 0 e la somma dei 2 voti è minore di 18
        
        #bocciato
        promosso=False
    
    elif votoTeoria > 0 and sommaVoti < 18:   #se il voto di teoria è superiore a 0 e la somma dei 2 voti è minore di 18
        
        #bocciato
        promosso=False
    
    else:
        
        promosso=True
        
        
    #infine, utilizzando appunto il pulsante True-False, stabilisco le stampe da mostrare
    
    if promosso and sommaVoti > 30:
    
        print("\nCongratulazioni: 30 e lode!")
        
    elif promosso and sommaVoti <= 30:
    
        print(f"\nPromosso! Voto finale: {sommaVoti}")
        
    else:
    
        print(f"\nBocciato. Torna al prossimo appello")