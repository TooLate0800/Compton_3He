#kinematic for 3body photodisintegration
import numpy
import matplotlib.pyplot as plt
from scipy import constants
M_e = constants.value('electron mass energy equivalent in MeV')
M_p = constants.value('proton mass energy equivalent in MeV')
M_n = constants.value('neutron mass energy equivalent in MeV')
M_d = constants.value('deuteron mass energy equivalent in MeV')
M_he = 3.0160293191*931.494 - 0.511*2 #atomic  mass - electrons mass
Ei = 100;
Es = - (M_he - 2*M_p -M_n)
print(Es)
i = 0
j = 0
k = 0
N = 100000
M = 180
A = 2*M_p+M_n
#B = 2*M_n*Ei#180deg
B = -2*M_n*Ei#0deg
C = M_n*Ei**2-4*M_n*M_p*(Ei-Es)
SR = numpy.sqrt(B**2-4*A*C)
Pn = (-B+SR)/(2*A)
Tn = numpy.sqrt(Pn**2+M_n**2)-M_n
print(Tn)
