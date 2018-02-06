#Jackson Heise
#Ge109 Vector Analysis Tools
#Version 1.1

import math
"""
~~~~~~~~~~~TRIGONOMETRY TOOLS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def dsin(deg):              #degree-based sin function
    rad = deg * math.pi / 180.0
    return math.sin(rad)

def dcos(deg):              #degree-based cos function
    rad = deg * math.pi / 180.0
    return math.cos(rad)

def dtan(deg):              #degree-based tan function
    rad = deg * math.pi / 180.0
    return math.tan(rad)

def dacos(n):               #degree-based acos function
    rad = math.acos(n)
    return rad * 180 / math.pi

def dasin(n):               #degree-based asin function
    rad = math.asin(n)
    return rad * 180 / math.pi

def datan(n):               #degree-based atan function
    rad = math.atan(n)
    return rad * 180 / math.pi

"""
~~~~~~~~~~~2D VECTOR ANALYSIS TOOLS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def magdir_2d(Rx, Ry):      #convert vector notation to scalar notation
    mag = math.sqrt(Rx ** 2 + Ry ** 2)
    direc = math.atan(Ry / Rx) * 180 / math.pi
    return [mag, direc]

def components_2d(mag, direc): #convert scalar notation to vector notation
    Rx = mag * dcos(direc)
    Ry = mag * dsin(direc)
    return [Rx, Ry]

def law_of_cosines(a, b, theta): #Apply the Law of Cosines 
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * dcos(theta))
    return c

def LOS_a():         #Apply the Law of Sines [IN DEVELOPMENT]
    return 0

def LOS_theta():
    return 0

"""
~~~~~~~~~~~3D VECTOR ANALYSIS TOOLS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def CDAtoCVN(f, alpha, beta, gamma):        #Coordinate Direction to CVN
    fx = f * dcos(alpha)
    fy = f * dcos(beta)
    fz = f * dcos(gamma)
    return [fx, fy, fz]

def CVNtoCDA(fx, fy, fz):                   #CVN to Coordinate Direction Angles
    f = math.sqrt(fx ** 2 + fy ** 2 + fz ** 2)
    alpha = math.acos(float(fx) / float(f)) * 180 / math.pi
    beta = math.acos(float(fy) / float(f)) * 180 / math.pi
    gamma = math.acos(float(fz) / float(f)) * 180 / math.pi
    return [f, alpha, beta, gamma]

def PVAtoCVN(f, phi, theta):                #Position Angles to CVN
    fx = f * dsin(phi) * dcos(theta)
    fy = f * dsin(phi) * dsin(theta)
    fz = f * dcos(phi)
    return [fx, fy, fz]

def CVNtoPVA(fx, fy, fz):                   #CVN to Position Angles [IN DEVELOPMENT]
    return 0

def normalize(fx, fy, fz):                  #make a unit vector from given CVN
    f = math.sqrt(fx ** 2 + fy ** 2 + fz ** 2)
    Fx = float(fx) / float(f)
    Fy = float(fy) / float(f)
    Fz = float(fz) / float(f)
    return [f, Fx, Fy, Fz]


















