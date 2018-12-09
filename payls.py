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
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import os

def drawBoard():
    window = Tk()
    #Geometry
    window.geometry("300x500")
    window.title("Files (ファイル)")
    window.resizable(width=False, height=False)

    #Functions
    def getFile():
        file = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("Text files", "*.txt"),("All Files","*.*")))
        if file != '':
            fileToOpen = open(file, "r")
            print("\nOpened file " + file)
            readContents = fileToOpen.read()
            print("Reading file:\n" + readContents)
            fileToOpen.close()
            return file
        else:
            print("Dialog cancelled.")
            return 0
    
    def writeToFile():
        text = textBox.get()
        print("Writing to file: " + text)
        if text == '':
            raise Exception(messagebox.showerror("Error", "Write text should not be blank."))
        
        try:
            file = open(getFile(), "w+")
            file.write(text + '\n')
            messagebox.showinfo("Write to File", "Write completed successfully.")
            file.close()
        except Exception as ex:
            print(ex)

    def appendToFile():
        text = textBox.get()
        print("Appending to file: " + text)
        if text == '':
            raise Exception(messagebox.showerror("Error", "Append text should not be blank."))
        
        try:    
            file = open(getFile(), "a+")
            file.write(text + '\n')
            messagebox.showinfo("Append to File", "Append completed successfully.")
            file.close()
        except Exception as ex:
            print(ex)

    def renameFile():
        file = open(getFile())
        currentFileName = file.name
        if currentFileName == 0:
            raise Exception("No file returned. Get file returned {}".format(currentFileName))
        
        newFileName = fileRename.get()
        print("Renaming file from: " + currentFileName)
        print("Renaming to: " + newFileName)
        if newFileName == '':
            raise Exception(messagebox.showerror("Error", "File name should not be blank."))
        
        try:
            os.rename(currentFileName, newFileName)
            messagebox.showinfo("Rename File", "Rename completed successfully.")
        except Exception as ex:
            print(ex)

    def createFile():
        fileName = fileRename.get()
        print("\nCreating file: " + fileName)
        if fileName == '':
            raise Exception(messagebox.showerror("Error", "New file name should not be blank."))
        
        try:
            file = open(fileName, "w+")
            messagebox.showinfo("Create File", "File created successfully.")
        except Exception as ex:
            print(ex)

    def removeFile():
        file = open(getFile())
        print("Removing file: " + file.name)
        try:
            os.remove(file.name)
            messagebox.showinfo("Remove File", "File removed successfully.")
        except Exception as ex:
            print(ex)

    def makeDirectory():
        dirName = fileRename.get()
        if dirName == '':
            raise Exception(messagebox.showerror("Error", "Directory name should not be blank."))
        
        cwd = os.getcwd()
        print("Creating directory " + dirName + " in " + cwd)
        try:
            os.mkdir(dirName)
            print("Directory created.")
            fileRename.clear()
        except Exception as ex:
            print(ex)

    def removeDirectory():
        cwd = os.getcwd()
        directory = filedialog.askdirectory(initialdir=cwd)
        if directory == '':
            print("Dialog cancelled.")
        else:
            try:
                os.rmdir(directory)
                print("Directory removed.")
            except Exception as ex:
                print(ex)

    def getCwd():
        cwd = os.getcwd()
        messagebox.showinfo("Current Directory", cwd)

    #File
    openFile = Button(window, text="Open File (ファイルを開く)", command=getFile).place(x=0, y=2, width=300, height=40)
    textBox = Entry(window)
    textBox.place(x=0, y=44, width=300, height=60)
    writeToFile = Button(window, text="Write to File (ファイルに書き込む)", command=writeToFile).place(x=0, y=100, width=300, height=40)
    appendToFile = Button(window, text="Append to File (ファイルに追加)", command=appendToFile).place(x=0, y=140, width=300, height=40)

    #OS
    fileRename = Entry(window)
    fileRename.place(x=0, y=200, width=300, height=60)
    renameFile = Button(window, text="Rename File (ファイルの名前を変更)", command=renameFile).place(x=0, y=260, width=300, height=40)
    createFile = Button(window, text="Create File (ファイルを作成する)", command=createFile).place(x=0, y=300, width=300, height=40)
    removeFile = Button(window, text="Remove File (ファイルを削除する)", command=removeFile).place(x=0, y=340, width=300, height=40)
    makeDirectory = Button(window, text="Make Directory (ディレクトリを作る)", command=makeDirectory).place(x=0, y=380, width=300, height=40)
    removeDirectory = Button(window, text="Remove Directory (ディレクトリを削除する)", command=removeDirectory).place(x=0, y=420, width=300, height=40)
    currentDirectory = Button(window, text="Current Directory (カレントディレクトリ)", command=getCwd).place(x=0, y=460, width=300, height=40)

    window.mainloop()
