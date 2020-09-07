import os
from utils.get_current_os import get_current_os


# Função que retorna o diretório dos arquivos com extensão ".feature" para execução do BDD
def get_features_folder():
    if get_current_os() == "Linux":
        run_way = os.popen('pwd').read()
        features = run_way.replace('\n', '/features/').strip()
        return str(features)
    elif get_current_os() == "Windows":
        way = os.popen('cd ,').read()
        features = way.replace('\n', '\\features\\').strip()
        return str(features)
