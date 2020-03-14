# Python program showing  
# a use of raw_input() 

info = "\
        Chapter 27: \n\
            \t magnetic forces\n\
            \t magnetic field lines and flux\n\
            \t motion in a magnetic field\n\
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
        Other: \n\
            \t right hand rule\n\
            "

def main():

    equation = ""

    while(equation != "exit"):
        
        equation = input("Equation Name: ")

        if equation == "info":
            print(info)

        ########  CHAPTER 27  ##########

        elif equation == "motion in a magnetic field":
            motionInMagneticField()


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



        ###########  OTHER  ############


##################################################
############ FUNCTION IMPLEMENTATIONS ############
##################################################

################################
########  CHAPTER 27  ##########
################################

def motionInMagneticField(): 
    r = input("R: ")
    m = input("m: ")
    v = input("v: ")
    q = input("q: ")
    b = input("b: ")

    if r == "?":
        print("R =", int(m)*int(v)/(abs(int(q))*int(b)))
    if m == "?":
        print("m =", (int(r)*abs(int(q))*int(b))/int(v))
    if v == "?":
        print("v =", (int(r)*abs(int(q))*int(b))/int(m))
    if b == "?":
        print("b =", int(m)*int(v)/(abs(int(q))*int(r)))
    if q == "?":
        print("abs(q) =", int(m)*int(v)/(int(r)*int(b)))

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

################################
###########  OTHER  ############
################################

if __name__== "__main__" :
    main()