import math
from math import *


def mod(z):
    return sqrt(z.real**2 + z.imag**2)



r1 = float(input("Enter the Resistance for Z1"))
l1 = float(input("Enter the Inductance for Z1"))
l1= l1 * 0.001
r2=float(input("Enter the Resistance for Z2"))
c2=float(input("Enter the Capacitance for Z2"))
c2= c2 * 1e-6
r3=float(input("Enter the Resistance for Z3"))
l3=float(input("Enter the Resistance for Z3"))
l3=l3*0.001
nu = float(input("Enter the Frequency"))
theta = float(input("Enter the Angle"))
theta = theta*180/pi
V=float(input("Enter the Voltage"))
V = V*(cos(theta) + 1j*sin(theta))
t = 400  # given in Q7 in minutes

w = 2*math.pi*nu
xl1 = w*l1*1j
xc2=1/(w*c2*1j)
xl3 = w*l3*1j

z1 = r1 + xl1
z2 = r2 + xc2
z3 = r3 + xl3
r = r1 + r2 + r3

print("q1 total impedence")
z = z1+z2+z3
print(z, "\n")

print("q2 total current")
i = V/z
print(i, "\n")

print("q3 volatge across z2")

V2 = i*z2
print(V2, "\n")

print("q4 V_ac")
vac = i*(z1+z2)
print(vac, "\n")

print("q5 power factor")
pf = r/mod(z)
print(pf, ("lead" if (xl1+xl3-xc2).imag<0 else "lag"), "\n")

print("q6 reactive power by z2")
phi = acos(pf)
P = mod(i**2*xc2)
print(P, "VAR", "\n")

print("q7 energy consumed by z1")
# t=t/60   # convert to hours
print("ignore")

print("q8 power factor becomes 1.0")
print("ignore\n")

print("q9 % powerloss in z3")
p3 = mod(i**2*z3.real)
print(mod(z3.real/z.real), "\n")

print("q10 V_ac and V_bd phase")
vac = i*(z1+z2)
vbd = i*(z2+z3)
print(degrees(acos(vac.real/mod(vac)))-degrees(acos(vbd.real/mod(vbd))))
