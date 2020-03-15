import math

info = "\
        Chapter 27: \n\
            \t motion in a magnetic field\n\
            \t hall effect\n\
            \t magnetic torque\n\
            \t magnetic potential energy\n\
        Chapter 28: \n\
            \t motion in a magnetic field\n\
        Chapter 29: \n\
        Chapter 30: \n\
        Chapter 31: \n\
        Chapter 32: \n\
        Chapter 33: \n\
        Chapter 34: \n\
        Chapter 35: \n\
        Chapter 36: \n\
        Chapter 37:\n\
            \t time dilation\n\
            \t length contraction\n\
            \t gamma\n\
            \t lorentz transformation: x\n\
            \t lorentz transformation: t\n\
            \t lorentz transformation: v\n\
        Other: \n\
            \t right hand rule\n\
            "

QMISSING = "No variable value requested (missing ?)"
SPEEDOFLIGHT = 300000000

def main():

    equation = ""

    while(equation != "exit"):
        
        equation = input("Equation Name: ")

        if equation == "info":
            print(info)

        ########  CHAPTER 27  ##########

        elif equation == "motion in a magnetic field":
            r = input("R: ")
            m = input("m: ")
            v = input("v: ")
            q = input("q: ")
            b = input("b: ")
            print(motionInMagneticField(r,m,v,q,b))

        elif equation == "hall effect":
            n = input("n: ")
            q = input("q: ")
            j = input("J: ")
            b = input("B: ")
            e = input("E: ")
            print(hallEffect(n,q,j,b,e))

        elif equation == "magnetic torque":
            t = input("t: ")
            i = input("I: ")
            b = input("B: ")
            a = input("A: ")
            phi = input("phi: ")
            print(magneticTorque(t,i,b,a,phi))

        elif equation == "magnetic potential energy":
            u = input("U: ")
            miu = input("miu: ")
            b = input("B: ")
            phi = input("phi: ")
            print(magneticPotentialEnergy(u,miu,b,phi))

        ########  CHAPTER 28  ##########



        ########  CHAPTER 29  ##########



        ########  CHAPTER 30  ##########



        ########  CHAPTER 31  ##########



        ########  CHAPTER 32  ##########



        ########  CHAPTER 33  ##########



        ########  CHAPTER 34  ##########



        ########  CHAPTER 35  ##########



        ########  CHAPTER 36  ##########



        ########  CHAPTER 37  ##########
        
        elif equation == "time dilation":
            t = input("t: ")
            t0 = input("t0: ")
            udivc = input("u/c: ")
            print(timeDilation(t,t0,udivc))

        elif equation == "length contraction":
            l = input("l: ")
            l0 = input("l0: ")
            udivc = input("u/c: ")
            print(lengthContraction(l,l0,udivc))

        elif equation == "gamma":
            udivc = input("u/c: ")
            g = input("gamma: ")
            print(calculateGamma(udivc,g))

        elif equation == "lorentz transformation: x":
            x = input("x: ")
            xprime = input("x': ")
            udivc = input("u/c: ")
            t = input("t: ")
            print(lorentzX(x,xprime,udivc,t))

        elif equation == "lorentz transformation: t":
            t = input("t: ")
            tprime = input("t': ")
            udivc = input("u/c: ")
            x = input("x: ")
            print(lorentzT(t,tprime,udivc,x))

        elif equation == "lorentz transformation: v":
            v = input("v: ")
            vprime = input("v': ")
            udivc = input("u/c: ")
            print(lorentzV(v,vprime,udivc))

        ###########  OTHER  ############


##################################################
############ FUNCTION IMPLEMENTATIONS ############
##################################################

##################################
######## HELPER FUNCTIONS ########
##################################

def getAngleInRadians(angle):
    sign = angle.split(" ")[1]
    val = float(angle.split(" ")[0])
    print(val, sign)
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
    else: print(QMISSING)

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
    else: print(QMISSING)

def magneticTorque(t,i,b,a,phi):
    if t == "?":
        return "t = " + str(float(i)*float(b)*float(a)*math.sin(getAngleInRadians(phi)))
    if i == "?":
        return "I = " + str(float(t)/(float(b)*float(a)*math.sin(getAngleInRadians(phi))))
    if b == "?":
        return "B = " + str(float(t)/(float(i)*float(a)*math.sin(getAngleInRadians(phi))))
    if a == "?":
        return "A = " + str(float(t)/(float(i)*float(b)*math.sin(getAngleInRadians(phi))))
    if phi == "?": 
        return "in progress"
        # TODO: sine inverse
    else: print(QMISSING)
    
def magneticPotentialEnergy(u,miu,b,phi):
    if u == "?":
        return "U = " + str(-1*float(miu)*float(b)*math.cos(getAngleInRadians(phi)))
    if miu == "?":
        return "miu = " + str(float(u)/(-1*float(b)*math.cos(getAngleInRadians(phi))))
    if b == "?":
        return "miu = " + str(float(u)/(-1*float(miu)*math.cos(getAngleInRadians(phi))))
    if phi == "?":
        return "in progress"
        # TODO: sine inverse
    else: print(QMISSING)
    

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

################################
########  CHAPTER 32  ##########
################################

################################
########  CHAPTER 33  ##########
################################

################################
########  CHAPTER 34  ##########
################################

################################
########  CHAPTER 35  ##########
################################

################################
########  CHAPTER 36  ##########
################################

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
    else: print(QMISSING)

def timeDilation(t,t0,udivc):
    if t == "?":
        return "t = " + str(float(t0) * getGamma(udivc))
    if t0 == "?":
        return "t0 = " + str(float(t)/getGamma(udivc))
    if udivc == "?":
        gamma = getGamma(udivc)
        return "u/c = " + str(udivcFromGamma)
    else: print(QMISSING)

def lengthContraction(l,l0,udivc):
    if l == "?":
        return "l = " + str(float(l0)/getGamma(udivc))
    if l0 == "?":
        return "l0 = " + str(float(l)*getGamma(udivc))
    if udivc == "?":
        ldivl0 = float(l)/float(l0)
        return "u/c = " + str(math.sqrt(1-(ldivl0*ldivl0)))
    else: print(QMISSING)

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
    else: print(QMISSING)

def lorentzT(t,tprime,udivc,x):
    u = float(udivc) * SPEEDOFLIGHT
    c2 = SPEEDOFLIGHT * SPEEDOFLIGHT

    if tprime == "?":
        return "t' = " + str(getGamma(udivc) * (float(t) - (u*float(x)/c2)))
    if t == "?":
        return "t = " + str((float(tprime)/getGamma(udivc)) + (u*float(x)/c2))
    if x == "?":
        return "x = in progress..."
        # TODO
    if udivc == "?":
        # TODO
        return "u/c = in progress..."

    else: print(QMISSING)

def lorentzV(v,vprime,udivc):


################################
###########  OTHER  ############
################################

if __name__== "__main__" :
    main()