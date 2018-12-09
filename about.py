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
    window = Tk()
    window.geometry("300x220")
    window.title("チーム情報")
    window.resizable(width=False, height=False)

    #Labels
    header = Label(window, text="Group 1", font=("Arial", 10)).place(x=2, y=2)
    subHeader = Label(window, text="Team Loli", font=("Arial", 20)).place(x=2, y=20)
    members = Label(window, text="""
Vien Villasin (Lead)
Aaron Estores
Keysha Pareja
Angelica Maghirang
Mark Nolledo
""", font=("Arial", 10), justify=LEFT).place(x=2, y=50)
    creds = Label(window, text="""
Advanced Programming Finals Project
© 2018 Team Loli
Thank you Ms. Gerios for the awesome semester!
""", font=("Arial", 9), justify=LEFT).place(x=2, y=150)

    window.mainloop()
