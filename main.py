from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox, QCheckBox, QPushButton, QFrame, QGridLayout, QHBoxLayout)
from PySide6.QtCore import Qt
import random
import string
import sys

# cores 
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#f05a43"  # vermelha

fundo_dark = "#484f60"
fundo_claro = "#fff"
fundo = co1

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gerador de Senhas')
        self.setFixedSize(300, 360)
        self.setStyleSheet(f"background-color: {fundo};")

        # Layout principal
        main_layout = QVBoxLayout(self)
        
        # Frame principal
        frame_main = QFrame()
        frame_main.setFixedHeight(110)
        frame_main.setStyleSheet(f"background-color: {fundo};")
        
        # Layout para o frame principal
        frame_main_layout = QVBoxLayout(frame_main)
        main_layout.addWidget(frame_main)

        app_name = QLabel("GERADOR DE SENHAS")
        app_name.setStyleSheet(f"font: bold 16px; color: {co0}; background-color: {co1};")
        app_name.setAlignment(Qt.AlignCenter)
        frame_main_layout.addWidget(app_name)

        app_linha = QLabel()
        app_linha.setFixedHeight(1)
        app_linha.setStyleSheet(f"background-color: {co3};")
        frame_main_layout.addWidget(app_linha)
        
        # Layout horizontal para o número de caracteres e o spinbox
        h_layout = QHBoxLayout()
        
        app_info = QLabel("Número total de caracteres na senha")
        app_info.setStyleSheet(f"font: bold 10px; color: {co0}; background-color: {fundo};")
        h_layout.addWidget(app_info)

        self.spin = QSpinBox()
        self.spin.setRange(0, 20)
        self.spin.setValue(8)  
        self.spin.setStyleSheet(f"color: {co0};")  
        h_layout.addWidget(self.spin)

        frame_main_layout.addLayout(h_layout)

        # Frame para checkboxes e senha gerada
        frame_box = QFrame()
        frame_box.setStyleSheet(f"background-color: {fundo};")
        main_layout.addWidget(frame_box)

        grid_layout = QGridLayout(frame_box)

        self.app_senha = QLabel("- - -")
        self.app_senha.setFixedHeight(40)
        self.app_senha.setStyleSheet(f"font: bold 10px; color: {co0}; background-color: {fundo}; border: 1px solid {co0};")
        self.app_senha.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(self.app_senha, 0, 0, 1, 2)

        # Checkboxes
        self.estado_1 = QCheckBox("ABC Letras maiúsculas")
        self.estado_1.setStyleSheet(f"font: bold 10px; color: {co0}; background-color: {co1};")
        grid_layout.addWidget(self.estado_1, 1, 1)
        
        self.estado_2 = QCheckBox("abc Letras minúsculas")
        self.estado_2.setStyleSheet(f"font: bold 10px; color: {co0}; background-color: {co1};")
        grid_layout.addWidget(self.estado_2, 2, 1)
        
        self.estado_3 = QCheckBox("123 Números")
        self.estado_3.setStyleSheet(f"font: bold 10px; color: {co0}; background-color: {co1};")
        grid_layout.addWidget(self.estado_3, 3, 1)
        
        self.estado_4 = QCheckBox("!@# Símbolos")
        self.estado_4.setStyleSheet(f"font: bold 10px; color: {co0}; background-color: {co1};")
        grid_layout.addWidget(self.estado_4, 4, 1)
        
        # Botão de gerar senha
        b_gerar_senha = QPushButton("Gerar senha")
        b_gerar_senha.setStyleSheet(f"font: bold 10px; color: white; background-color: {co3};")
        b_gerar_senha.clicked.connect(self.gerar_senha)
        grid_layout.addWidget(b_gerar_senha, 5, 0, 1, 2)
        
        # Botão de copiar
        b_copiar = QPushButton("Copiar")
        b_copiar.setStyleSheet(f"font: bold 10px; color: {co0}; background-color: {co1};")
        b_copiar.clicked.connect(self.copiar_senha)
        grid_layout.addWidget(b_copiar, 0, 2)

    def gerar_senha(self):
        tamanho = self.spin.value()
        caracteres = ""
        if self.estado_1.isChecked():
            caracteres += string.ascii_uppercase
        if self.estado_2.isChecked():
            caracteres += string.ascii_lowercase
        if self.estado_3.isChecked():
            caracteres += '123456789'
        if self.estado_4.isChecked():
            caracteres += "[]{}()*;/,_-"
        
        if caracteres:
            senha = ''.join(random.choice(caracteres) for i in range(tamanho))
        else:
            senha = "- - -"
        
        self.app_senha.setText(senha)
    
    def copiar_senha(self):
        senha = self.app_senha.text()
        if senha != "- - -":
            QApplication.clipboard().setText(senha)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
