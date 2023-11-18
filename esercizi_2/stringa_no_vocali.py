#concatenare i caratteri di una stringa in una nuova stringa SENZA VOCALI

stringaUser=input("Inserisci una parola: ")

stringaNuova=""

for lettera in stringaUser:

    if lettera != "a" and lettera != "e" and lettera != "i" and lettera != "o" and lettera != "u":
        
        stringaNuova+=lettera
        
    
print(f"La parola senza vocali diventa: {stringaNuova}")