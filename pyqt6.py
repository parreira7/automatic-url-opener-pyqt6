import sys
from PyQt6.QtWidgets import * 
from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QFont
import webbrowser
#config root
app = QApplication(sys.argv)
window = QWidget()
window.resize(600,200)
window.setWindowTitle("URL Opener")
window.setWindowIcon(QtGui.QIcon('icon.png'))
window.setStyleSheet('background-color: #967AA1;')
#texto do programa
url_auto = QLabel('Automatic URL Opener',window)
url_auto.move(50,0)
url_auto.setFont(QFont('Sketch 3D', 32))
url_auto.setStyleSheet('color: #D5C6E0')
#urls
yt = 'https://www.youtube.com/'
lnkdin = 'https://www.linkedin.com/feed/'
git = 'https://github.com/'
stack = 'https://stackoverflow.com/'
nub = 'https://www.nube.com.br/'
wppweb = 'https://web.whatsapp.com/'
w3 = 'https://www.w3schools.com/'
mail = 'https://mail.google.com/mail/'
ind = 'https://br.indeed.com/'
ggle = 'https://www.google.com.br/'
insta = 'https://www.instagram.com/'
fb = 'https://www.facebook.com/'
uam = 'https://estudantesuam.ead.br/'
tele = 'https://web.telegram.org/'
ude_my = 'https://www.udemy.com/'
netf = 'https://www.netflix.com/browse'
#funçoes
def youtube():
    webbrowser.open_new(yt)
def linkedin():
    webbrowser.open_new(lnkdin)
def github():
    webbrowser.open_new(git)
def stackoverflow():
    webbrowser.open_new(stack)
def nube():
    webbrowser.open_new(nub)
def whatsapp():
    webbrowser.open_new(wppweb)
def w3shools():
    webbrowser.open_new(w3)
def gmail():
    webbrowser.open_new(mail)
def indeed():
    webbrowser.open_new(ind)
def google():
    webbrowser.open_new(ggle)
def instagram():
    webbrowser.open_new(insta)
def facebook():
    webbrowser.open_new(fb)
def faculdade():
    webbrowser.open_new(uam)
def telegram():
    webbrowser.open_new(tele)
def udemy():
    webbrowser.open_new(ude_my)
def netflix():
    webbrowser.open_new(netf)
#cores
fundo = '#FCF6B1'
letra = '#2D1E2F'
#botoes
button = QPushButton(window)
button.clicked.connect(youtube) 
button.setGeometry(70, 70, 50, 50)
button.setIcon(QIcon('ytb.png'))
button.setIconSize(QtCore.QSize(50, 50)) 

button1 = QPushButton(window)
button1.clicked.connect(github) 
button1.setGeometry(120, 70, 50, 50)
button1.setIcon(QIcon('github.png'))
button1.setIconSize(QtCore.QSize(50, 50)) 

button2 = QPushButton(window)
button2.clicked.connect(linkedin) 
button2.setGeometry(170, 70, 50, 50)
button2.setIcon(QIcon('linkedin.png'))
button2.setIconSize(QtCore.QSize(50, 50)) 

button3 = QPushButton(window)
button3.clicked.connect(stackoverflow) 
button3.setGeometry(220, 70, 50, 50)
button3.setIcon(QIcon('stackoverflow.png'))
button3.setIconSize(QtCore.QSize(50, 50)) 

button4 = QPushButton(window)
button4.clicked.connect(nube) 
button4.setGeometry(270, 70, 50, 50)
button4.setIcon(QIcon('nubee.png'))
button4.setIconSize(QtCore.QSize(60, 60)) 

button5 = QPushButton(window)
button5.clicked.connect(whatsapp)
button5.setGeometry(320, 70, 50, 50)
button5.setIcon(QIcon('wpp.png'))
button5.setIconSize(QtCore.QSize(40, 40))

button6 = QPushButton(window)
button6.clicked.connect(w3shools)
button6.setGeometry(370, 70, 50, 50)
button6.setIcon(QIcon('w3s.png'))
button6.setIconSize(QtCore.QSize(40, 40))

button7 = QPushButton(window)
button7.clicked.connect(gmail)
button7.setGeometry(420, 70, 50, 50)
button7.setIcon(QIcon('gmail.png'))
button7.setIconSize(QtCore.QSize(40, 40))

button8 = QPushButton(window)
button8.clicked.connect(indeed)
button8.setGeometry(470, 70, 50, 50)
button8.setIcon(QIcon('work.png'))
button8.setIconSize(QtCore.QSize(40, 40))

button9 = QPushButton(window)
button9.clicked.connect(google)
button9.setGeometry(120, 120, 50, 50)
button9.setIcon(QIcon('google.png'))
button9.setIconSize(QtCore.QSize(40, 40))

button10 = QPushButton(window)
button10.clicked.connect(instagram)
button10.setGeometry(170, 120, 50, 50)
button10.setIcon(QIcon('insta.png'))
button10.setIconSize(QtCore.QSize(40, 40))

button11 = QPushButton(window)
button11.clicked.connect(facebook)
button11.setGeometry(220, 120, 50, 50)
button11.setIcon(QIcon('faceb.png'))
button11.setIconSize(QtCore.QSize(40, 40))

button12 = QPushButton(window)
button12.clicked.connect(faculdade)
button12.setGeometry(270, 120, 50, 50)
button12.setIcon(QIcon('facul.png'))
button12.setIconSize(QtCore.QSize(40, 40))

button13 = QPushButton(window)
button13.clicked.connect(telegram)
button13.setGeometry(320, 120, 50, 50)
button13.setIcon(QIcon('teleg.png'))
button13.setIconSize(QtCore.QSize(40, 40))

button14 = QPushButton(window)
button14.clicked.connect(udemy)
button14.setGeometry(370, 120, 50, 50)
button14.setIcon(QIcon('udemy.png'))
button14.setIconSize(QtCore.QSize(40, 40))

button15 = QPushButton(window)
button15.clicked.connect(netflix)
button15.setGeometry(420, 120, 50, 50)
button15.setIcon(QIcon('netf.png'))
button15.setIconSize(QtCore.QSize(40, 40))

window.show()
app.exec()



