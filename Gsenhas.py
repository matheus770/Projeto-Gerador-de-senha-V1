from PyQt5 import uic
import PyQt5.QtWidgets as QtWidgets
import random
import os

def gerar_senha():
    s = start.lineEdit.text()
    u = start.lineEdit_2.text()

    if(s == "") and (u == ""):
        start.lineEdit_3.setText("Erro, sem informação")
    
    elif(s == "") or (u == ""):
        start.lineEdit_3.setText("Erro, esqueceu de algo?")

    else:
        v = start.comboBox.currentText()
        carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@'
        chars = random.choices(carac, k=int(v))
        npass = ''.join(chars)
                
        with open('Crip.txt','a',newline='') as arquivo:
            arquivo.write(f"Software: {s} | User: {u} | Password: {npass}\n")
            start.lineEdit_3.setText("Senha criada e salva com sucesso")
        


app = QtWidgets.QApplication([])
start = uic.loadUi("GERATELA.ui")

start.pushButton.clicked.connect(gerar_senha)
start.pushButton_2.clicked.connect(exit)

start.show()
app.exec()

    










    


