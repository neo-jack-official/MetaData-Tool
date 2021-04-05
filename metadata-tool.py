#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By Neo-Jack 2021

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class varT:
    info = color.YELLOW + "[INFO]:" + color.END
    home = "/home/"        
    escrSP = "/Escritorio/"
    libSP = "Instalando Libreria faltante."
    listo = " Listo..."    
    insDepSP = " Instalando dependencia..."    
    espera = " Esperando..."    
    traSP = " Traducido..."
    ingrSP = " Tienes que ingresar un Directorio y nombre de Archivo valido."
    expFileSP = " Archivo exportado en "
    metaSP = " Meta Data Eliminada de: "
    escrEN = "/Desktop/"
    done = " Done..."
    instDepEN = " Installing dependency ... "
    wait = " Waiting..."
    traEN = " Translated..."
    ingrEN = " You have to enter a valid Directory and Filename. "
    expFileEN = " Exported file in  " 
    metaEN = " Meta Data Removed from:  "

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

from os import system, name
import sys, os, time
from PIL import Image 
import pickle 
    
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    clear()
    print(color.PURPLE + color.UNDERLINE + varT.libSP + color.END)
    system('pip3 install pyqt5')
    
usr = os.getlogin()

def db():
    global baseInsExif
    global baseidioma    
    baseInsExif = "SI"; baseidioma = "SP";    
    try:
        baseInsExif, baseidioma = pickle.load(open("conf.neo","rb"))                
        if baseInsExif == "SI":
            if baseidioma == "SP":
                try:
                    clear()
                    print(varT.info + varT.insDepSP)
                    system('sudo apt-get update')
                    system('sudo apt-get install libimage-exiftool-perl') # Ubuntu, Debian, Mint, Kali
                    clear()
                    print(varT.info + varT.listo)
                except:
                    clear()
                    print(varT.info + varT.insDepSP)
                    system('sudo dnf update')           
                    system('sudo dnf install perl-Image-ExifTool.noarch') # Fedora, CentOS, RedHat
                    clear()
                    print(varT.info + varT.listo)
            elif baseidioma == "EN":
                try:
                    clear()
                    print(varT.info + varT.instDepEN)
                    system('sudo apt-get update')
                    system('sudo apt-get install libimage-exiftool-perl') # Ubuntu, Debian, Mint, Kali
                    clear()
                    print(varT.info + varT.done)
                except:
                    clear()
                    print(varT.info + varT.insDepEN)
                    system('sudo dnf update')           
                    system('sudo dnf install perl-Image-ExifTool.noarch') # Fedora, CentOS, RedHat
                    clear()
                    print(varT.info + varT.done)               
        elif baseInsExif == "NO":
            if baseidioma == "SP":
                clear()
                print(varT.info + varT.espera)
            elif baseidioma == "EN":
                clear()
                print(varT.info + varT.wait)      
        baseInsExif = "NO"
        pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb")) 
    except: 
        pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb"))
        baseInsExif, baseidioma = pickle.load(open("conf.neo","rb"))        
        if baseInsExif == "SI":
            if baseidioma == "SP":
                try:
                    clear()                    
                    print(varT.info + varT.insDepSP)
                    system('sudo apt-get update')
                    system('sudo apt-get install libimage-exiftool-perl') # Ubuntu, Debian, Mint, Kali
                    clear()
                    print(varT.info + varT.listo)
                except:
                    clear()
                    print(varT.info + varT.insDepSP)
                    system('sudo dnf update')           
                    system('sudo dnf install perl-Image-ExifTool.noarch') # Fedora, CentOS, RedHat
                    clear()
                    print(varT.info + varT.listo)
            elif baseidioma == "EN":
                try:
                    clear()                    
                    print(varT.info + varT.instDepEN)
                    system('sudo apt-get update')
                    system('sudo apt-get install libimage-exiftool-perl') # Ubuntu, Debian, Mint, Kali
                    clear()
                    print(varT.info + varT.done)
                except:
                    clear()
                    print(varT.info + varT.insDepEN)
                    system('sudo dnf update')           
                    system('sudo dnf install perl-Image-ExifTool.noarch') # Fedora, CentOS, RedHat
                    clear()
                    print(varT.info + varT.done)                    
        elif baseInsExif == "NO":
            if baseidioma == "SP":
                clear()
                print(varT.info + varT.espera)
            elif baseidioma == "EN":
                clear()
                print(varT.info + varT.wait)
        baseInsExif = "NO"
        pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb")) 
        
db()

class Ui_MainWindow(object):   

    def rutaE(self):
        global folder
        baseInsExif, baseidioma = pickle.load(open("conf.neo","rb"))
        if self.sp_radio.isChecked():
            escritorio = varT.escrSP            
            baseidioma = "SP"            
            pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb"))             
        elif self.en_radio.isChecked():
            escritorio = varT.escrEN            
            baseidioma = "EN"            
            pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb"))            
        folder = varT.home + usr + escritorio
        self.ruta_e.setText(folder)
    
    def confInstala(self):
        baseInsExif, baseidioma = pickle.load(open("conf.neo","rb"))
        if self.si_radio.isChecked():
            baseInsExif = "SI"
            pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb"))
        elif self.no_radio.isChecked():
            baseInsExif = "NO"
            pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb"))

    def instalar(self):                
        if self.si_radio.isChecked():            
            baseInsExif = "SI"
            pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb"))
            try:                
                if self.sp_radio.isChecked():
                    clear()
                    print(varT.info + varT.insDepSP)
                elif self.en_radio.isChecked():
                    clear()
                    print(varT.info + varT.instDepEN)                    
                system('sudo apt-get update')
                system('sudo apt-get install libimage-exiftool-perl') # Ubuntu, Debian, Mint, Kali
                clear()
                if self.sp_radio.isChecked():
                    clear()
                    print(varT.info + varT.listo)
                elif self.en_radio.isChecked():
                    clear()
                    print(varT.info + varT.done)
            except:
                if self.sp_radio.isChecked():
                    clear()
                    print(varT.info + varT.insDepSP)
                elif self.en_radio.isChecked():
                    clear()
                    print(varT.info + varT.varT.instDepEN)
                system('sudo dnf update')             
                system('sudo dnf install perl-Image-ExifTool.noarch') #Fedora, CentOS, RedHat                
                clear()
                if self.sp_radio.isChecked():
                    clear()
                    print(varT.info + varT.listo)
                elif self.en_radio.isChecked():
                    clear()
                    print(varT.info + varT.done)
            baseInsExif = "NO"
            pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb"))
            self.no_radio.setChecked(True)
            
        elif self.no_radio.isChecked():
            baseInsExif = "NO"
            pickle.dump([baseInsExif, baseidioma], open("conf.neo","wb"))            
            clear()
            if self.sp_radio.isChecked():
                clear()
                print(varT.info + varT.espera)
            elif self.en_radio.isChecked():
                clear()
                print(varT.info + varT.wait)
            pass
        
    def idioma(self):
        global escritorio
        if self.sp_radio.isChecked():            
            self.retranslate_SP(MainWindow)
            escritorio = varT.escrSP 
            self.rutaE()           
            clear()
            print(varT.info + varT.traSP + varT.listo)
        elif self.en_radio.isChecked():            
            self.retranslate_EN(MainWindow)
            escritorio = varT.escrEN 
            self.rutaE()
            clear()
            print(varT.info + varT.traEN + varT.done)            
        
    def cambia_img(self):   
        folder = str(self.ruta_e.text())                          
        imagen = str(self.img_name_e.text())
        rutaCompleta = folder + imagen        
        if imagen != ".png, .jpg, .gif, .pdf, .zip, .doc, etc.":
            try:
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(rutaCompleta), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.abrir_img_b.setIcon(icon1)                
            except:
                print("err")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("img/no2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.abrir_img_b.setIcon(icon1)                
        else:
            if self.sp_radio.isChecked():
                clear()
                print(varT.info + varT.ingrSP)
            elif self.en_radio.isChecked():
                clear()
                print(varT.info + varT.ingrEN)
    
    def abreimg(self):        
        folder = str(self.ruta_e.text())       
        imagen = str(self.img_name_e.text())
        rutaCompleta = folder + imagen        
        try:
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(rutaCompleta), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.abrir_img_b.setIcon(icon1)            
            ruta = Image.open(folder + imagen, 'r')
            ruta.show()
        except:
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("img/no2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.abrir_img_b.setIcon(icon1)  

    def ver_exif(self):        
        folder = str(self.ruta_e.text())              
        imagen = str(self.img_name_e.text())
        rutaCompleta = folder + imagen      
        clear()        
        os.system('exiftool ' + rutaCompleta)
    
    def exportar(self):       
        folder = str(self.ruta_e.text())
        imagen = str(self.img_name_e.text())
        rutaCompleta = folder + imagen                
        clear()
        if self.sp_radio.isChecked():
            print(varT.info + varT.expFileSP + rutaCompleta + ".html")
            os.system('exiftool -h ' + rutaCompleta + ' > ' + rutaCompleta + '.html')
        elif self.en_radio.isChecked():
            print(varT.info + varT.expFileEN + rutaCompleta + ".html")
            os.system('exiftool -h ' + rutaCompleta + ' > ' + rutaCompleta + '.html')
          
    def limpiaExif(self):
        folder = str(self.ruta_e.text())
        imagen = str(self.img_name_e.text())
        rutaCompleta = folder + imagen
        clear()
        if self.sp_radio.isChecked():
            print(varT.info + varT.metaSP + imagen)
            os.system('exiftool -all= ' + rutaCompleta)
        elif self.en_radio.isChecked():
            print(varT.info + varT.metaEN + imagen)
            os.system('exiftool -all= ' + rutaCompleta)

    def setupUi(self, MainWindow):                
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 494)        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/anon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 351, 58))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid1.setContentsMargins(0, 0, 0, 0)
        self.grid1.setObjectName("grid1")
        self.ruta_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ruta_txt.setObjectName("ruta_txt")
        self.grid1.addWidget(self.ruta_txt, 0, 0, 1, 1)        
        self.ruta_e = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ruta_e.setTabletTracking(False)
        self.ruta_e.setObjectName("ruta_e")
        self.grid1.addWidget(self.ruta_e, 0, 1, 1, 1)
        self.img_nombre_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img_nombre_txt.setObjectName("img_nombre_txt")
        self.grid1.addWidget(self.img_nombre_txt, 1, 0, 1, 1)
        self.img_name_e = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.img_name_e.setObjectName("img_name_e")
        self.grid1.addWidget(self.img_name_e, 1, 1, 1, 1)
        self.titulo_txt = QtWidgets.QLabel(self.centralwidget)
        self.titulo_txt.setGeometry(QtCore.QRect(140, 10, 121, 17))
        self.titulo_txt.setObjectName("titulo_txt")
        self.abrir_img_b = QtWidgets.QToolButton(self.centralwidget)
        self.abrir_img_b.setGeometry(QtCore.QRect(20, 140, 351, 291))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/no.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abrir_img_b.setIcon(icon1)
        self.abrir_img_b.setIconSize(QtCore.QSize(250, 400))
        self.abrir_img_b.setAutoRepeat(False)
        self.abrir_img_b.setAutoExclusive(False)
        self.abrir_img_b.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.abrir_img_b.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.abrir_img_b.setAutoRaise(False)
        self.abrir_img_b.setObjectName("abrir_img_b")
        self.abrir_img_b.clicked.connect(self.abreimg)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 351, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontal1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontal1.setContentsMargins(0, 0, 0, 0)
        self.horizontal1.setObjectName("horizontal1")        
        self.ver_img_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ver_img_b.setObjectName("ver_img_b")
        self.ver_img_b.clicked.connect(self.cambia_img) 
        self.horizontal1.addWidget(self.ver_img_b)        
        self.ver_exif_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ver_exif_b.setObjectName("ver_exif_b")
        self.ver_exif_b.clicked.connect(self.ver_exif)
        self.horizontal1.addWidget(self.ver_exif_b)        
        self.exportar_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exportar_b.setObjectName("exportar_b")
        self.exportar_b.clicked.connect(self.exportar)
        self.horizontal1.addWidget(self.exportar_b)        
        self.borrar_exif_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.borrar_exif_b.setObjectName("borrar_exif_b")  
        self.borrar_exif_b.clicked.connect(self.limpiaExif)
        self.horizontal1.addWidget(self.borrar_exif_b)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(139, 430, 231, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")        
        self.horizontal2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontal2.setContentsMargins(0, 0, 0, 0)
        self.horizontal2.setObjectName("horizontal2")        
        self.instala_txt = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.instala_txt.setObjectName("instala_txt")
        self.horizontal2.addWidget(self.instala_txt) 
        self.si_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        if baseInsExif == "SI":
            self.si_radio.setChecked(True)
        self.si_radio.setObjectName("si_radio")
        self.si_radio.clicked.connect(self.instalar)
        self.horizontal2.addWidget(self.si_radio)        
        self.no_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        if baseInsExif == "NO":
            self.no_radio.setChecked(True)        
        self.no_radio.setObjectName("no_radio")
        self.no_radio.clicked.connect(self.instalar)
        self.horizontal2.addWidget(self.no_radio)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 460, 191, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")        
        self.horizontal3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontal3.setContentsMargins(0, 0, 0, 0)
        self.horizontal3.setObjectName("horizontal3")        
        self.idioma_txt = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.idioma_txt.setObjectName("idioma_txt")         
        self.horizontal3.addWidget(self.idioma_txt)
        self.sp_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        if baseidioma == "SP":
            self.sp_radio.setChecked(True)                  
        self.sp_radio.setObjectName("sp_radio")
        self.sp_radio.clicked.connect(self.idioma)
        self.horizontal3.addWidget(self.sp_radio)        
        self.en_radio = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        if baseidioma == "EN":
            self.en_radio.setChecked(True)            
        self.en_radio.setObjectName("en_radio")
        self.en_radio.clicked.connect(self.idioma)
        self.horizontal3.addWidget(self.en_radio)       
        self.neo_txt = QtWidgets.QLabel(self.centralwidget)
        self.neo_txt.setGeometry(QtCore.QRect(230, 470, 111, 17))
        self.neo_txt.setStyleSheet("font: 9pt \"Ubuntu\";")
        self.neo_txt.setObjectName("neo_txt")        
        self.rutaE()
        self.confInstala()        
        MainWindow.setCentralWidget(self.centralwidget)                
        if baseidioma == "SP":
            self.retranslate_SP(MainWindow)  
        else:
            self.retranslate_EN(MainWindow)              
        QtCore.QMetaObject.connectSlotsByName(MainWindow)        
    
    def retranslate_SP(self, MainWindow):        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MetaData-Tool v.1"))
        self.ruta_txt.setText(_translate("MainWindow", "Ruta:"))
        self.img_nombre_txt.setText(_translate("MainWindow", "IMG Nombre:"))
        self.img_name_e.setText(_translate("MainWindow", ".png, .jpg, .gif, .pdf, .zip, .doc, etc."))
        self.titulo_txt.setText(_translate("MainWindow", "MetaData-Tool"))
        self.abrir_img_b.setText(_translate("MainWindow", "Abrir IMG"))
        self.ver_img_b.setText(_translate("MainWindow", "Ver IMG"))
        self.ver_exif_b.setText(_translate("MainWindow", "Ver Exif"))
        self.exportar_b.setText(_translate("MainWindow", "Exp. Exif"))
        self.borrar_exif_b.setText(_translate("MainWindow", "Limpiar Exif"))
        self.neo_txt.setText(_translate("MainWindow", "by Neo-Jack 2021"))
        self.instala_txt.setText(_translate("MainWindow", "Instalar ExifTool:"))
        self.si_radio.setText(_translate("MainWindow", "Si"))
        self.no_radio.setText(_translate("MainWindow", "No"))
        self.idioma_txt.setText(_translate("MainWindow", "Lenguaje:"))
        self.sp_radio.setText(_translate("MainWindow", "SP"))
        self.en_radio.setText(_translate("MainWindow", "EN"))
        
        
    def retranslate_EN(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MetaData-Tool v.1"))
        self.ruta_txt.setText(_translate("MainWindow", "File Path :"))
        self.img_nombre_txt.setText(_translate("MainWindow", "IMG Name:"))
        self.img_name_e.setText(_translate("MainWindow", ".png, .jpg, .gif, .pdf, .zip, .doc, etc."))
        self.titulo_txt.setText(_translate("MainWindow", "MetaData-Tool"))
        self.abrir_img_b.setText(_translate("MainWindow", "Open IMG"))
        self.ver_img_b.setText(_translate("MainWindow", "View IMG"))
        self.ver_exif_b.setText(_translate("MainWindow", "View Exif"))
        self.exportar_b.setText(_translate("MainWindow", "Exp. Exif")) 
        self.borrar_exif_b.setText(_translate("MainWindow", "Wipe out Exif"))
        self.neo_txt.setText(_translate("MainWindow", "by Neo-Jack 2021"))
        self.instala_txt.setText(_translate("MainWindow", "Install ExifTool:"))
        self.si_radio.setText(_translate("MainWindow", "Yes"))
        self.no_radio.setText(_translate("MainWindow", "No"))
        self.idioma_txt.setText(_translate("MainWindow", "Language :"))
        self.sp_radio.setText(_translate("MainWindow", "SP"))
        self.en_radio.setText(_translate("MainWindow", "EN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
