from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QFileDialog, QMessageBox
)
import sys
from app.services.certificado import carregar_certificado_pfx
from app.config import CERT_PASSWORD

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notazy - Cadastro Empresa e Certificado")

        self.layout = QVBoxLayout()

        self.cnpj_label = QLabel("CNPJ:")
        self.cnpj_input = QLineEdit()
        self.layout.addWidget(self.cnpj_label)
        self.layout.addWidget(self.cnpj_input)

        self.cert_label = QLabel("Arquivo .pfx:")
        self.cert_path = QLineEdit()
        self.cert_browse = QPushButton("Selecionar")
        self.cert_browse.clicked.connect(self.selecionar_certificado)
        self.layout.addWidget(self.cert_label)
        self.layout.addWidget(self.cert_path)
        self.layout.addWidget(self.cert_browse)

        self.senha_label = QLabel("Senha do certificado:")
        self.senha_input = QLineEdit()
        self.senha_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.senha_label)
        self.layout.addWidget(self.senha_input)

        self.testar_btn = QPushButton("Testar Certificado")
        self.testar_btn.clicked.connect(self.testar_certificado)
        self.layout.addWidget(self.testar_btn)

        self.setLayout(self.layout)

    def selecionar_certificado(self):
        caminho, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo .pfx", "", "Arquivos PFX (*.pfx)")
        if caminho:
            self.cert_path.setText(caminho)

    def testar_certificado(self):
        caminho = self.cert_path.text()
        senha = self.senha_input.text()
        chave, cert = carregar_certificado_pfx(caminho, senha)
        if cert:
            QMessageBox.information(self, "Sucesso", "Certificado carregado com sucesso!")
        else:
            QMessageBox.critical(self, "Erro", "Falha ao carregar o certificado.")

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
