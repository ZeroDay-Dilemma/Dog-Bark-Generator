from tkinter import *
import random
import pyperclip
import sys, os 
#def resource_path(relative_path):
#    if hasattr(sys, '_MEIPASS'):
#        return os.path.join(sys._MEIPASS, relative_path)
#    return os.path.join(os.path.abspath("."), relative_path)
#resource_path('DogHead.ico')
datafile = "DogHead.ico"
if not hasattr(sys, "frozen"):
    datafile = os.path.join(os.path.dirname(__file__), datafile)
else:
    datafile = os.path.join(sys.prefix, datafile)
"""
Noise list:
arf
bark
bite
chomp
ruff
snarl
woof


=---variations
GRRR     (# of Rs, beween 2-7)
HSSS     (# of Ss, beween 3-7)
HISS     (# of Ss, beween 2-7)
GROWL  (# of Rs 1 or 3-5)
HOWL     (either # of Os or Ls (?) -> 1 or 2)
arrgff   (# of Rs or Fs, 1-4) ARGFF


"""

print("yo")
#TODO:
#Upper/Lowercase should run at end. Default will be uppercase
#more varients -> chance for random letter to duplicate (I.E. bark -> barrk )
master = Tk()
checkboxList=[]
dictNoises={
    "1" : "GRR",
    "2" : "ARF",
    "3" : "HSS",
    "4" : "BARK",
    "5" : "HISS",
    "6" : "BITE",
    "7" : "GROWL",
    "8" : "CHOMP",
    "9" : "HOWL",
    "10" : "RUFF",
    "11" : "ARGFF",
    "12" : "SNARL",
    "13" : "WOOF"
}
'''
widgets are added here
'''
def bRand(num1,num2):
    return random.randint(num1,num2+1)


###############################
#####      GENERATORS     #####
###############################
def grrGen():
    rNum=bRand(2,7)
    output="G" + ("R"*rNum)
    return(output)
def hssGen():
    rNum=bRand(3,7)
    output="H" + ("S"*rNum)
    return(output)

def hissGen():
    rNum=bRand(2,5)
    output="HI" + ("S"*rNum)
    return(output)

def growlGen():
    tmp=bRand(1,4)
    if(tmp==1):
        rNum=bRand(1,5)
        output="G" + ("R"*rNum) + "OWL"
        return(output)
    if(tmp==2):
        rNum=bRand(1,4)
        output="GR" + ("O"*rNum)+"WL"
        return(output)
    if(tmp==3):
        rNum=bRand(1,3)
        output="GROW" + ("L"*rNum)
        return(output)
    else:
        return("GROWL")
def howlGen():

    if(bRand(1,2)==1):
        rNum=bRand(2,4)
        output="H" + ("O"*rNum)+"WL"
        return(output)
    else:
        return("HOWL")
def argffGen():
    tmp=bRand(1,4)
    if(tmp==1):
        rNum=bRand(2,4)
        output="A" + ("R"*rNum) + "GFF"
        return(output)
    if(tmp==2):
        rNum=bRand(2,4)
        output="AR"+("G"*rNum) + "FF"
        return(output)
    else:
        return("ARGFF")

###############################
#####        END OF       #####
#####      GENERATORS     #####
###############################

def genNoises():
    avalWords=[]
    finalString=""
    
   #print("male: %d,\nfemale: %d" % (GRR.get(), HSS.get()))
    for i in checkboxList:
        if(i.get()==1):
            avalWords.append(dictNoises[str(int(str(i)[6:])+1)])
    #errorchecking First
    if(len(avalWords)==0):
        return "Make sure to select at least one word!"
    try:
        placeHolder=int(numWordsInput.get())
    except ValueError:
        return "Please make sure you set a valid whole number greater than one (ERROR: NOT A NUMBER)"
    if (int(numWordsInput.get())<=0):
        return "Please make sure you set a valid whole number greater than oneERROR: SMALLER THAN 1)"
    #print(avalWords)
    #print(numWordsInput.get())
    for i in range(0, int(numWordsInput.get())):
        wordToUse=random.choice(avalWords)
        ##test, and if its a gen word use the gen
        if wordToUse=="GRR":
            finalString+=grrGen()
            
        elif wordToUse=="HSS":
            finalString+=hssGen()
            

        elif wordToUse=="HISS":
            finalString+=hissGen()
            
        elif wordToUse=="GROWL":
            finalString+=growlGen()

        elif wordToUse=="HOWL":
            finalString+=howlGen()
            
        elif wordToUse=="ARGFF":
            finalString+=argffGen()

        else:
            finalString+=wordToUse
        finalString+=" "
    #string generated. Now Run moreRandom() if needed, or else go straight to
    #uppercase/lowercase and output.
    if(moreRand.get()==1):
        #will modify the string with more variation.
        finalString=moreRandom(finalString)
        #moreRandom(finalString)
        
    if(isUppercase.get()==1):
    #    print(finalString.upper())
        return(finalString.upper())
    elif(isUppercase.get()==0):
    #    print(finalString.lower())
        return(finalString.lower())
    

def moreRandom(inputStr):
    #ONLY RUN AFTER FINAL STRING GENERATED
    #to add variation, it will look at each individual word in a string, and randomly
    #decide how many (if at all) letters it will duplicate.
    #I.E. WOOF -> WWOOOF or WOOF -> WOOF
    arrToMod=inputStr.split()
    for eleNum in range(0,len(arrToMod)):
        #print(arrToMod[eleNum])
        tmp=bRand(1,2)
        if (tmp==1): #do randomize
            arrToMod[eleNum]=doTheRandomModifing(arrToMod[eleNum])
    return(" ".join(arrToMod))
            
def doTheRandomModifing(eleToMod):
    lenOfEle=len(eleToMod)
    for numChar in range(0,lenOfEle):
        #for each letter in the string, have a chance to dupe it
        #b[:4] + b[4] + b[4:], will copy the string and dipe the 5th character
        if(bRand(1,6)==1):
            eleToMod=eleToMod[:numChar] + eleToMod[numChar] + eleToMod[numChar:]
            lenOfEle+=2 #continues looping thru string and wont dupe already modifed
    return(eleToMod)


def outputNoises(): #Try to delete popup
    #try:
    #    window.destroy()
    #except:
    #    print("ERROR, no window to delete. resuming")
    popup_window(genNoises())
def forceCheckAll():
    for i in checkboxList:
        i.set(1)
def forceUnCheckAll():
    for i in checkboxList:
        i.set(0)
#def testing():
#    for i in checkboxList:
#        if(i.get()==1):
#            print(dictNoises[str(int(str(i)[6:])+1)])

def quitStuff():
    master.destroy()
    sys.exit("Program Closed")
    
isLightMode=True
def switchColorMode():
    global isLightMode
    if(isLightMode==True): #then switch to darkmode Stuff
        isLightMode=False
        master.tk_setPalette(background='#36393F', foreground='#dcddde',
               activeBackground='#36393F', activeForeground='#dcddde')
        #master['bg']='#2c2f33'
        #FFFFFF
        print("Do Dark Mode")
    elif(isLightMode==False): #then switch to lightmode Stuff
        isLightMode=True
        master.tk_setPalette(background='#F0F0F0', foreground='#000000',
               ativeBackground='#F0F0F0', activeForeground='#000000')
        #master['bg']='#F0F0F0'
        print("Do Light Mode")
    else:
        print("ERROR")
        return 0
def reroll(window):
        window.destroy()
        outputNoises()
def popup_window(output):
    def doReroll():
        T.delete("1.0","end")
        T.insert(END, genNoises())
    window = Toplevel()
                                    
                                    
    T = Text(window, height = 5, width = 52)
    l = Label(window, text = "The Noises:")
    l.config(font =("Courier", 14))
                                    
    l.pack()
    T.pack()
    T.insert(END, output)
    button_close = Button(window, text="Copy To Clipboard", command=pyperclip.copy(output))
    button_close.pack(fill='x')
    
    button_close = Button(window, text="Reroll", command=doReroll) #command = lambda: reroll(window))
    button_close.pack(fill='x')
    
    button_close = Button(window, text="Change Settings", command=window.destroy)
    button_close.pack(fill='x')

Label(master, text="Will's Dog Noise Gen").grid(row=0, sticky=W)
master.title("Will's Dog Noise Gen")
master.iconbitmap(default=datafile)
Label(master, text="# of Words").grid(row=1, sticky=W)
numWordsInput = Entry(master)
numWordsInput.grid(row=1, column=1)
numWordsInput.insert(END, '10')

Label(master, text="Noise Toggles:").grid(row=2, sticky=W)

"""
GRR
ARF
HSS
BARK
HISS
BITE
GROWL
CHOMP
HOWL
RUFF
ARGFF
SNARL
WOOF
"""
master.geometry("250x380")

#ROW 1--------------------------------------------------------
GRR = IntVar()
checkboxList.append(GRR)
noise1 = Checkbutton(master, text="GRR", variable=GRR).grid(row=3, sticky=W)



ARF = IntVar()
checkboxList.append(ARF)
noise2 = Checkbutton(master, text="ARF", variable=ARF).grid(row=3,column=1, sticky=W)
#ROW 2--------------------------------------------------------
HSS = IntVar()
checkboxList.append(HSS)
noise3 = Checkbutton(master, text="HSS", variable=HSS).grid(row=4, sticky=W)


BARK = IntVar()
checkboxList.append(BARK)
noise4 = Checkbutton(master, text="BARK", variable=BARK).grid(row=4,column=1, sticky=W)
#ROW 3--------------------------------------------------------
HISS = IntVar()
checkboxList.append(HISS)
noise5 = Checkbutton(master, text="HISS", variable=HISS).grid(row=5, sticky=W)


BITE = IntVar()
checkboxList.append(BITE)
noise6 = Checkbutton(master, text="BITE", variable=BITE).grid(row=5,column=1, sticky=W)
#ROW 4--------------------------------------------------------
GROWL = IntVar()
checkboxList.append(GROWL)
noise7 = Checkbutton(master, text="GRR", variable=GROWL).grid(row=6, sticky=W)


CHOMP = IntVar()
checkboxList.append(CHOMP)
noise8 = Checkbutton(master, text="CHOMP", variable=CHOMP).grid(row=6,column=1, sticky=W)
#ROW 5--------------------------------------------------------
HOWL = IntVar()
checkboxList.append(HOWL)
noise9 = Checkbutton(master, text="HOWL", variable=HOWL).grid(row=7, sticky=W)


RUFF = IntVar()
checkboxList.append(RUFF)
noise10 = Checkbutton(master, text="RUFF", variable=RUFF).grid(row=7,column=1, sticky=W)
#ROW 6--------------------------------------------------------
ARGFF = IntVar()
checkboxList.append(ARGFF)
noise11 = Checkbutton(master, text="ARGFF", variable=ARGFF).grid(row=8, sticky=W)


SNARL = IntVar()
checkboxList.append(SNARL)
noise12 = Checkbutton(master, text="SNARL", variable=SNARL).grid(row=8,column=1, sticky=W)
#ROW 7
WOOF = IntVar()
checkboxList.append(WOOF)
noise13 = Checkbutton(master, text="WOOF", variable=WOOF).grid(row=9, sticky=W)


Button(master, text='check all', command=forceCheckAll).grid(row=12, sticky="w")
Button(master, text='uncheck all', command=forceUnCheckAll).grid(row=12, column=1,sticky="w")


Button(master, text='Generate', command=outputNoises).grid(row=13, sticky=W)
#Label(master, text='  Uppercase:', command=outputNoises).grid(row=13, colum=1, padx=3, sticky=W)
isUppercase = IntVar()
Checkbutton(master, text="Uppercase?", variable=isUppercase).grid(row=13, column=1, sticky="W")
isUppercase.set(1)

Button(master, text='Toggle Dark Mode', command=switchColorMode).grid(row=14, column=0,sticky="W")

moreRand = IntVar()
Checkbutton(master, text="More Random", variable=moreRand).grid(row=14, column=1, sticky="W")


Label(master, text='').grid(row=15, sticky=W, pady=4)

Button(master, text='Quit', command=quitStuff).grid(row=16, sticky=W, pady=4)#quit).grid(row=16, sticky=W, pady=4)


#Button(master, text='Testing', command=testing).grid(row=17, sticky=W, pady=4)

mainloop()



