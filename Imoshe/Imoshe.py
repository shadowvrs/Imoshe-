#To run in a terminal - python3 Imoshe.py
from tkinter import *
import tkinter as tk

#Variables
root = tk.Tk()

"""
saveFile = open("SettingsSave.txt", "r")

GetSettingsFile = saveFile.read()

saveFile.close
"""

why = PhotoImage(file = "why.png")
whyPut = Label(root, image = why)

inputsColorT = "black"
buttonBackround = "white"

fileName = "SettingsSave.txt"

#Tk variables
WhichTheme = StringVar()
WhichTheme.set("Gray")

#Global variables
global backr
backr = "#696868"

global textColorChose
textColorChose = "white"

global fontChange
fontChange = "Times new roman"

global fontWhich
fontWhich = StringVar()
fontWhich.set(fontChange)

global getFont
getFont = ""

global saveTranslation
saveTranslation = []

#Secrets
global kill
kill = False

global code
code = 0

"""
Index translation for each word

Q 0-1, W 2-3, E 4-5, R 6-7, T 8-9, Y 10-11, U 12-13, I 14-15, O 16-17, P 18-19, A 20-21, S 22-23, | D 24-25, F 26-27,
G 28-29, H 30-31, J 32-33, K 34-35, L 36-37, Z 38-39, X 40-41, C 42-43, V 44-45, B 46-47, N 48-49, M 50-51, | " " 52, 
"/" 53, "?" 54, "." 55, "," 56, ">" 57, "<" 58, "'" 59, ":" 60, ";" 61, "|" 62, "]" 63, "[" 64, "{" 65, "}" 66, "!" 67,
"@" 68, "#" 69, "$" 70, "%" 71, "^" 72, "&" 73, "*" 74, "(" 75, ")" 76, "_" 77, "`" 78, | - 79, + 80, = 81, 0 82, 1 83, 2 84
3 85, 4 86, 5 87, 6 88, 7 89, 8 90, 9 91 
"""

#Lists
allImosheWords = [
    "IfIT", "ifit", "RiIT", "riit", "OpIT", "opit", "AkIT", "akit", "ODIT", "odit", "DFDT", "dfdt","LFDT", "lfdt",
    "KODT", "kodt", "ANWS", "anws", "PTWS", "ptws", "MKWS", "mkws", "HJWS", "hjws", "RY^8", "ry^8", "LY(*", "ly(*", 
    "PC{|", "pc{|", "EC$R", "ec$r", "LC0O", "lc0o", "UCU%", "ucu%", "KQ>L", "kq>l", "AQ<K", "aq<k", "BQ#F", "bq#f", 
    "ZQ'L", "zq'l", "UM-+", "um-+", "TM!Y", "tm!y", "RM;K", "rm;k", "GM=3", "gm=3", "+QTY", "/WRE", "?EFG", ".RHJ", 
    ",TAQ", ">YOI", "<UJK", "'IQA", ":OMB", ";POA", "|ADE", "]SVB", "[DZX", "{FXB", "}GRT", "!XVM", "@OPJ", "#LOK",
    "$SUD", "%MAT", "^UPT", "&GHR", "*STA", "(FNB", ")DEQ", "_WSD", "`ALM", "jn.|", "bg!~", "kl(8", "TyU9", "GiP8",
    "Hg7P", "Gt6m", "A5jo", "N4qw", "$kol", "#gme", "2lkg", "1jnb"]

allEnglishWords = [
    "Q", "q", "W", "w", "E", "e", "R", "r", "T", "t", "Y", "y", "U", "u", "I", "i", "O", "o", "P", "p", "A", "a",
    "S", "s", "D", "d", "F", "f", "G", "g", "H", "h", "J", "j", "K", "k", "L", "l", "Z", "z", "X", "x", "C", "c",
    "V", "v", "B", "b", "N", "n", "M", "m", " ", "/", "?", ".", ",", ">", "<", "'", ":", ";", "|", "]", "[", "{", 
    "}", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "`", "-", "+", "=", "0", "1", "2", "3", "4", "5",
    "6", "7", "8", "9"]

#Setting up stuff
root.configure(bg = backr)
root.title("Imoshe")
root.geometry("860x560")

#Def functions
def newImosheChange(rep):
    global changeResponse
    checkImosheToText = 0
    #Loop checks for each letter in Imoshe
    for word in allImosheWords[:]:
        if rep == allImosheWords[checkImosheToText]:
            changeResponse = allEnglishWords[checkImosheToText]
        else:
            checkImosheToText += 1

def newImosheCon(phrase):
    checkTextToImoshe = 0
    #Loop checks each letter in english
    for word in allEnglishWords[:]:
        if phrase == allEnglishWords[checkTextToImoshe]:
            translation = allImosheWords[checkTextToImoshe]
            return translation
        else:
            checkTextToImoshe += 1

def forgetPlace(chose):
    #This is for forgeting the place of the UI
    #Their are tow diffrent versions, one for the meun and the other for everything else
    if chose == 0:
        ImosheConText.place_forget()
        back.place_forget()
        frameImosheCon.place_forget()
        save.place_forget()
        theme.place_forget()
        settingsText.place_forget()
        settingsTheme.place_forget()
        fontText.place_forget()
        fonts.place_forget()
        backwardsText.place_forget()
        frameBackwardsText.place_forget()
        
    elif chose == 1:
        MT.place_forget()
        newImoshe.place_forget()
        settingsb.place_forget()
        exitButton.place_forget()
        backwardsTextB.place_forget()

def Menu():
    forgetPlace(0)

    MT.place(relx = 0.5, rely = 0, anchor = "n")

    newImoshe.place(relx = 0.5, rely = 0.14, anchor = "center")
    backwardsTextB.place(relx = 0.5, rely = 0.26, anchor = "center")
    settingsb.place(relx = 0.5, rely = 0.38, anchor = "center")
    exitButton.place(relx = 0.5, rely = 0.5, anchor = "center")

def ImosheUI():
    global code

    code = 0

    forgetPlace(1)

    #Placing new UI
    ImosheConText.place(relx = 0.5, rely = 0, anchor = "n")
    back.place(relx = 0.08, rely = 0.02, anchor = "n")
    frameImosheCon.place(relx = 0.5, rely = 0.5, anchor = "center")

def resultNewImosheTrans():
    response.delete(0, END)
    global changeResponse
    global fullWord
    global numLook
    global Get

    Get = Input.get()
    num = 0
    numLook = 2

    #The first for loop is to get num to the max letters
    for letter in Get:
        num += 1

    #The fist loop is one off so minuse one
    num -= 1

    for letter in Get:
        Get = Input.get()
        try:
            response.insert(0, newImosheCon(Get[num]))
        except:
            response.insert(0, "THEIR IS NO TRANSLATION FOUND FOR THAT LETTER")

        num -= 1

    #This is setting fullWord = to the letters you want to look for
    fullWord = Get[:numLook]

    changeLook()

def changeLook():
    global numLook
    global fullWord
    global Get
    global saveTranslation
    global keyword

    checkWord = 0
    numLook = 0
    multipleCheck4 = 4
    otherCheck4 = 4
    addNumbre = 12

    #range checks for everything in between two numbers, Ex: range(3, 6) will give 3, 4 and 5
    #When you print out keyword it gives you: range(0, 53)
    keyword = range(len(allImosheWords[:]))

    while True:
        #This is to check if the looking variable is higher than the fullword
        if numLook >= len(Get[:]):
            saveTranslation = []
            break
        if fullWord != allImosheWords[checkWord] and numLook <= len(Get[:]):
            numLook += 1

            #This has to be called so that numLook will b
            if numLook == multipleCheck4:
                fullWord = Get[:numLook]

                #Call in the change function
                translateImoshe(False)

                if multipleCheck4 > otherCheck4:
                    fullWord = Get[otherCheck4:numLook]
                    translateImoshe(True)

                    if numLook >= addNumbre:
                        otherCheck4 += 4
                        addNumbre += 4
                        fullWord = Get[otherCheck4:numLook]
                        translateImoshe(True)
                            
                #change what it's checking 
                multipleCheck4 = multipleCheck4 + 4

        if checkWord >= 91:
            checkWord = 0
        checkWord += 1

def translateImoshe(wasMultiple):
    global fullWord
    global changeResponse
    global Get
    global saveTranslation
    global numLook
    global keyword

    newImosheChange(fullWord)

    ListEnglish = range(len(allEnglishWords[:]))

    numWhich = 0
    firstRun = True

    #len gets the number of letters in a strings
    for word in keyword:
        if numWhich == len(allImosheWords[:]):
            break
        if fullWord == allImosheWords[numWhich]:

            response.delete(0, END)
            response.insert(0, changeResponse)

            #Get the response
            getRe = response.get()

            #Put the response in a list
            saveTranslation.append(getRe)
            
            loopTime = len(saveTranslation[:]) - 1

            if wasMultiple == True:
                response.delete(0, END)
                while loopTime != -1:
                    response.insert(0, saveTranslation[loopTime])
                    loopTime -= 1

            break
        numWhich += 1

def Set():
    global textColorChose
    global fontChange
    global fontWhich
    global getFont
    global backr
    global kill

    ThemeSave = WhichTheme.get()
    getFont = fontWhich.get()

    if ThemeSave == "Gray":
        backr = "#696868"
        textColorChose = "white"
        whyPut.place_forget()

    elif ThemeSave == "Dark":
        backr = "#3F3D3D"
        textColorChose = "white"
        whyPut.place_forget()

    elif ThemeSave == "Light":
        backr = "#CFCFCF"
        textColorChose = "black"
        whyPut.place_forget()

    elif ThemeSave == "WHY":
        whyPut.place(x=0, y=0, relwidth=1, relheight=1)

    if getFont == "Secret ;D":
        fontChange = "Comic Sans MS"
        fonts.place_forget()
        fontText.place_forget()

        Input.configure(font = (fontChange, 12))
        kill = True
    elif getFont == "Times New Roman":
        fontChange = "Times New Roman"
        Input.configure(font = (fontChange, 13))
    elif getFont == "Arial":
        fontChange = "Arial"
        Input.configure(font = (fontChange, 13))
    elif getFont == "DeJaVu sans mono":
        fontChange = "DeJaVu sans mono"
        Input.configure(font = (fontChange, 13))
    elif getFont == "Calibri":
        fontChange = "Calibri"
        Input.configure(font = (fontChange, 13))
    elif getFont == "Georgia":
        fontChange = "Georgia"
        Input.configure(font = (fontChange, 13))
    elif getFont == "VCR OSD MONO":
        fontChange = "VCR OSD MONO"
        Input.configure(font = (fontChange, 13))
    elif getFont == "Fascinate":
        fontChange = "Fascinate"
        Input.configure(font = (fontChange, 13))

    #Root
    root.configure(bg = backr)

    #Frames
    frameImosheCon.configure(bg = backr, fg = textColorChose)
    frameSetting.configure(bg = backr)
    frameBackwardsText.configure(bg = backr)

    #Title screen
    MT.configure(bg = backr, fg = textColorChose, font = (fontChange, 25))

    #Inputs
    #response.configure(bg = backr, fg = textColorChose, font = (fontChange, 13))

    #Text
    settingsText.configure(bg = backr, fg = textColorChose, font = (fontChange, 22))
    ImosheConText.configure(bg = backr, font = (fontChange,  20))
    fontText.configure(bg = backr, fg = textColorChose, font = (fontChange, 15))
    settingsTheme.configure(bg = backr, fg = textColorChose, font = (fontChange, 15))
    backwardsText.configure(bg = backr, fg = textColorChose, font = (fontChange, 22))

    #Buttons
    save.configure(font = (fontChange, 15))
    back.configure(font = (fontChange, 15))
    settingsb.configure(font = (fontChange, 15))
    newImoshe.configure(font = (fontChange, 15))
    backwardsTextB.configure(font = (fontChange, 15))
    exitButton.configure(font = (fontChange, 15))
    convert.configure(font = (fontChange, 15))
    convertBTButton.configure(font = (fontChange, 15))

    #Options
    theme.configure(font = (fontChange, 15))
    fonts.configure(font = (fontChange, 15))


    #opening the save settings file
    #Thank you for helping me solve this :D https://stackoverflow.com/questions/21005921/deleting-a-specific-word-from-a-file-in-python

    """
    saveFile = open(fileName, "r")

    save = saveFile.readlines()

    saveFile.close()
    """

def settings():
    global kill
    global code
    global theme

    code += 1

    if code >= 5:
        theme = OptionMenu(root, WhichTheme, "Gray", "Dark", "Light", "WHY")
        theme.configure(bg = buttonBackround, font = (fontChange, 15))

    forgetPlace(1)

    #placing things
    frameSetting.place(relx = 0.5, rely = 0.5, anchor = "center")

    back.place(relx = 0.08, rely = 0.02, anchor = "n")
    theme.place(relx = 0.17, rely = 0.24, anchor = "w")
    save.place(relx = 0.92, rely = 0.02, anchor = "n")
    settingsText.place(relx = 0.5, rely = 0.03, anchor = "center")
    settingsTheme.place(relx = 0.151, rely = 0.15, anchor = "w")
    if kill == False:
        fontText.place(relx = 0.153, rely = 0.35, anchor = "w")
        fonts.place(relx = 0.17, rely = 0.435, anchor = "w")

def convertBackwardsText():
    outcome.delete(0, END)
    tran = entre.get()
    num = 0

    for letter in tran:
        outcome.insert(0, tran[num])
        num += 1

def backwardsTextPut():
    global code

    code = 0

    forgetPlace(1)

    back.place(relx = 0.08, rely = 0.02, anchor = "n")
    backwardsText.place(relx = 0.5, rely = 0.05, anchor = "center")
    frameBackwardsText.place(relx = 0.5, rely = 0.5, anchor = "center")

#Setting UI

#Setting Frames
frameImosheCon = LabelFrame(root, padx = 90, pady = 140, bg = backr)
frameSetting = LabelFrame(root, padx = 90, pady = 140, bg = backr)
frameBackwardsText = LabelFrame(root, padx = 90, pady = 140, bg = backr)

#Buttons
newImoshe = Button(root, text = "Imoshe Translate", font = (fontChange, 15), bg = buttonBackround, padx = 25, command = ImosheUI)
backwardsTextB = Button(root, text = "Backwards Text", font = (fontChange, 15), bg = buttonBackround, padx = 20, command = backwardsTextPut)
settingsb = Button(root, text = "Settings", font = (fontChange, 15), bg = buttonBackround, padx = 40, command = settings)
exitButton = Button(root, text = "Exit", fon = (fontChange, 15), bg = buttonBackround, padx = 40, command = root.quit)
save = Button(root, text = "Save", font = (fontChange, 15), bg = buttonBackround, padx = 30, pady = 10, command = Set)
back = Button(root, text = "Back", font = (fontChange, 15), bg = buttonBackround, padx = 30, pady = 10, command = Menu)
convert = Button(frameImosheCon, text = "Convert", font = (fontChange, 15), bg = buttonBackround, padx = 25, pady = 8, command = resultNewImosheTrans)
convertBTButton = Button(frameBackwardsText, text = "Convert", font = (fontChange, 15), bg = buttonBackround, padx = 25, pady = 8, command = lambda: convertBackwardsText())

#Options
global theme
theme = OptionMenu(root, WhichTheme, "Gray", "Dark", "Light")
fonts = OptionMenu(root, fontWhich, "Arial", "Calibri", "DeJaVu sans mono", "Fascinate", "Georgia", "Times New Roman", "VCR OSD MONO", "Secret ;D")

#Confiure options
theme.configure(bg = buttonBackround, font = (fontChange, 15))
fonts.configure(bg = buttonBackround, font = (fontChange, 15))

#Inputs
Input = Entry(frameImosheCon, fg = inputsColorT, width = 71, font = (fontChange, 13))
response = Entry(frameImosheCon, fg = inputsColorT, width = 71, font = (fontChange, 13))
entre = Entry(frameBackwardsText, fg = inputsColorT, width = 71, font = (fontChange, 13))
outcome = Entry(frameBackwardsText, fg = inputsColorT, width = 71, font = (fontChange, 13))

#Text
MT = Label(root, text = "--------------Welcome to Imoshe--------------", bg = backr, fg = textColorChose, font = (fontChange, 25))
ImosheConText = Label(root, text = "--------------Imoshe--------------", bg = backr, fg = textColorChose, font = (fontChange, 22))
settingsText = Label(root, text = "--------------Settings--------------", bg = backr, fg = textColorChose, font = (fontChange, 22))
settingsTheme = Label(root, text = "Themes:", bg = backr, fg = textColorChose, font = (fontChange, 15))
fontText = Label(root, text = "Fonts:", bg = backr, fg = textColorChose, font = (fontChange, 15))
backwardsText = Label(root, text = "--------------drawkcaB Text--------------", bg = backr, fg = textColorChose, font = (fontChange, 22))

#Placing the UI that goes in the frames
response.grid(column = 0, row = 2, sticky = "n", pady = 10)
Input.grid(column = 0, row = 0, sticky = "n", pady = 10)
convert.grid(column = 0, row = 1, sticky = "n")

entre.grid(column = 0, row = 0, sticky = "n", pady = 10)
outcome.grid(column = 0, row = 2, sticky = "n", pady = 10)
convertBTButton.grid(column = 0, row = 1, sticky = "n")

#Putting the meun on screen
Menu()

root.mainloop()