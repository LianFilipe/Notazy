from cryptography.hazmat.primitives.serialization import pkcs12

def carregar_certificado_pfx(caminho_pfx: str, senha: str):
    with open(caminho_pfx, 'rb') as f:
        pfx_data = f.read()
    try:
        p12 = pkcs12.load_key_and_certificates(pfx_data, senha.encode())
        chave_privada = p12[0]
        certificado = p12[1]
        # Você pode extrair informações do certificado aqui para validar
        return chave_privada, certificado
    except Exception as e:
        print(f"Erro ao carregar certificado: {e}")
        return None, None
