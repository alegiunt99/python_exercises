#stampa il numero di vocali presenti nella stringa inserita dall'utente

stringaUser=input("Inserisci una parola: ")

vocali=0

for lettera in stringaUser:

    if lettera == "a":
        vocali+=1
    elif lettera == "e":
        vocali+=1
    elif lettera == "i":
        vocali+=1
    elif lettera == "o":
        vocali+=1
    elif lettera == "u":
        vocali+=1

if vocali > 0:
    print(f"La parola contiene {vocali} vocali")
else:
    print(f"La parola non contiene vocali")
    