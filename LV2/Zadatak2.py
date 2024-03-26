import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("C:/Users/student/Desktop/LV2/mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

wt = data[:, 5]
mpg = data[:, 0]
hp = data[:, 3]

plt.scatter(mpg, hp, s= 10*wt)
plt.xlabel('hp')
plt.ylabel('mpg')
plt.title('Graf ovisnosti hp o mpg')
plt.show()

print("Minimalna vrijednost potrosnje automobila je: ", np.min(mpg))
print("Maksimalna vrijednost potrosnje automobila je: ", np.max(mpg))
print("Srednja vrijednsot potrosnje automobila je: ", np.mean(mpg))

cyl6 = np.where(data[:,1] == 6)
mpg_cyl6 = mpg[cyl6]

print("\nMinimalna vrijednost potrosnje automobila sa 6 cilindara je: ", np.min(mpg_cyl6))
print("Maksimalna vrijednost potrosnje automobila sa 6 cilindara je: ", np.max(mpg_cyl6))
print("Srednja vrijednsot potrosnje automobila sa 6 cilindara je: ", np.mean(mpg_cyl6))