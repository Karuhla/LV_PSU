print("Unesite broj izmedu 0.0 i 1.0:")

while(True):

    x = input()
    
    try:
        broj = float(x)
        break
    except:
        print("Niste unijeli broj")

if(broj < 0.6 and broj >= 0.0):
    print("F")
elif(broj < 0.7 and broj >= 0.6):
    print("D")
elif(broj < 0.8 and broj >= 0.7):
    print("C")
elif(broj < 0.9 and broj >= 0.8):
    print("B")
elif(broj < 1.0 and broj >= 0.9):
    print("A")
else:
    ("Niste unijeli broj unutar granica")