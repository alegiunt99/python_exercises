#Verifica se un numero positivo, negativo o 0

numeroUser=int(input("inserisci un numero: "))

if numeroUser > 0:
    print("il numero è positivo")
elif numeroUser < 0:
    print("il numero è negativo")
else:
    print("il numero è 0")