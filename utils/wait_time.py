import gc
import sys
import time


# Método que realiza um time sleep e pausa a execução nos segundos definidos
def wait_time(time_seconds):
    try:
        gc.garbage.append(sys.stdout)
        sys.stdout.flush()
        time.sleep(int(time_seconds))
    except InterruptedError:
        raise InterruptedError
