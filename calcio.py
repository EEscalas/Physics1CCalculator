import calc

info = "\
        Chapter 27: \n\
            \t motion in a magnetic field\n\
            \t hall effect\n\
            \t magnetic torque\n\
            \t magnetic potential energy\n\
        Chapter 28: \n\
        Chapter 29: \n\
        Chapter 30: \n\
            \t impedance\n\
        Chapter 31: \n\
        Chapter 32: \n\
        Chapter 33: \n\
            \t law of refraction\n\
            \t total internal reflection\n\
        Chapter 34: \n\
             \t lateral magnification (y)\n\
             \t lateral magnification (s)\n\
             \t lensmaker\n\
             \t focal point\n\
             \t lateral magnification for plane refracting surfaces\n\
        Chapter 35: \n\
            \t double-slit interference bright fringe location\n\
            \t double-slit interference intensity\n\
        Chapter 36: \n\
            \t single-slit diffraction\n\
            \t single-slit diffraction intensity\n\
        Chapter 37:\n\
            \t time dilation\n\
            \t length contraction\n\
            \t gamma\n\
            \t lorentz transformation: x\n\
            \t lorentz transformation: t\n\
            \t lorentz transformation: v\n\
        Other: \n\
            \t degrees from radians\n\
            "

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
            print(calc.motionInMagneticField(r,m,v,q,b))

        elif equation == "hall effect":
            n = input("n: ")
            q = input("q: ")
            j = input("J: ")
            b = input("B: ")
            e = input("E: ")
            print(calc.hallEffect(n,q,j,b,e))

        elif equation == "magnetic torque":
            t = input("t: ")
            i = input("I: ")
            b = input("B: ")
            a = input("A: ")
            phi = input("phi: ")
            print(calc.magneticTorque(t,i,b,a,phi))

        elif equation == "magnetic potential energy":
            u = input("U: ")
            miu = input("miu: ")
            b = input("B: ")
            phi = input("phi: ")
            print(calc.magneticPotentialEnergy(u,miu,b,phi))

        ########  CHAPTER 28  ##########



        ########  CHAPTER 29  ##########



        ########  CHAPTER 30  ##########



        ########  CHAPTER 31  ##########

        elif equation == "impedance":
            r = input("R: ")
            omega = input("omega: ")
            l = input("L: ")
            c = input("C: ")
            print(calc.impedance(r,omega,l,c))

        ########  CHAPTER 32  ##########



        ########  CHAPTER 33  ##########

        elif equation == "law of refraction":
            na = input("na: ")
            nb = input("nb: ")
            theta_a = input("theta (a): ")
            theta_b = input("theta (b): ")
            print(calc.lawOfRefraction(na,nb,theta_a,theta_b))

        elif equation == "total internal reflection":
            na = input("na: ")
            nb = input("nb: ")
            critical = input("theta (critical): ")
            print(calc.totalInternalReflection(na,nb,critical))

        ########  CHAPTER 34  ##########
        
        elif equation == "lateral magnification (y)":
            m = input("m: ")
            y = input("y: ")
            yprime = input("y': ")
            print(calc.lateralMagnificationY(m,y,yprime))

        elif equation == "lateral magnification (s)":
            m = input("m: ")
            s = input("s: ")
            sprime = input("s': ")
            print(calc.lateralMagnificationS(m,s,sprime))

        elif equation == "lateral magnification for plane refracting surfaces":
            m = input("m: ")
            s = input("s: ")
            sprime = input("s': ")
            na = input("na: ")
            nb = input("nb: ")
            print(calc.lateralMagnificationRefractingSurfaces(m,s,sprime,na,nb))

        elif equation == "lensmaker":
            f = input("f: ")
            n = input("n: ")
            r1 = input("R1: ")
            r2 = input("R2: ")
            print(calc.lensmaker(f,n,r1,r2))

        elif equation == "focal point":
            f = input("f: ")
            s = input("s: ")
            sprime = input("s': ")
            print(calc.focalPoint(f,s,sprime))

        


        ########  CHAPTER 35  ##########

        elif equation == "double-slit interference bright fringe location":
            y = input("y: ")
            r = input("R: ")
            m = input("m: ")
            wvl = input("wavelength: ")
            d = input("d: ")
            print(calc.doubleSlitInterferenceBrightFringeLocation(y,r,m,wvl,d))

        elif equation == "double-slit interference intensity":
            i = input("I: ")
            i0 = input("I0: ")
            phi = input("phi: ")
            print(calc.doubleSlitInterferenceIntensity(i,i0,phi))

        ########  CHAPTER 36  ##########

        elif equation == "single-slit diffraction":
            m = input("m: ")
            wvl = input("wavelength: ")
            a = input("a: ")
            theta = input("theta: ")
            print(calc.singleSlitDiffraction(m,wvl,a,theta))        
        
        elif equation == "single-slit diffraction intensity":
            i = input("I: ")
            i0 = input("I0: ")
            a = input("a: ")
            wvl = input("wavelength: ")
            theta = input("theta: ")
            print(calc.singleSlitDiffractionIntensity(i,i0,a,wvl,theta))

        ########  CHAPTER 37  ##########
        
        elif equation == "time dilation":
            t = input("t: ")
            t0 = input("t0: ")
            udivc = input("u/c: ")
            print(calc.timeDilation(t,t0,udivc))

        elif equation == "length contraction":
            l = input("l: ")
            l0 = input("l0: ")
            udivc = input("u/c: ")
            print(calc.lengthContraction(l,l0,udivc))

        elif equation == "gamma":
            udivc = input("u/c: ")
            g = input("gamma: ")
            print(calc.calculateGamma(udivc,g))

        elif equation == "lorentz transformation: x":
            x = input("x: ")
            xprime = input("x': ")
            udivc = input("u/c: ")
            t = input("t: ")
            print(calc.lorentzX(x,xprime,udivc,t))

        elif equation == "lorentz transformation: t":
            t = input("t: ")
            tprime = input("t': ")
            udivc = input("u/c: ")
            x = input("x: ")
            print(calc.lorentzT(t,tprime,udivc,x))

        elif equation == "lorentz transformation: v":
            v = input("v: ")
            vprime = input("v': ")
            udivc = input("u/c: ")
            print(calc.lorentzV(v,vprime,udivc))

        ###########  OTHER  ############
        
        elif equation == "degrees from radians":
            rad = input("angle (in radians): ")
            print(calc.radiansToDegrees(rad))


if __name__== "__main__" :
    main()