from math import *

def ser(z1, z2): return z1+z2

def par(z1, z2): return 1/(1/z1+1/z2)

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

# r1=18
# l1=0.18
# r2=28
# c2=100e-6
# r3 = 5
# l3=0.27

# theta=50/180*pi
# V = 125*(cos(theta) + 1j*sin(theta))
# nu = 40

w = 2*pi*nu
xl1 = w*l1*1j
xc2=1/(w*c2*1j)
xl3 = w*l3*1j

z1 = r1 + xl1
z2 = r2 + xc2
z3 = r3 + xl3

print("q11 total impedence")
z = ser(z1, par(z2, z3))
print(z, "\n")

print("q12 total current")
i = V/z
print(i, "\n")

print("q13 voltage across z2")
v2 = v3 = i*par(z2, z3)
print(v2, "\n")

print("q14 power factor")
pf = z.real/mod(z)
print(pf, "\n")

print("q15 power factor 1.0")
print("ignored\n")

print("q16 phase angle")
i2 = v2 / z2
print(degrees(acos(i2.real/mod(i2)))-degrees(acos(v3.real/mod(v3))), "\n")

print("q17 % power loss in z2")
print(mod(z2.real*i2**2/(z.real*i**2)), "\n")

print("q18 reactive power in z2")
print(mod(i2**2*z2.imag), "\n")

print("q19 energy consumed by z1")
print("ignored\n")

print("q20 phase between V_ab and V_ac")
vab = i*z1
vac = vab+v2
print(degrees(acos(vab.real/mod(vab)))-degrees(acos(vac.real/mod(vac))))
