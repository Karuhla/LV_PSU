def total_euro(a,b):
    c = a * b
    return c


print("Unesite broj radnih sati:")
brSati = int(input())
print("Unesite koliko ste placeni po satu:")
placa = float(input())

zarada = total_euro(brSati, placa)
print("Ukupna zarada je: ", zarada)