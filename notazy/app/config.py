from dotenv import load_dotenv
import os

load_dotenv()

CERT_PASSWORD = os.getenv("CERT_PASSWORD")
CNPJ = os.getenv("CNPJ")
