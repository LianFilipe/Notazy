from dataclasses import dataclass

@dataclass
class Empresa:
    cnpj: str
    caminho_certificado: str
    senha_certificado: str
