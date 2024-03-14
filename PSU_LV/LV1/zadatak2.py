try:
    broj = float(input("Unesite ocjenu izmedu 0.0 i 1.0: "))
    
    if broj < 0.0 or broj > 1.0:
        print ("Niste unijeli broj unutar granica 0.0 i 1.0.")
    elif(broj < 0.6 and broj >= 0.0):
        print("F")
    elif(broj < 0.7 and broj >= 0.6):
        print("D")
    elif(broj < 0.8 and broj >= 0.7):
        print("C")
    elif(broj < 0.9 and broj >= 0.8):
        print("B")
    elif(broj < 1.0 and broj >= 0.9):
        print("A")
except:
    print("Niste unijeli broj.")