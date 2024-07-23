from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

class Criptografia:
    def __init__(self):
        self.backend = default_backend()
        self.salt = os.urandom(16)  # Gera um salt aleatório

    def encriptar_senha(self, senha):
        # Converte a senha para bytes
        senha_bytes = senha.encode('utf-8')
        # Configura o algoritmo PBKDF2HMAC com SHA256
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=self.backend
        )
        # Gera a chave (hash) da senha
        chave = kdf.derive(senha_bytes)
        # Retorna a chave codificada em base64 junto com o salt
        return base64.urlsafe_b64encode(self.salt + chave).decode('utf-8')

# Criando uma instância da classe Criptografia
cripto = Criptografia()

# Encriptando uma senha e imprimindo o resultado
senha = "minha_senha_secreta"
senha_encriptada = cripto.encriptar_senha(senha)
print(f"A senha encriptada é: {senha_encriptada}")
