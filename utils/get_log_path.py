import errno
import os
import re

from utils.get_current_os import get_current_os
from utils.get_date_time import get_date_time


# Método que valida o S.O e cria a pasta de logs e screenshot dos erros de execução de acordo com o navegador
def get_log_path(screenshot, browser):
    log = None

    def log_path():
        if browser == 'F':
            if screenshot:
                directory = 'firefox/%s/screenshot' % get_date_time(True)
                filename = '/web_firefox_screenshot %s.png' % get_date_time(False)
                if get_current_os() == "Linux":
                    return directory + filename
                elif get_current_os() == "Windows":
                    directory = directory.replace('/', '\\\\')
                    filename = filename.replace('/', '\\\\')
                    return directory + filename
            else:
                directory = 'firefox/%s' % get_date_time(True)
                filename = '/web_firefox %s.log' % get_date_time(False)
                if get_current_os() == "Linux":
                    return directory + filename
                elif get_current_os() == "Windows":
                    directory = directory.replace('/', '\\\\')
                    filename = filename.replace('/', '\\\\')
                    return directory + filename
        elif browser == 'C':
            if screenshot:
                directory = 'chrome/%s/screenshot' % get_date_time(True)
                filename = '/web_chrome_screenshot %s.png' % get_date_time(False)
                if get_current_os() == "Linux":
                    return directory + filename
                elif get_current_os() == "Windows":
                    directory = directory.replace('/', '\\\\')
                    filename = filename.replace('/', '\\\\')
                    return directory + filename
            else:
                directory = 'chrome/%s' % get_date_time(True)
                filename = '/web_chrome %s.log' % get_date_time(False)
                if get_current_os() == "Linux":
                    return directory + filename
                elif get_current_os() == "Windows":
                    directory = directory.replace('/', '\\\\')
                    filename = filename.replace('/', '\\\\')
                    return directory + filename

    if get_current_os() == "Linux":
        run_way = os.popen('pwd').read()
        current = run_way.replace('\n', '/log/').strip()
        log = current + log_path()
        if screenshot:
            screen = re.compile('(?:(.*/))')
            screen = screen.findall(log)
            if not os.path.exists(os.path.dirname(screen[0] + 'screenshot')):
                try:
                    os.makedirs(os.path.dirname(screen[0] + 'screenshot'), exist_ok=True)
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
        return log
    elif get_current_os() == "Windows":
        way = os.popen('cd ,').read()
        current = way.replace('\n', '\\log\\').strip()
        log = current + log_path()
        if screenshot:
            screen = re.compile('(?:(.*\\\\))')
            screen = screen.findall(log)
            if not os.path.exists(os.path.dirname(screen[0] + 'screenshot')):
                try:
                    os.makedirs(os.path.dirname(screen[0] + 'screenshot'), exist_ok=True)
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
        return log
