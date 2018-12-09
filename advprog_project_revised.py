<<<<<<< HEAD
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
import os

#Co-scripts
import kibord
import payls
import about as tungkol

window = Tk()
#Window params
window.geometry("300x160")
window.title("高度なプログラミングプロジェクト")
window.resizable(width=False, height=False)

#Commands
class Commands:
    def showKeyboard():
        kibord.drawBoard()

    def showIO():
        payls.drawBoard()

    def showAbout():
        tungkol.drawBoard()

#Buttons
keyboard = Button(window, text="Keyboard (キーボード)\nTkinter Demo", command=Commands.showKeyboard).place(x=0, y=5, width=300, height=50)
files = Button(window, text="Files (ファイル)\nPython Files I/O with Exception Handling", command=Commands.showIO).place(x=0, y=55, width=300, height=50)
about = Button(window, text="Team Info (チーム情報)", command=Commands.showAbout).place(x=0, y=105, width=300, height=50)

window.mainloop()
=======
import tkinter
>>>>>>> bef6fc463ec47eaee473466f47038e60ae19cc2e
