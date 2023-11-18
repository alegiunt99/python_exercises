#conta la lunghezza di una stringa con il for

stringaUser=input("Inserisci una parola: ")

lunghezzaStringa=0

for lettera in stringaUser:
   
   lunghezzaStringa+=1



print(f"La parola è lunga {lunghezzaStringa} caratteri")