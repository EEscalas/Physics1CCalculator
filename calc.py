import math

QMISSING = "No variable value requested (missing ?)"
SPEEDOFLIGHT = 300000000

##################################################
############ FUNCTION IMPLEMENTATIONS ############
##################################################

##################################
######## HELPER FUNCTIONS ########
##################################

def getRadiansFromInput(angle):
    contents = angle.split(" ")
    if len(contents) != 2:
        raise ValueError('units not given for angle')
    sign = contents[1]
    val = float(contents[0])
    if sign != "rad": # convert to radians
        val = val*math.pi/180
    return val

################################
########  CHAPTER 27  ##########
################################

def motionInMagneticField(r, m, v, q, b): 
    if r == "?":
        return ("R = " + str(float(m)*float(v)/(abs(float(q))*float(b))))
    if m == "?":
        return ("m = " + str((float(r)*abs(float(q))*float(b))/float(v)))
    if v == "?":
        return ("v = " + str((float(r)*abs(float(q))*float(b))/float(m)))
    if b == "?":
        return ("b = " + str(float(m)*float(v)/(abs(float(q))*float(r))))
    if q == "?":
        return ("abs(q) = " + str(float(m)*float(v)/(float(r)*float(b))))
    else: return QMISSING

def hallEffect(n,q,j,b,e):
    if n == "?":
        return "n = " + str(-1*float(j)*float(b)/(float(e)*float(q)))
    if q == "?":
        return "q = " + str(-1*float(j)*float(b)/(float(e)*float(n)))
    if j == "?":
        return "J = " + str(-1*float(n)*float(q)*float(e)/(float(b)))
    if b == "?":
        return "B = " + str(-1*float(n)*float(q)*float(e)/(float(j)))
    if e == "?":
        return "E = " + str(-1*float(j)*float(b)/(float(n)*float(q)))
    else: return QMISSING

def magneticTorque(t,i,b,a,phi):
    if t == "?":
        return "t = " + str(float(i)*float(b)*float(a)*math.sin(getRadiansFromInput(phi)))
    if i == "?":
        return "I = " + str(float(t)/(float(b)*float(a)*math.sin(getRadiansFromInput(phi))))
    if b == "?":
        return "B = " + str(float(t)/(float(i)*float(a)*math.sin(getRadiansFromInput(phi))))
    if a == "?":
        return "A = " + str(float(t)/(float(i)*float(b)*math.sin(getRadiansFromInput(phi))))
    if phi == "?": 
        return "in progress"
        # TODO: sine inverse
    else: return QMISSING
    
def magneticPotentialEnergy(u,miu,b,phi):
    if u == "?":
        return "U = " + str(-1*float(miu)*float(b)*math.cos(getRadiansFromInput(phi)))
    if miu == "?":
        return "miu = " + str(float(u)/(-1*float(b)*math.cos(getRadiansFromInput(phi))))
    if b == "?":
        return "b = " + str(float(u)/(-1*float(miu)*math.cos(getRadiansFromInput(phi))))
    if phi == "?":
        return "phi = " + str(math.acos(float(u)/(-1*float(b)*float(miu)))) + " rad"
    else: return QMISSING
    
################################
########  CHAPTER 28  ##########
################################

################################
########  CHAPTER 29  ##########
################################

################################
########  CHAPTER 30  ##########
################################

################################
########  CHAPTER 31  ##########
################################

def impedance(r,w,l,c):
    return "Z = " + str(math.sqrt(math.pow(float(r),2) + math.pow((float(w)*float(l)) - (1/(float(w) * float(c))),2)))

################################
########  CHAPTER 32  ##########
################################

################################
########  CHAPTER 33  ##########
################################

def lawOfRefraction(na,nb,theta_a,theta_b):
    if na == "?":
        return "na = " + str(math.sin(getRadiansFromInput(theta_a))/(float(nb)*math.sin(getRadiansFromInput(theta_b))))
    if nb == "?":
        return "nb = " + str(math.sin(getRadiansFromInput(theta_b))/(float(na)*math.sin(getRadiansFromInput(theta_a))))
    if theta_a == "?":
        return "theta (a) = " + str(math.asin((float(nb)*math.sin(getRadiansFromInput(theta_b)))/float(na))) + " rad"
    if theta_b == "?":
        return "theta (b) = " + str(math.asin((float(na)*math.sin(getRadiansFromInput(theta_a)))/float(nb))) + " rad"
    else: return QMISSING

def totalInternalReflection(na,nb,critical):
    if na == "?":
        return "na = " + str(float(nb)/math.sin(getRadiansFromInput(critical)))
    if nb == "?":
        return "nb = " + str(float(na)*math.sin(getRadiansFromInput(critical)))
    if critical == "?":
        return "theta (critical) = " + str(math.asin(float(nb)/float(na))) + " rad"
    else: return QMISSING

################################
########  CHAPTER 34  ##########
################################

def lateralMagnificationY(m,y,yprime):
    if m == "?":
        return "m = " + str(float(yprime)/float(y))
    if y == "?":
        return "y = " + str(float(yprime)/float(m))
    if yprime == "?":
        return "y' = " + str(float(m)*float(yprime))
    else: return QMISSING

def lateralMagnificationS(m,s,sprime):
    if m == "?":
        return "m = " + str(-1*float(sprime)/float(s))
    if s == "?":
        return "s = " + str(-1*float(sprime)/float(m))
    if sprime == "?":
        return "s' = " + str(-1*float(m)*float(sprime))
    else: return QMISSING

def lateralMagnificationRefractingSurfaces(m,s,sprime,na,nb):
    if m == "?":
        return "m = " + str(-1*float(na)*float(sprime)/(float(nb)*float(s)))
    if nb == "?":
        return "nb = " + str(-1*float(na)*float(sprime)/(float(m)*float(s)))
    if s == "?":
        return "s = " + str(-1*float(na)*float(sprime)/(float(m)*float(nb)))
    if sprime == "?":
        return "s = " + str(-1*float(m)*float(nb)*float(s)/float(na))
    if na == "?":
        return "s = " + str(-1*float(m)*float(nb)*float(s)/float(sprime))
    else: return QMISSING

def lensmaker(f,n,r1,r2):
    if f == "?":
        return "f = " + str(1/((float(n) - 1)) * ((1/float(r1)) - (1/float(r2))))
    if n == "?":
        return "n = " + str((1/(float(f) * ((1/float(r1)) - (1/float(r2))))) + 1)
    if r1 == "?":
        return "R1 = " + str((1/(float(f) * (float(n) - 1))) + (1/float(r2)))
    if r2 == "?":
        return "R2 = " + str(-1*(1/(float(f) * (float(n) - 1))) + (1/float(r1)))
    else: return QMISSING

def focalPoint(f,s,sprime):
    if f == "?":
        return "f = " + str(1/((1/float(s)) + (1/float(sprime))))
    if s == "?":
        return "s = " + str(1/((1/float(f)) - (1/float(sprime))))
    if sprime == "?":
        return "s' = " + str(1/((1/float(f)) - (1/float(s))))
    else: return QMISSING

def focalLength(r,f):
    if r == "?":
        return "R = " + str(float(f)*2)
    if f == "?":
        return "F = " + str(float(r)/2)
    else: return QMISSING

################################
########  CHAPTER 35  ##########
################################

def doubleSlitInterferenceBrightFringeLocation(y,r,m,wvl,d):
    if y == "?":
        return "y = " + str(float(r)*float(m)*float(wvl)/float(d))
    if d == "?":
        return "d = " + str(float(r)*float(m)*float(wvl)/float(y))
    if r == "?":
        return "R = " + str(float(d)*float(y)/(float(wvl)*float(m)))
    if m == "?":
        return "m = " + str(float(d)*float(y)/(float(wvl)*float(r)))
    if wvl == "?":
        return "wavelength = " + str(float(d)*float(y)/(float(r)*float(m)))
    else: return QMISSING

def doubleSlitInterferenceIntensity(i,i0,phi):
    return QMISSING

################################
########  CHAPTER 36  ##########
################################

def singleSlitDiffraction(m,wvl,a,theta):
    if m == "?":
        return "m = " + str(float(math.sin(getRadiansFromInput((theta)))*float(a)/(float(wvl))))
    if wvl == "?":
        return "wavelength = " + str(float(math.sin(getRadiansFromInput((theta)))*float(a)/(float(m))))
    if a == "?":
        return "a = " + str(float(m)*float(wvl)/float(math.sin(getRadiansFromInput((theta)))))
    if theta == "?":
        return "theta = " + str(math.asin(float(m)*float(wvl)/float(a))) + " rad"
    else: return QMISSING

def singleSlitDiffractionIntensity(i,i0,a,wvl,theta):
    if a == "?" or wvl == "?" or theta == "?": return "too much math, must do by hand"
    beta = 2*math.pi*float(a)*math.sin(getRadiansFromInput((theta)))/float(wvl)
    if i == "?" and i0 == "?":
        return "I = I0 * " + str(math.pow((math.sin(beta/2.0)/(beta/2.0)),2))
    if i == "?" and i0 != "?":
        return "I = " + str(float(i0)*math.pow((math.sin(beta/2.0)/(beta/2.0)),2))
    else: return QMISSING

################################
########  CHAPTER 37  ##########
################################

def getGamma(udivc):
    return float(1/(math.sqrt(1 - (float(udivc)*float(udivc)))))

def udivcFromGamma(gamma):
    return math.sqrt(1-(1/float(gamma)*float(gamma)))

def calculateGamma(udivc,gamma):
    if udivc == "?":
        return "u/c = " + str(udivcFromGamma(gamma))
    if gamma == "?":
        return "gamma = " + str(getGamma(udivc))
    else: return QMISSING

def timeDilation(t,t0,udivc):
    if t == "?":
        return "t = " + str(float(t0) * getGamma(udivc))
    if t0 == "?":
        return "t0 = " + str(float(t)/getGamma(udivc))
    if udivc == "?":
        gamma = getGamma(udivc)
        return "u/c = " + str(udivcFromGamma(gamma))
    else: return QMISSING

def lengthContraction(l,l0,udivc):
    if l == "?":
        return "l = " + str(float(l0)/getGamma(udivc))
    if l0 == "?":
        return "l0 = " + str(float(l)*getGamma(udivc))
    if udivc == "?":
        ldivl0 = float(l)/float(l0)
        return "u/c = " + str(math.sqrt(1-(ldivl0*ldivl0)))
    else: return QMISSING

def lorentzX(x,xprime,udivc,t):
    u = float(udivc) * SPEEDOFLIGHT
    if x == "?":
        return "x = " + str((float(xprime)/getGamma(udivc)) + (u*float(t)))
    if xprime == "?":
        return "x' = " + str(getGamma(udivc) * (float(x) - (u*float(t))))
    if udivc == "?":
        return "u/c = " + str(udivcFromGamma(float(xprime)/(float(x) - (float(u)*float(t)))))
    if t == "?":
        return "t = " + str((float(x) - (float(xprime)/getGamma(udivc)))/u)
    else: return QMISSING

def lorentzT(t,tprime,udivc,x):
    if udivc == "?":
        return "outside scope of program: find out by hand"
    
    u = float(udivc) * SPEEDOFLIGHT
    c2 = SPEEDOFLIGHT * SPEEDOFLIGHT

    if tprime == "?":
        return "t' = " + str(getGamma(udivc) * (float(t) - (u*float(x)/c2)))
    if t == "?":
        return "t = " + str((float(tprime)/getGamma(udivc)) + (u*float(x)/c2))
    if x == "?":
        return "x = " + str(((float(t) - (float(tprime)/getGamma(udivc))) * math.pow(SPEEDOFLIGHT,2))/u)
    else: return QMISSING

def lorentzV(v,vprime,udivc):
    if udivc == "?":
        return "outside scope of program: find out by hand"
    
    u = float(udivc) * SPEEDOFLIGHT
    if v == "?":
        return "v = " + str((float(vprime) + u)/(1 + ((u * float(vprime))/math.pow(SPEEDOFLIGHT,2))))
    if vprime == "?":
        return "v' = " + str((float(v) - u)/(1 - ((u * float(v))/math.pow(SPEEDOFLIGHT,2))))
    else: return QMISSING

################################
###########  OTHER  ############
################################

def radiansToDegrees(rad):
    return "angle (in degrees) = " + str(float(rad)*180/math.pi) + "°"

def wave(v,f,wvl):
    if v == "?":
        return "v = " + str(float(f) * float(wvl))
    if f == "?":
        return "f = " + str(float(v)/float(wvl))
    if wvl == "?":
        return "wavelength = " + str(float(v)/float(f))
    else: return QMISSING
