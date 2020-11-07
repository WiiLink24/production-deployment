import pyminizip
import pickle
import sys
import pathlib
import os
import random
extmain = sys.exit
extsecn = "/" + "password.dat"
data4 = 'password.dat'
data5 = 'key.dat'
data9 = 'wb'
path = str(pathlib.Path(__file__).parent.absolute())
data8 = path + "/" + "password.dat"
data6 = path + extsecn
data7 = path + "/" + "password.enc"
print("The more bits, the more secure it is!")
print("Availale bit sizes: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 9999")
w = input("Enter the bitsize you want:")
x = random.getrandbits(int(w))
y = random.getrandbits(int(w))
savefile = open(data4, data9)
pickle.dump(x, savefile)
savefile.close()
savefile2 = open(data5, data9)
pickle.dump(y, savefile2)
savefile2.close()
data3 = 9
pyminizip.compress(str(data6), str(path), str(data7), str(y), int(data3))
os.remove(data8)
extmain(0)
