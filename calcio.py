import calc

info = "\
        Chapter 27: \n\
            \t 1) motion in a magnetic field\n\
            \t 2) hall effect\n\
            \t 3) magnetic torque\n\
            \t 4) magnetic potential energy\n\
        Chapter 28: \n\
        Chapter 29: \n\
            \t 5) displacement current density (two plates)\n\
            \t 6) B field from Ampere's Law (two plates)\n\
        Chapter 30: \n\
        Chapter 31: \n\
            \t 7) impedance\n\
            \t 8) L-R-C phase angle\n\
            \t 9) voltage\n\
            \t 10) voltage given amplitude\n\
            \t 11) current\n\
            \t 12) average power\n\
            \t 13) voltage (R)\n\
            \t 14) voltage (L)\n\
            \t 15) voltage (C)\n\
            \t 16) all voltages given max voltage\n\
        Chapter 32: \n\
            \t 17) electromagnetic wave amplitudes\n\
            \t 18) average pressure\n\
            \t 19) intensity from power\n\
        Chapter 33: \n\
            \t 20) law of refraction\n\
            \t 21) total internal reflection\n\
        Chapter 34: \n\
             \t 22) lateral magnification (y)\n\
             \t 23) lateral magnification (s)\n\
             \t 24) lateral magnification (skip m)\n\
             \t 25) lateral magnification for refracting surfaces\n\
             \t 26) object and image distances (spherical refracting surface)\n\
             \t 27) object and image distances (plane refracting surface)\n\
             \t 28) lensmaker\n\
             \t 29) focal point\n\
             \t 30) focal point concave spherical mirror\n\
             \t 31) focal length\n\
        Chapter 35: \n\
            \t 32) bright fringe location\n\
            \t 33) double-slit interference\n\
            \t 34) double-slit interference intensity\n\
            \t 35) phase angle\n\
        Chapter 36: \n\
            \t 36) bright fringe location\n\
            \t 37) single-slit diffraction\n\
            \t 38) single-slit diffraction intensity\n\
        Chapter 37:\n\
            \t 39) time dilation\n\
            \t 40) length contraction\n\
            \t 41) simple speed\n\
            \t 42) simple speed relative to light\n\
            \t 43) gamma\n\
            \t 44) lorentz transformation: x\n\
            \t 45) lorentz transformation: t\n\
            \t 46) lorentz transformation: v\n\
        Other: \n\
            \t 47) degrees from radians\n\
            \t 48) wave basics\n\
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

        if equation == "motion in a magnetic field" or equation == "1":
            print("motion in a magnetic field")
            r = input("R: ")
            m = input("m: ")
            v = input("v: ")
            q = input("q: ")
            b = input("b: ")
            print(calc.motionInMagneticField(r,m,v,q,b))

        elif equation == "hall effect" or equation == "2":
            print("hall effect")
            n = input("n: ")
            q = input("q: ")
            j = input("J: ")
            b = input("B: ")
            e = input("E: ")
            print(calc.hallEffect(n,q,j,b,e))

        elif equation == "magnetic torque" or equation == "3":
            print("magnetic torque")
            t = input("t: ")
            i = input("I: ")
            b = input("B: ")
            a = input("A: ")
            phi = input("phi: ")
            print(calc.magneticTorque(t,i,b,a,phi))

        elif equation == "magnetic potential energy" or equation == "4":
            print("magnetic potential energy")
            u = input("U: ")
            miu = input("miu: ")
            b = input("B: ")
            phi = input("phi: ")
            print(calc.magneticPotentialEnergy(u,miu,b,phi))

        ########  CHAPTER 28  ##########



        ########  CHAPTER 29  ##########

        elif equation == "displacement current density (two plates)" or equation == "5":
            print("displacement current density (two plates)")
            j = input("j: ")
            i = input("i: ")
            r = input("R: ")
            print(calc.dispCurrentDensity(j,i,r))

        elif equation == "B field from Ampere's Law (two plates)" or equation == "6":
            print("B field from Ampere's Law (two plates)")
            r = input("r: ")
            R = input("R: ")
            i = input("i(c): ")
            print(calc.bFromAmpereTwoPlates(r,R,i))

        ########  CHAPTER 30  ##########



        ########  CHAPTER 31  ##########

        elif equation == "impedance" or equation == "7":
            print("impedance")
            omega = input("omega: ")
            l = input("L: ")
            r = input("R: ")
            c = input("C: ")
            print(calc.impedance(r,omega,l,c))

        elif equation == "L-R-C phase angle" or equation == "8":
            print("L-R-C phase angle")
            phi = input("phi (phase angle): ")
            w = input("omega (angular frequency): ")
            l = input("L: ")
            r = input("R: ")
            c = input("C: ")
            print(calc.lrcPhaseAngle(phi,w,l,r,c))

        elif equation == "voltage" or equation == "9":
            print("voltage")
            i = input("I: ")
            l = input("L: ")
            r = input("R: ")
            c = input("C: ")
            t = input("t: ")
            w = input("omega: ")
            phi = input("phi: ")
            print(calc.voltage(i,l,r,c,w,phi,t))

        elif equation == "voltage given amplitude" or equation == "10":
            print("voltage given amplitude")
            v = input("V: ")
            t = input("t: ")
            w = input("omega: ")
            phi = input("phi: ")
            print(calc.voltageGivenAmplitude(v,w,phi,t))

        elif equation == "current" or equation == "11":
            print("current")
            i = input("I (amplitude): ")
            w = input("omega: ")
            t = input("t: ")
            phi = input("phi: ")
            print(calc.current(i,w,t,phi))

        elif equation == "average power" or equation == "12":
            print("average power")
            v = input("V: ")
            i = input("I: ")
            phi = input("phi: ")
            print(calc.power(v,i,phi))

        elif equation == "voltage (R)" or equation == "13":
            print("voltage (R)")
            i = input("I: ")
            r = input("R: ")
            w = input("omega: ")
            t = input("t: ")
            v = float(i)*float(r)
            print(calc.voltageGivenAmplitude(v,w,"0 degrees",t))
        
        elif equation == "voltage (L)" or equation == "14":
            print("voltage (L)")
            i = input("I: ")
            l = input("L: ")
            w = input("omega: ")
            t = input("t: ")
            v = float(i)*float(w)*float(l)
            print(calc.voltageGivenAmplitude(v,w,"90 degrees",t))

        elif equation == "voltage (C)" or equation == "15":
            print("voltage (C)")
            i = input("I: ")
            c = input("C: ")
            w = input("omega: ")
            t = input("t: ")
            v = float(i)*(1/(float(w)*float(c)))
            print(calc.voltageGivenAmplitude(v,w,"-90 degrees",t))

        elif equation == "all voltages given max voltage" or equation == "16":
            print("all voltages given max voltage")
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

        if equation == "electromagnetic wave amplitudes" or equation == "17":
            print("electromagnetic wave amplitudes")
            B = input("Bmax: ")
            E = input("Emax: ")
            print(calc.electromagneticWaveAmplitudes(B,E))

        if equation == "average pressure" or equation == "18":
            print("average pressure")
            Emax = input("Emax: ")
            Bmax = input("Bmax: ")
            print(calc.averagePressure(Emax,Bmax))

        if equation == "intensity from power" or equation == "19":
            print("intensity from power")
            i = input("I: ")
            p = input("p (power): ")
            a = input("A (area): ")
            print(calc.intensityFromPower(i,p,a))


        ########  CHAPTER 33  ##########

        elif equation == "law of refraction" or equation == "20":
            print("law of refraction")
            na = input("na: ")
            nb = input("nb: ")
            theta_a = input("theta (a): ")
            theta_b = input("theta (b): ")
            print(calc.lawOfRefraction(na,nb,theta_a,theta_b))

        elif equation == "total internal reflection" or equation == "21":
            print("total internal reflection")
            na = input("na: ")
            nb = input("nb: ")
            critical = input("theta (critical): ")
            print(calc.totalInternalReflection(na,nb,critical))

        ########  CHAPTER 34  ##########
        
        elif equation == "lateral magnification (y)" or equation == "22":
            print("lateral magnification (y)")
            m = input("m: ")
            y = input("y: ")
            yprime = input("y': ")
            print(calc.lateralMagnificationY(m,y,yprime))

        elif equation == "lateral magnification (s)" or equation == "23":
            print("lateral magnification (s)")
            m = input("m: ")
            s = input("s: ")
            sprime = input("s': ")
            print(calc.lateralMagnificationS(m,s,sprime))

        elif equation == "lateral magnification (skip m)" or equation == "24":
            print("lateral magnification (skip m)")
            s = input("s: ")
            sprime = input("s': ")
            y = input("y: ")
            yprime = input("y': ")
            print(calc.lateralMagnification(s,sprime,y,yprime))

        elif equation == "lateral magnification for refracting surfaces" or equation == "25":
            print("lateral magnification for refracting surfaces")
            m = input("m: ")
            s = input("s: ")
            sprime = input("s': ")
            na = input("na: ")
            nb = input("nb: ")
            print(calc.lateralMagnificationRefractingSurfaces(m,s,sprime,na,nb))

        elif equation == "lensmaker" or equation == "28":
            print("lensmaker")
            f = input("f: ")
            n = input("n: ")
            r1 = input("R1: ")
            r2 = input("R2: ")
            print(calc.lensmaker(f,n,r1,r2))

        elif equation == "focal point" or equation == "29":
            print("focal point")
            f = input("f: ")
            s = input("s: ")
            sprime = input("s': ")
            print(calc.focalPoint(f,s,sprime))

        elif equation == "focal length" or equation == "31":
            print("focal length")
            r = input("R: ")
            f = input("F: ")
            print(calc.focalLength(r,f))

        elif equation == "focal point concave spherical mirror" or equation == "30":
            print("focal point concave spherical mirror")
            r = input("R: ")
            s = input("s: ")
            sprime = input("s': ")
            print(calc.focalPointCSM(r,s,sprime))

        elif equation == "object and image distances (spherical refracting surface)" or equation == "26":
            print("object and image distances (spherical refracting surface)")
            na = input("na: ")
            nb = input("nb: ")
            s = input("s: ")
            sprime = input("s': ")
            r = input("R: ")
            print(calc.distancesSphericalRefracting(na,nb,s,sprime,r))

        elif equation == "object and image distances (plane refracting surface)" or equation == "27":
            print("object and image distances (plane refracting surface)")
            na = input("na: ")
            nb = input("nb: ")
            s = input("s: ")
            sprime = input("s': ")
            print(calc.distancesPlaneRefracting(na,nb,s,sprime))

        ########  CHAPTER 35  ##########

        elif equation == "bright fringe location" or equation == "32" or equation == "36":
            print('bright fringe location')
            y = input("y: ")
            r = input("R: ")
            m = input("m: ")
            wvl = input("wavelength: ")
            d = input("d: ")
            print(calc.doubleSlitInterferenceBrightFringeLocation(y,r,m,wvl,d))

        elif equation == "double-slit interference intensity" or equation == "34":
            print("double-slit interference intensity")
            i = input("I: ")
            i0 = input("I0: ")
            phi = input("phi: ")
            print(calc.doubleSlitInterferenceIntensity(i,i0,phi))

        elif equation == "double-slit interference" or equation == "33":
            print("double-slit interference")
            interferenceType = input("destructive or constructive (c/d): ")
            if interferenceType == "c":
                offset = 0
            else: offset = 0.5
            d = input("d: ")
            theta = input("theta: ")
            wvl = input("wavelength: ")
            m = input("m: ")
            print(calc.doubleSlitInterference(offset,d,theta,wvl,m))

        elif equation == "phase angle" or equation == "35":
            print("phase angle")
            phi = input("phase angle: ")
            wvl = input("wavelength: ")
            diff = input("(r2 - r1): ")
            print(calc.phaseAngle(phi,wvl,diff))

        ########  CHAPTER 36  ##########

        elif equation == "single-slit diffraction" or equation == "37":
            print("single-slit diffraction")
            m = input("m: ")
            wvl = input("wavelength: ")
            a = input("a: ")
            theta = input("theta: ")
            print(calc.singleSlitDiffraction(m,wvl,a,theta))        
        
        elif equation == "single-slit diffraction intensity" or equation == "38":
            print("single-slit diffraction intensity")
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
        
        elif equation == "time dilation" or equation == "39":
            print("time dilation")
            t = input("t: ")
            t0 = input("t0: ")
            udivc = input("u/c: ")
            print(calc.timeDilation(t,t0,udivc))

        elif equation == "length contraction" or equation == "40":
            print("length contraction")
            l = input("l: ")
            l0 = input("l0: ")
            udivc = input("u/c: ")
            print(calc.lengthContraction(l,l0,udivc))

        elif equation == "gamma" or equation == "43":
            print("gamma")
            udivc = input("u/c: ")
            g = input("gamma: ")
            print(calc.calculateGamma(udivc,g))

        elif equation == "lorentz transformation: x" or equation == "44":
            print("lorentz transformation: x")
            x = input("x: ")
            xprime = input("x': ")
            udivc = input("u/c: ")
            t = input("t: ")
            print(calc.lorentzX(x,xprime,udivc,t))

        elif equation == "lorentz transformation: t" or equation == "45":
            print("lorentz transformation: t")
            t = input("t: ")
            tprime = input("t': ")
            udivc = input("u/c: ")
            x = input("x: ")
            print(calc.lorentzT(t,tprime,udivc,x))

        elif equation == "lorentz transformation: v" or equation == "46":
            print("lorentz transformation: v")
            v = input("v: ")
            vprime = input("v': ")
            udivc = input("u/c: ")
            print(calc.lorentzV(v,vprime,udivc))

        elif equation == "simple speed" or equation == "41":
            print("simple speed")
            v = input("v: ")
            t = input("t: ")
            d = input("d: ")
            print(calc.speedTimeDist(v,t,d))

        elif equation == "simple speed relative to light" or equation == "42":
            print("simple speed relative to light")
            udivc = input("u/c: ")
            t = input("t: ")
            d = input("d: ")
            v = float(udivc) * calc.SPEEDOFLIGHT
            print(calc.speedTimeDist(v,t,d))

        ###########  OTHER  ############
        
        elif equation == "degrees from radians" or equation == "47":
            print("degrees from radians")
            rad = input("angle (in radians): ")
            print(calc.radiansToDegrees(rad))

        elif equation == "wave basics" or equation == "48":
            print("wave basics")
            v = input("v: ")
            f = input("f: ")
            wvl = input("wavelength: ")
            print(calc.wave(v,f,wvl))

        prev = equation

if __name__== "__main__" :
    main()