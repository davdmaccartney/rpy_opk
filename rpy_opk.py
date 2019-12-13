import numpy as np


def getSignOf(chifre):
    if chifre >= 0:
        return 1
    else:
        return -1

def hrp2opk(Roll, Pitch, heading):
    Roll = np.deg2rad(Roll)
    Pitch   = np.deg2rad(Pitch)
    heading = np.deg2rad(heading)

    A_SINH = np.sin(heading)
    A_SINR = np.sin(Roll)
    A_SINP = np.sin(Pitch)

    A_COSH = np.cos(heading)
    A_COSR = np.cos(Roll)
    A_COSP = np.cos(Pitch)

    MX = np.zeros((3, 3))
    MX[0][0] =  (A_COSH *A_COSR) + (A_SINH*A_SINP*A_SINR)
    MX[0][1] =  (-A_SINH*A_COSR)+(A_COSH*A_SINP*A_SINR)
    MX[0][2] =   -A_COSP*A_SINR

    MX[1][0] = A_SINH*A_COSP
    MX[1][1] = A_COSH*A_COSP
    MX[1][2] = A_SINP


    MX[2][0] = (A_COSH*A_SINR)-(A_SINH*A_SINP*A_COSR)
    MX[2][1] = (-A_SINH*A_SINR)-(A_COSH*A_SINP*A_COSR)
    MX[2][2] =  A_COSP*A_COSR

    P = np.zeros((3, 3))
    P[0][0] = MX[0][0]
    P[0][1] = MX[1][0]
    P[0][2] = MX[2][0]
    
    P[1][0] = MX[0][1]
    P[1][1] = MX[1][1]
    P[1][2] = MX[2][1]
    
    P[2][0] = MX[2][0]
    P[2][1] = MX[1][2]
    P[2][2] = MX[2][2]

    Omega = 0
    Phi   = 0
    Kappa = 0

    Omega = np.arctan(-P[2][1]/P[2][2])
    Phi = np.arcsin(P[2][2])
    Kappa = np.arctan(-P[1][0]/P[0][0])

    Phi   = abs(np.arcsin(P[2][0]))
    Phi = Phi * getSignOf(P[2][0])
    Omega = abs(np.arccos((P[2][2] / np.cos(Phi))))
    Omega = Omega * (getSignOf(P[2][1] / P[2][2]*-1))
    Kappa = np.arccos(P[0][0] / np.cos(Phi))

    if getSignOf(P[0][0]) == getSignOf((P[1][0] / P[0][0])):
        Kappa = Kappa * -1

    Omega = np.rad2deg(Omega)
    Phi   = np.rad2deg(Phi)
    Kappa = np.rad2deg(Kappa)

    return(Omega,Phi,Kappa)

roll = -13.937
pitch = -8.01
yaw = 357.437
omega, phi, kappa = hrp2opk(roll, pitch, yaw)


print ('omega = ', omega)
print ('phi = ', phi)
print ('kappa = ', kappa)
