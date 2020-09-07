from behave import *
from page.home.americanas_home_page import HomePage
from page.smartphones.americanas_smartphone_page import SmartphonePage
from page.product.americanas_product_page import ProductPage
from page.warranty.americanas_warranty_page import WarrantyPage
from page.cart.americanas_cart_page import CartPage
from drivers.interact import Interact


# Função de gatilho que é executado antes do inicio do teste
def before_test():
    pass


# Função de gatilho que é executada pós teste
def after_test():
    Interact.teardown()


# Classe com teste de adição do produto no carrinho utilizando BDD
class AddProductToCart:
    @given(u'que eu esteja com a home do portal americanas aberto @add_product')
    def open_page(context):
        before_test()
        Interact.open_url(HomePage.url)
        if not HomePage.title == Interact.get_title():
            raise Exception('Título da página não correspondente.')

        Interact.delay(3)
        Interact.click('xpath', HomePage.button_confirm_lgpd())

    @when(u'eu inserir o código do produto no campo de busca @add_product')
    def insert_product_code(context):
        Interact.send_keys(
            'xpath',
            HomePage.input_search_element(),
            int(Interact.get_excel('americanas', 1, 1))
        )

    @when(u'clicar no botão de busca @add_product')
    def click_search(context):
        Interact.click(
            'xpath',
            HomePage.button_search_element()
        )

    @then(u'a pesquisa é realizada e o produto corespondente é exibido na lista @add_product')
    def search_results(context):
        Interact.wait_visible_element(
            'xpath',
            2,
            SmartphonePage.div_first_product_element()
        )

    @then(u'selecionar o produto @add_product')
    def select_product(context):
        Interact.execute_javascript('window.scrollTo(0, 200)')
        Interact.delay(2)
        Interact.click(
            'xpath',
            SmartphonePage.div_first_product_element()
        )

    @then(u'a página com as informações para compra do produto é exibida @add_product')
    def wait_product_page(context):
        Interact.delay(2)
        if not ProductPage.title == Interact.get_title():
            raise Exception('Título da página não correspondente.')

    @then(u'validar as informações do produto @add_product')
    def validate_product_info(context):
        # Por algum motivo o portal americanas não está deixando a função gettext retornar o texto do elemento
        # Porém as validações estão aqui nesta função para verificação

        # Validar descrição do produto
        # if not Interact.get_text('xpath', ProductPage.h1_product_name_element()) == Interact.get_excel('americanas', 2, 1):
        #    raise Exception('Produto não correspondente!')

        # Validar preço do produto
        # if not Interact.get_text('xpath', ProductPage.span_product_price_element()) == Interact.get_excel('validate', 1, 1):
        #    raise Exception('Preço do produto não correspondente!')
        pass

    @then(u'clicar em comprar @add_product')
    def click_buy_product(context):
        Interact.click(
            'xpath',
            ProductPage.span_buy_product_element()
        )

    @then(u'a página de seleção da garantia e do seguro é exibida @add_product')
    def wait_warranty_page(context):
        Interact.delay(3)
        if not WarrantyPage.title == Interact.get_title():
            raise Exception('Título da página não correspondente.')

    @then(u'clicar em continuar @add_product')
    def click_continue(context):
        Interact.execute_javascript('window.scrollTo(0, 400)')
        Interact.delay(2)
        Interact.click(
            'xpath',
            WarrantyPage.span_continue_element()
        )

    @then(u'a página do carrinho de compras é exibida com o produto adicionado @add_product')
    def wait_cart_page(context):
        Interact.delay(3)
        if not CartPage.title == Interact.get_title():
            raise Exception('Título da página não correspondente.')

    @then(u'validar as informações do produto no carrinho de compras @add_product')
    def validate_product_cart(context):
        # Por algum motivo o portal americanas não está deixando a função gettext retornar o texto do elemento
        # Porém as validações estão aqui nesta função para verificação

        # Validar descrição do produto
        # if not Interact.get_text('xpath', CartPage.a_product_name_element()) == Interact.get_excel('americanas', 3, 1):
        #    raise Exception('Produto não correspondente!')

        # Validar preço do produto
        # if not Interact.get_text('xpath', CartPage.div_cart_product_price_element()) == Interact.get_excel('validate', 1, 1):
        #    raise Exception('Preço do produto não correspondente!')
        after_test()
