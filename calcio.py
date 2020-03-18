import calc

info = "\
        Chapter 27: \n\
            \t motion in a magnetic field\n\
            \t hall effect\n\
            \t magnetic torque\n\
            \t magnetic potential energy\n\
        Chapter 28: \n\
        Chapter 29: \n\
            \t displacement current density (two plates)\n\
            \t B field from Ampere's Law (two plates)\n\
        Chapter 30: \n\
        Chapter 31: \n\
            \t impedance\n\
            \t L-R-C phase angle\n\
            \t voltage\n\
            \t voltage given amplitude\n\
            \t current\n\
            \t average power\n\
            \t voltage (R)\n\
            \t voltage (L)\n\
            \t voltage (C)\n\
            \t all voltages given max \n\
        Chapter 32: \n\
            \t electromagnetic wave amplitudes\n\
            \t average pressure\n\
            \t instensity from power\n\
        Chapter 33: \n\
            \t law of refraction\n\
            \t total internal reflection\n\
        Chapter 34: \n\
             \t lateral magnification (y)\n\
             \t lateral magnification (s)\n\
             \t lateral magnification (skip m)\n\
             \t lateral magnification for refracting surfaces\n\
             \t object and image distances (spherical refracting surface)\n\
             \t object and image distances (plane refracting surface)\n\
             \t lensmaker\n\
             \t focal point\n\
             \t focal point concave spherical mirror\n\
             \t focal length\n\
        Chapter 35: \n\
            \t bright fringe location\n\
            \t double-slit interference\n\
            \t double-slit interference intensity\n\
            \t phase angle\n\
        Chapter 36: \n\
            \t bright fringe location\n\
            \t single-slit diffraction\n\
            \t single-slit diffraction intensity\n\
        Chapter 37:\n\
            \t time dilation\n\
            \t length contraction\n\
            \t simple speed\n\
            \t simple speed relative to light\n\
            \t gamma\n\
            \t lorentz transformation: x\n\
            \t lorentz transformation: t\n\
            \t lorentz transformation: v\n\
        Other: \n\
            \t degrees from radians\n\
            \t wave basics\n\
            "

def main():

    equation = ""
    prev = ""

    while(equation != "exit"):
        
        equation = input("Equation Name: ")

        if equation == "info":
            print(info)
        elif equation == "prev":
            equation = prev
            print("now running",prev,"function again")

        ########  CHAPTER 27  ##########

        if equation == "motion in a magnetic field":
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

        elif equation == "displacement current density (two plates)":
            j = input("j: ")
            i = input("i: ")
            r = input("R: ")
            print(calc.dispCurrentDensity(j,i,r))

        elif equation == "B field from Ampere's Law (two plates)":
            r = input("r: ")
            R = input("R: ")
            i = input("i(c): ")
            print(calc.bFromAmpereTwoPlates(r,R,i))

        ########  CHAPTER 30  ##########



        ########  CHAPTER 31  ##########

        elif equation == "impedance":
            omega = input("omega: ")
            l = input("L: ")
            r = input("R: ")
            c = input("C: ")
            print(calc.impedance(r,omega,l,c))

        elif equation == "L-R-C phase angle":
            phi = input("phi (phase angle): ")
            w = input("omega (angular frequency): ")
            l = input("L: ")
            r = input("R: ")
            c = input("C: ")
            print(calc.lrcPhaseAngle(phi,w,l,r,c))

        elif equation == "voltage":
            i = input("I: ")
            l = input("L: ")
            r = input("R: ")
            c = input("C: ")
            t = input("t: ")
            w = input("omega: ")
            phi = input("phi: ")
            print(calc.voltage(i,l,r,c,w,phi,t))

        elif equation == "voltage given amplitude":
            v = input("V: ")
            t = input("t: ")
            w = input("omega: ")
            phi = input("phi: ")
            print(calc.voltageGivenAmplitude(v,w,phi,t))

        elif equation == "current":
            i = input("I (amplitude): ")
            w = input("omega: ")
            t = input("t: ")
            phi = input("phi: ")
            print(calc.current(i,w,t,phi))

        elif equation == "average power":
            v = input("V: ")
            i = input("I: ")
            phi = input("phi: ")
            print(calc.power(v,i,phi))

        elif equation == "voltage (R)":
            i = input("I: ")
            r = input("R: ")
            w = input("omega: ")
            t = input("t: ")
            v = float(i)*float(r)
            print(calc.voltageGivenAmplitude(v,w,"0 degrees",t))
        
        elif equation == "voltage (L)":
            i = input("I: ")
            l = input("L: ")
            w = input("omega: ")
            t = input("t: ")
            v = float(i)*float(w)*float(l)
            print(calc.voltageGivenAmplitude(v,w,"90 degrees",t))

        elif equation == "voltage (C)":
            i = input("I: ")
            c = input("C: ")
            w = input("omega: ")
            t = input("t: ")
            v = float(i)*(1/(float(w)*float(c)))
            print(calc.voltageGivenAmplitude(v,w,"-90 degrees",t))

        elif equation == "all voltages given max voltage":
            v = input("V: ")
            i = input("I: ")
            t = input("t: ")
            w = input("omega: ")
            phi = input("phi: ")
            l = input("L: ")
            r = input("R: ")
            c = input("C: ")
            print("v",calc.voltageGivenAmplitude(v,w,phi,t))
            vr = float(i)*float(r)
            print("R", calc.voltageGivenAmplitude(vr,w,"0 degrees",t))
            vl = float(i)*float(w)*float(l)
            print("L",calc.voltageGivenAmplitude(vl,w,"90 degrees",t))
            vc = float(i)*(1/(float(w)*float(c)))
            print("C",calc.voltageGivenAmplitude(vc,w,"-90 degrees",t))

        ########  CHAPTER 32  ##########
        """
        elif equation == "electromagnetic wave cross product":
            E = input("E (sign direction): ")
            B = input("B (sign direction): ")
            W = input("Electromagnetic wave (sign direction): ")
            print(calc.crossProduct(E,B,W))
        """

        if equation == "electromagnetic wave amplitudes":
            B = input("Bmax: ")
            E = input("Emax: ")
            print(calc.electromagneticWaveAmplitudes(B,E))

        if equation == "average pressure":
            Emax = input("Emax: ")
            Bmax = input("Bmax: ")
            print(calc.averagePressure(Emax,Bmax))

        if equation == "intensity from power":
            i = input("I: ")
            p = input("p (power): ")
            a = input("A (area): ")
            print(calc.intensityFromPower(i,p,a))


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

        elif equation == "lateral magnification (skip m)":
            s = input("s: ")
            sprime = input("s': ")
            y = input("y: ")
            yprime = input("y': ")
            print(calc.lateralMagnification(s,sprime,y,yprime))

        elif equation == "lateral magnification for refracting surfaces":
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

        elif equation == "focal length":
            r = input("R: ")
            f = input("F: ")
            print(calc.focalLength(r,f))

        elif equation == "focal point concave spherical mirror":
            r = input("R: ")
            s = input("s: ")
            sprime = input("s': ")
            print(calc.focalPointCSM(r,s,sprime))

        elif equation == "object and image distances (spherical refracting surface)":
            na = input("na: ")
            nb = input("nb: ")
            s = input("s: ")
            sprime = input("s': ")
            r = input("R: ")
            print(calc.distancesSphericalRefracting(na,nb,s,sprime,r))

        elif equation == "object and image distances (plane refracting surface)":
            na = input("na: ")
            nb = input("nb: ")
            s = input("s: ")
            sprime = input("s': ")
            print(calc.distancesPlaneRefracting(na,nb,s,sprime))

        ########  CHAPTER 35  ##########

        elif equation == "bright fringe location":
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

        elif equation == "double-slit interference":
            interferenceType = input("destructive or constructive (c/d): ")
            if interferenceType == "c":
                offset = 0
            else: offset = 0.5
            d = input("d: ")
            theta = input("theta: ")
            wvl = input("wavelength: ")
            m = input("m: ")
            print(calc.doubleSlitInterference(offset,d,theta,wvl,m))

        elif equation == "phase angle":
            phi = input("phase angle: ")
            wvl = input("wavelength: ")
            diff = input("(r2 - r1): ")
            print(calc.phaseAngle(phi,wvl,diff))

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
            option = input("sin(theta) or theta (s/t): ")
            if option == "s":
                theta = input("sin(theta): ")
            else: theta = input("theta: ")
            print(calc.singleSlitDiffractionIntensity(i,i0,a,wvl,theta,option))

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

        elif equation == "simple speed":
            v = input("v: ")
            t = input("t: ")
            d = input("d: ")
            print(calc.speedTimeDist(v,t,d))

        elif equation == "simple speed relative to light":
            udivc = input("u/c: ")
            t = input("t: ")
            d = input("d: ")
            v = float(udivc) * calc.SPEEDOFLIGHT
            print(calc.speedTimeDist(v,t,d))

        ###########  OTHER  ############
        
        elif equation == "degrees from radians":
            rad = input("angle (in radians): ")
            print(calc.radiansToDegrees(rad))

        elif equation == "wave basics":
            v = input("v: ")
            f = input("f: ")
            wvl = input("wavelength: ")
            print(calc.wave(v,f,wvl))

        prev = equation

if __name__== "__main__" :
    main()