import os
from utils.get_current_os import get_current_os


# Médoto que mata o processo dos drivers do selenium no sistema operacional pós execução dos testes
def kill_driver(browser):
    def kill_linux():
        if browser == 'F':
            os.popen('killall geckodriver')
        elif browser == 'C':
            os.popen('killall chromedriver')
        else:
            raise Exception('Navegador não suportado pela execução do comando kill!')

    def kill_windows():
        if browser == 'F':
            os.popen('tskill geckodriver*')
        elif browser == 'C':
            os.popen('tskill chromedriver*')
        else:
            raise Exception('Navegador não suportado pela execução do comando kill!')

    if get_current_os() == "Linux":
        kill_linux()
    elif get_current_os() == "Windows":
        kill_windows()
