import os
from utils.get_current_os import get_current_os


# Função que retorna o diretório atual
def get_current_folder():
    if get_current_os() == "Linux":
        run_way = os.popen('pwd').read()
        current = run_way.replace('\n', '').strip()
        return str(current)
    elif get_current_os() == "Windows":
        way = os.popen('cd ,').read()
        current = way.strip()
        return str(current)
