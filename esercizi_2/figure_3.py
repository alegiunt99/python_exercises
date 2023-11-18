#3

stringaes3_1="1"
stringaes3_2="654321"

i=1

print(stringaes3_1, stringaes3_2)


while i < 6:
    
    stringaes3_1+=str(i+1)
    stringaes3_2=stringaes3_2[1:]
    
    print(stringaes3_1, stringaes3_2)
    
    i+=1
   