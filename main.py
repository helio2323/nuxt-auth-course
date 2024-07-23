import requests
import json

# URL base da Piston API
BASE_URL = "https://emkc.org/api/v2/piston"

# Função para obter as versões disponíveis das linguagens
def get_language_versions():
    response = requests.get(f"{BASE_URL}/runtimes")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao obter as versões das linguagens: {response.text}")

# Função para executar o código
def execute_code(language, source_code):
    # Obter versões disponíveis
    language_versions = get_language_versions()
    
    # Encontrar uma versão válida para a linguagem
    version = next((v['version'] for v in language_versions if v['language'] == language), None)
    if not version:
        raise Exception(f"Versão para a linguagem {language} não encontrada.")
    
    # Payload com o código e a versão da linguagem
    payload = {
        "language": language,
        "version": version,
        "files": [
            {
                "content": source_code
            }
        ]
    }

    # Cabeçalhos da requisição
    headers = {
        "Content-Type": "application/json"
    }

    # Fazendo a requisição POST à Piston API
    response = requests.post(f"{BASE_URL}/execute", headers=headers, data=json.dumps(payload))
    
    # Verificando a resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao executar o código: {response.text}")

# Código Python para somar dois números
source_code = """
class Solution(object):
    def twoSum(self, nums, target):
        
        





"""

# Exemplo de uso
try:
    result = execute_code("python", source_code)
    print("Saída do código:")
    print(result['run']['output'])

except Exception as e:
    print(e)
