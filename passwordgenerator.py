import pyminizip as v
import pickle as a
import sys as r
import pathlib as o
import os as p
import random as b
c = str
d = int
u = ".dat"
g = "/" + "password" + u
h = 'password' + u
s = print
q = b.getrandbits
n = d(9)
i = 'key.dat'
j = 'wb'
t = "/"
w = c(o.Path(__file__).parent.absolute())
k = w + t + "password" + u
l = c(w + g)
m = c(w + t + "password.enc")
s("The more bits, the more secure it is!\n")
s("Availale bit sizes:\n")
s("1, 2, 4,\n")
s("8, 16, 32,\n")
s("64, 128, 256, \n")
s("512, 1024, 2048,\n")
s("4096, 8192, 9999,\n")
z = d(input("Enter the bitsize you want:\n"))
x = q(z)
y = c(q(z))
e = open(h, j)
a.dump(x, e)
e.close()
f = open(i, j)
a.dump(y, f)
f.close()
v.compress(l, w, m, y, n)
p.remove(k)
r.exit(0)
