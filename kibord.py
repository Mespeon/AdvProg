##Advance Programming Finals Project
##Group 1 - Team Loli
##Created by:
##    Vien Villasin (Lead)
##    Aaron Estores
##    Keysha Pareja
##    Angelica Maghirang
##    Mark Nolledo
##
##Submitted for:
##    Ms. Gerios
##
##Code written using IDLE 3.6.4 for Python 3.6.4
##© 2018 Team Loli

from tkinter import *

def drawBoard():
    board = Tk()
    #Board params
    board.geometry("840x240")
    board.title("Le Magical Keyboard")
    board.resizable(width=False, height=False)

    #Row 1
    esc = Button(board, text="Esc", bg="#AAA").place(x=0, y=0, width=40, height=40)
    f1 = Button(board, text="F1", bg="#9CE2FF").place(x=40, y=0, width=40, height=40)
    f2 = Button(board, text="F2", bg="#9CE2FF").place(x=80, y=0, width=40, height=40)
    f3 = Button(board, text="F3", bg="#9CE2FF").place(x=120, y=0, width=40, height=40)
    f4 = Button(board, text="F4", bg="#9CE2FF").place(x=160, y=0, width=40, height=40)
    f5 = Button(board, text="F5", bg="#9CE2FF").place(x=200, y=0, width=40, height=40)
    f6 = Button(board, text="F6", bg="#9CE2FF").place(x=240, y=0, width=40, height=40)
    f7 = Button(board, text="F7", bg="#9CE2FF").place(x=280, y=0, width=40, height=40)
    f8 = Button(board, text="F8", bg="#9CE2FF").place(x=320, y=0, width=40, height=40)
    f9 = Button(board, text="F9", bg="#9CE2FF").place(x=360, y=0, width=40, height=40)
    f10 = Button(board, text="F10", bg="#9CE2FF").place(x=400, y=0, width=40, height=40)
    f11 = Button(board, text="F11\nNumLk", bg="#9CE2FF").place(x=440, y=0, width=40, height=40)
    f12 = Button(board, text="F12\nScrLk", bg="#9CE2FF").place(x=480, y=0, width=40, height=40)
    prtScr = Button(board, text="PrtSc", bg="#AAA").place(x=520, y=0, width=40, height=40)
    pause = Button(board, text="Pause\nBreak", bg="#AAA").place(x=560, y=0, width=40, height=40)
    ins = Button(board, text="Ins", bg="#AAA").place(x=600, y=0, width=40, height=40)
    delete = Button(board, text="Del", bg="#AAA").place(x=640, y=0, width=40, height=40)

    #Row 2
    karet = Button(board, text="~\n`", bg="#B3ABFF").place(x=0, y=40, width=40, height=40)
    num01 = Button(board, text="!\n1", bg="#B3ABFF").place(x=40, y=40, width=40, height=40)
    num01 = Button(board, text="@\n2", bg="#B3ABFF").place(x=80, y=40, width=40, height=40)
    num01 = Button(board, text="#\n3", bg="#B3ABFF").place(x=120, y=40, width=40, height=40)
    num01 = Button(board, text="$\n4", bg="#B3ABFF").place(x=160, y=40, width=40, height=40)
    num01 = Button(board, text="%\n5", bg="#B3ABFF").place(x=200, y=40, width=40, height=40)
    num01 = Button(board, text="^\n6", bg="#B3ABFF").place(x=240, y=40, width=40, height=40)
    num01 = Button(board, text="&\n7", bg="#B3ABFF").place(x=280, y=40, width=40, height=40)
    num01 = Button(board, text="*\n8", bg="#B3ABFF").place(x=320, y=40, width=40, height=40)
    num01 = Button(board, text="(\n9", bg="#B3ABFF").place(x=360, y=40, width=40, height=40)
    num01 = Button(board, text=")\n0", bg="#B3ABFF").place(x=400, y=40, width=40, height=40)
    minun = Button(board, text="_\n-", bg="#B3ABFF").place(x=440, y=40, width=40, height=40)
    plusle = Button(board, text="+\n=", bg="#B3ABFF").place(x=480, y=40, width=40, height=40)
    backspace = Button(board, text="Backspace", bg="#AAA").place(x=520, y=40, width=120, height=40)
    home = Button(board, text="Home", bg="#AAA").place(x=640, y=40, width=40, height=40)

    #Row 3
    tab = Button(board, text="Tab", bg="#AAA").place(x=0, y=80, width=40, height=40)
    q = Button(board, text="Q", bg="#FFF09C").place(x=40, y=80, width=40, height=40)
    w = Button(board, text="W", bg="#FFF09C").place(x=80, y=80, width=40, height=40)
    e = Button(board, text="E", bg="#FFF09C").place(x=120, y=80, width=40, height=40)
    r = Button(board, text="R", bg="#FFF09C").place(x=160, y=80, width=40, height=40)
    t = Button(board, text="T", bg="#FFF09C").place(x=200, y=80, width=40, height=40)
    y = Button(board, text="Y", bg="#FFF09C").place(x=240, y=80, width=40, height=40)
    u = Button(board, text="U", bg="#FFF09C").place(x=280, y=80, width=40, height=40)
    i = Button(board, text="I", bg="#FFF09C").place(x=320, y=80, width=40, height=40)
    o = Button(board, text="O", bg="#FFF09C").place(x=360, y=80, width=40, height=40)
    p = Button(board, text="P", bg="#FFF09C").place(x=400, y=80, width=40, height=40)
    openBracket = Button(board, text="{\n[", bg="#B3ABFF").place(x=440, y=80, width=40, height=40)
    closeBracket = Button(board, text="}\n]", bg="#B3ABFF").place(x=480, y=80, width=40, height=40)
    backSlash = Button(board, text="|\n\\", bg="#B3ABFF").place(x=520, y=80, width=120, height=40)
    pageUp = Button(board, text="Pg Up", bg="#AAA").place(x=640, y=80, width=40, height=40)

    #Row 4
    capsLock = Button(board, text="Caps\nLk", bg="#AAA").place(x=0, y=120, width=40, height=40)
    a = Button(board, text="A", bg="#FFF09C").place(x=40, y=120, width=40, height=40)
    s = Button(board, text="S", bg="#FFF09C").place(x=80, y=120, width=40, height=40)
    d = Button(board, text="D", bg="#FFF09C").place(x=120, y=120, width=40, height=40)
    f = Button(board, text="F", bg="#FFF09C").place(x=160, y=120, width=40, height=40)
    g = Button(board, text="G", bg="#FFF09C").place(x=200, y=120, width=40, height=40)
    h = Button(board, text="H", bg="#FFF09C").place(x=240, y=120, width=40, height=40)
    j = Button(board, text="J", bg="#FFF09C").place(x=280, y=120, width=40, height=40)
    k = Button(board, text="K", bg="#FFF09C").place(x=320, y=120, width=40, height=40)
    l = Button(board, text="L", bg="#FFF09C").place(x=360, y=120, width=40, height=40)
    colon = Button(board, text=":\n;", bg="#B3ABFF").place(x=400, y=120, width=40, height=40)
    quote = Button(board, text="\"\n'", bg="#B3ABFF").place(x=440, y=120, width=40, height=40)
    enterTheDragon = Button(board, text="Enter", bg="#AAA").place(x=480, y=120, width=160, height=40)
    pageDown = Button(board, text="Pg Dn", bg="#AAA").place(x=640, y=120, width=40, height=40)

    #Row 5
    shiftL = Button(board, text="Shift", bg="#AAA").place(x=0, y=160, width=120, height=40)
    z = Button(board, text="Z", bg="#FFF09C").place(x=120, y=160, width=40, height=40)
    x = Button(board, text="X", bg="#FFF09C").place(x=160, y=160, width=40, height=40)
    c = Button(board, text="C", bg="#FFF09C").place(x=200, y=160, width=40, height=40)
    v = Button(board, text="V", bg="#FFF09C").place(x=240, y=160, width=40, height=40)
    b = Button(board, text="B", bg="#FFF09C").place(x=280, y=160, width=40, height=40)
    n = Button(board, text="N", bg="#FFF09C").place(x=320, y=160, width=40, height=40)
    m = Button(board, text="M", bg="#FFF09C").place(x=360, y=160, width=40, height=40)
    comma = Button(board, text="<\n,", bg="#B3ABFF").place(x=400, y=160, width=40, height=40)
    dot = Button(board, text=">\n.", bg="#B3ABFF").place(x=440, y=160, width=40, height=40)
    forwardSlash = Button(board, text="?\n/", bg="#B3ABFF").place(x=480, y=160, width=40, height=40)
    shiftR = Button(board, text="Shift", bg="#AAA").place(x=520, y=160, width=120, height=40)
    endMeNow = Button(board, text="End", bg="#AAA").place(x=640, y=160, width=40, height=40)

    #Row 6
    leftCtrl = Button(board, text="Ctrl", bg="#AAA").place(x=0, y=200, width=40, height=40)
    fN = Button(board, text="Fn", bg="#AAA").place(x=40, y=200, width=40, height=40)
    winKey = Button(board, text="WND", bg="#33B5E5").place(x=80, y=200, width=40, height=40)
    leftAlt = Button(board, text="Alt", bg="#AAA").place(x=120, y=200, width=40, height=40)
    spaceBar = Button(board, text="").place(x=160, y=200, width=280, height=40)
    rightAlt = Button(board, text="Alt", bg="#AAA").place(x=440, y=200, width=40, height=40)
    context = Button(board, text="Cntx", bg="#AAA").place(x=480, y=200, width=40, height=40)
    rightCtrl = Button(board, text="Ctrl", bg="#AAA").place(x=520, y=200, width=40, height=40)
    left = Button(board, text="left", bg="#F7AEF7").place(x=560, y=200, width=40, height=40)
    up = Button(board, text="up", bg="#F7AEF7").place(x=600, y=200, width=40, height=20)
    down = Button(board, text="down", bg="#F7AEF7").place(x=600, y=220, width=40, height=20)
    right = Button(board, text="right", bg="#F7AEF7").place(x=640, y=200, width=40, height=40)

    #NumPad
    npDivide = Button(board, text="/", bg="#AAA").place(x=680, y=40, width=40, height=40)
    npMultiply = Button(board, text="x", bg="#AAA").place(x=720, y=40, width=40, height=40)
    npSubtract = Button(board, text="-", bg="#AAA").place(x=760, y=40, width=80, height=40)
    npAdd = Button(board, text="+", bg="#AAA").place(x=800, y=80, width=40, height=120)
    np07 = Button(board, text="7", bg="#AAA").place(x=680, y=80, width=40, height=40)
    np08 = Button(board, text="8", bg="#AAA").place(x=720, y=80, width=40, height=40)
    np09 = Button(board, text="9", bg="#AAA").place(x=760, y=80, width=40, height=40)
    np04 = Button(board, text="4", bg="#AAA").place(x=680, y=120, width=40, height=40)
    np05 = Button(board, text="5", bg="#AAA").place(x=720, y=120, width=40, height=40)
    np06 = Button(board, text="6", bg="#AAA").place(x=760, y=120, width=40, height=40)
    np01 = Button(board, text="1", bg="#AAA").place(x=680, y=160, width=40, height=40)
    np02 = Button(board, text="2", bg="#AAA").place(x=720, y=160, width=40, height=40)
    np03 = Button(board, text="3", bg="#AAA").place(x=760, y=160, width=40, height=40)
    np00 = Button(board, text="0", bg="#AAA").place(x=680, y=200, width=160, height=40)

    board.mainloop()
