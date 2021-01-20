#kinematic for 3body photodisintegration
import numpy
import matplotlib.pyplot as plt
from scipy import constants
M_e = constants.value('electron mass energy equivalent in MeV')
M_p = constants.value('proton mass energy equivalent in MeV')
M_n = constants.value('neutron mass energy equivalent in MeV')
M_d = constants.value('deuteron mass energy equivalent in MeV')
M_he = 3.0160293191*931.494 - 0.511*2 #atomic  mass - electrons mass
Ei = 18-7.7;
i = 0
j = 0
k = 0
N = 100000
M = 180
while i<=N:
    #Ei = numpy.random.uniform(0.0, 3000)
    cos_theta_p = numpy.random.uniform(-1,1)
    phi_p = numpy.random.uniform(-180.0, 180.0)* numpy.pi / 180
    #P_p = numpy.random.uniform(0.0, 10.0)#MeV
    #P_p = numpy.random.uniform(0.0, 400.0)#MeV
    E_p = numpy.random.uniform(M_p, Ei+M_he)#MeV
    cos_theta_n = numpy.random.uniform(-1,1)
    phi_n = numpy.random.uniform(-180.0, 180.0)* numpy.pi / 180
    theta_p = 180 * numpy.pi / 180
    #theta_p = numpy.arccos(cos_theta_p)
    theta_n = numpy.arccos(cos_theta_n)
    #theta_p = numpy.random.uniform(0.0, 180.0)* numpy.pi / 180
    #theta_n = numpy.random.uniform(0.0, 180.0)* numpy.pi / 180
    #E_p = numpy.sqrt(P_p**2+M_p**2)
    P_p = numpy.sqrt(E_p**2-M_p**2)
    sint1 = numpy.sin(theta_p)
    cost1 = numpy.cos(theta_p)
    sint = numpy.sin(theta_n)
    cost = numpy.cos(theta_n)
    cos_m = numpy.cos(phi_p-phi_n)
    A = -2*(Ei+M_he-E_p)
    B = M_he**2+2*(Ei*M_he-Ei*E_p-E_p*M_he)
    C = 2*P_p*(sint1*sint*cos_m+cost1*cost)-2*Ei*cost
    D = -M_n**2-2*P_p*cost1
    EE = A**2-C**2
    F = 2*A*(B-D)
    G = (B-D)**2+C**2*M_n**2
    #A = Ei+M_he-E_p
    #B = A
    #C = 2*P_p*(sint1*sint*cos_m+cost1*cost)-2*Ei*cost
    #D = -M_n**2-2*P_p*cost1*Ei+E_p**2+Ei**2
    #EE = 4*B**2-C**2
    #F = -4*B*(A**2-D)
    #G = (A**2-D)**2+C**2*M_n**2
    if F**2-4*EE*G > 0:
        SR = numpy.sqrt(F**2-4*EE*G)
        En = ((-F + SR)/(2*EE))
        if En > 0:
            print(P_p)
            #print(En-M_n)
            K_n = (En-M_n)
            #K_n = (En-M_n)*(1+numpy.random.normal(0,0.03))
            plt.plot(theta_n*180/numpy.pi,K_n,'o',color ='grey' ,markersize=2)
            j += 1
    theta = numpy.random.uniform(0.0, 180.0)* numpy.pi / 180
    cos = numpy.cos(theta)
    E_elastic = Ei/(1.0+Ei*(1.0-cos)/M_he)
    #E_elastic = Ei/(1.0+Ei*(1.0-cos)/M_he)*(1+numpy.random.normal(0,0.03))
    #plt.plot(theta*180/numpy.pi,E_elastic,'bo',markersize=2)
    i += 1
#while k<=M:
#    theta = k*numpy.pi/180;
#    cos = numpy.cos(theta)
#    E_elastic = Ei/(1.0+Ei*(1.0-cos)/M_he)
#    print(E_elastic)
#    plt.plot(k,E_elastic,'bo',markersize=2)
#    k += 1
print(j)
#plt.savefig("Ei.png",dpi = 100)
plt.savefig("En.png",dpi = 100)
