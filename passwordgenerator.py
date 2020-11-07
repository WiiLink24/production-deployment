import pyminizip
import pickle
import sys
import pathlib
import os
ext = sys.exit
path = pathlib.Path(__file__).parent.absolute()
print("The more bits, the more secure it is!")
print("Availale bit sizes: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 9999")
w = input("Enter the bitsize you want:")
x = d.getrandbits(w)
y = d.getrandbits(w)
savefile = open('password.dat', 'wb')
pickle.dump(x, savefile)
savefile.close()
savefile2 = open('key.dat', 'wb')
pickle.dump(y, savefile2)
savefile2.close()
pyminizip.compress("password.dat", path, "password.enc", y, int(compress_level))
os.remove(password.dat)
ext(0)
