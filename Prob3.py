import numpy as np

def series(Z1,Z2):
    return Z1+Z2

def parallel(Z1,Z2):
    invZ=(1/Z1)+(1/Z2)
    return (1/invZ)
def modulus(Z):
    return np.sqrt(Z.real*Z.real+Z.imag*Z.imag)

def Argument(Z):
    return np.rad2deg(np.arctan(Z.imag/Z.real)) 
#Input Data
R1=float(input("Enter Resistance for Z1:"))
R2=float(input("Enter Resistance for Z2:"))
R3=float(input("Enter Resitance for Z3:"))
L1=float(input("Enter the Inductance for Z1:"))
C2=float(input("Enter the Capacitance for Z2:"))
L3=float(input("Enter the Inductance for Z3:"))
V=float(input("Enter the Voltage:"))
Frequency=float(input("Enter the Frequency:"))
Angle=float(input("Enter the Angle:"))
#Data Manipulation
Omega=2*(np.pi)*Frequency
XC=(1/(Omega*C2)) * 1e6
XL1=(Omega*L1) * 0.001
XL3=(Omega*L3) * 0.001
Angle=Angle*np.pi/180
#Have ur Data Finally in Complex Form
Z1=R1+1j*XL1
Z2=R2-1j*XC
Z3=R3+1j*XL3
V=V*(np.cos(Angle)+1j*np.sin(Angle)) #Its RMS

#Total Impedence
Z=parallel(Z1,series(Z2,Z3))

#Problem 11 (Total Current)
I=(V/Z) 
print("Problem 11: Total Current of Circuit is ",I)

#Problem 12 (Current in I1 when Z3 is short circuit)
I1=V/Z1
print("Problem 12: Current in I1 is ",I1)

#Problem 13
P=modulus((I**2)*Z.real)
print("Problem 13: Active Power of circuit is ",P)

#Problem 14
PowerFactor=Z.real/modulus(Z)
print("Problem 14: Power Factor of circuit is ",PowerFactor)

#Problem 15
I1=V/Z1
I2=V/series(Z2,Z3)
AngleI1=Argument(I1)
AngleI2=Argument(I2)
PhaseDiff=modulus(AngleI1-AngleI2)
print("Problem 15: Phase Diff of circuit is ",PhaseDiff)

#Problem 16
I1=V/Z1
I2=V/Z3
AngleI1=Argument(I1)
AngleI2=Argument(I2)
PhaseDiff=modulus(AngleI1-AngleI2)
print("Problem 16: Phase Diff of circuit(Z2 is short circuit) is ",PhaseDiff)

#Problem 17
print("Problem 17: Question is Incorrect, Mark Anything")

#Problem 18
I2=V/series(Z2,Z3)
PowerLoss = modulus((I2**2)*Z3.real)
print("Problem 18: Power Loss in Z3 is ",PowerLoss)

#Problem 19
print("Problem 19: Problem is Incorrect, Mark Anything")

#Problem 20
Vab=V
Vde=I2*Z3
AngleVab=Argument(Vab)
AngleVde=Argument(Vde)
PhaseDiff=modulus(AngleVab-AngleVde)
print("Problem 20: Phase Diff between Vab and Vde is ",PhaseDiff)
