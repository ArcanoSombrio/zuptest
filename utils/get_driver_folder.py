import os
from utils.get_current_os import get_current_os


# Função que retorna o diretório e nome do arquivo de driver do chrome de acordo com o S.O
def chromedriver():
    if get_current_os() == "Linux":
        way = os.popen('pwd').read()
        chromedriver = way.replace('\n', '/drivers/files/chromedriver').strip()
        return str(chromedriver)
    elif get_current_os() == "Windows":
        way = os.popen('cd ,').read()
        chromedriver = way.strip() + '\\drivers\\files\\chromedriver.exe'
        return str(chromedriver)


# Função que retorna o diretório e nome do arquivo de driver do firefox de acordo com o S.O
def geckodriver():
    if get_current_os() == "Linux":
        way = os.popen('pwd').read()
        geckodriver = way.replace('\n', '/drivers/files/geckodriver').strip()
        return str(geckodriver)
    elif get_current_os() == "Windows":
        way = os.popen('cd ,').read()
        geckodriver = way.strip() + "\\drivers\\files\\geckodriver.exe"
        return str(geckodriver)
