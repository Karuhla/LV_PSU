brojevi = []
brojac = 0
zbroj = 0

while(True):

    varijabla =  input()

    if(varijabla == "Done"):
        break
    elif(varijabla.isdigit() != True):
        print("Niste unijeli broj")
    else:
        brojevi.append(int(varijabla))

brojevi.sort
print(brojevi)
