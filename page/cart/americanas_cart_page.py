from page.page import Page


# Classe da página do carrinho de compras
class CartPage(Page):
    url = ''
    title = 'Americanas.com - A Maior Loja da Internet com os Menores Preços do Mercado'

    # Função principal e inicial da classe
    def __init__(self):
        Page.__init__(self)
        self.url = self.url
        self.title = self.title

    # Função que retorna o xpath do elemento a com o nome do produto na lista do carrinho
    @staticmethod
    def a_product_name_element():
        return '//a[@title="Smartphone Samsung Galaxy A10 - Preto"]'

    # Função que retorna o xpath do elemento input com a quantidade do produto no carrinho
    @staticmethod
    def input_product_quantity_element():
        return '//input[@name="productQuantity"]'

    # Função que retorna o xpath do elemento div com o preço do produto no carrinho
    @staticmethod
    def div_cart_product_price_element():
        return '//div[contains(@class, "basket-productPrice")]/p[@class="basket-productPrice"]'

    # Função que retorna o xpath do elemento span para remoção do produto do carrinho
    @staticmethod
    def span_remove_product_element():
        return '//span[text()="remover"]'

    # Função que retorna o xpath do elemento h2 informando que o carrinho está vazio
    @staticmethod
    def h2_empty_cart_element():
        return '//div/section[contains(@class, "basket-products")]/h2'

    # Função que retorna o xpath do elemento svg com opção de incremento do produto no carrinho
    @staticmethod
    def svg_plus_quantity_element():
        return '//span[contains(@class, "icon-plus")]/*[@id="icon-plus"]'
