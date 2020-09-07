from drivers.execute import Execute
from drivers.interact import Interact


# Função de gatilho que é executada antes da suite de testes
# Recebe a variável browser para escolha do navegador para execução
def before_suite(browser, headless):
    Interact.setup(browser, headless)


# Função de gatilho que é executada pós suite de testes
def after_suite():
    Interact.teardown()


# Classe onde são chamadas as execuções dos gatilhos before e after suite, e dos testes
class Main:
    # Método onde se inserem as features na ordem especificada para execução dos testes, é o conceito de suite
    def __init__(self):
        before_suite('F', True)
        Execute.start_bdd_test(
            stories_list=[
                'add_product_to_cart.feature',
                'add_plus_quantity_product_to_cart.feature',
                'remove_product_from_cart.feature'
            ]
        )
        after_suite()


if __name__ == '__main__':
    Main()
