from pyvirtualdisplay import Display


# Método utilizado para iniciar um display para execução dos testes em Headless
def open_display():
    try:
        display = Display(visible=0, size=(800, 600))
        display.start()
    except Exception as e:
        print(e)
