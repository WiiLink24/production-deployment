import pyminizip as q
import pickle as a
import sys as r
import pathlib as o
import os as p
import random as b
s = print
q = b.getrandbits
c = str
d = int
n = d(9)
u = ".dat"
g = "/" + "password" + u
h = 'password' + u
i = 'key.dat'
j = 'wb'
t = "/"
path = c(o.Path(__file__).parent.absolute())
k = path + t + "password.dat" + u
l = c(path + g)
m = c(path + t + "password.enc")
s("The more bits, the more secure it is!\n")
s("Availale bit sizes:\n")
s("1, 2, 4,\n")
s("8, 16, 32,\n")
s("64, 128, 256, \n")
s("512, 1024, 2048,\n")
s("4096, 8192, 9999\n")
w = d(input("Enter the bitsize you want:"))
x = q(w)
y = c(q(w))
e = open(h, j)
a.dump(x, e)
e.close()
f = open(i, j)
a.dump(y, f)
f.close()
q.compress(l, path, m, y, n)
p.remove(k)
r.exit(0)
