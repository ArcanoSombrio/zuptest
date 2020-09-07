from page.page import Page


# Classe da página do produto selecionado
class ProductPage(Page):
    url = ''
    title = 'Smartphone Samsung Galaxy A10 32GB Dual Chip Android 9.0 Tela 6.2" Octa-Core 4G Câmera 13MP - Preto nas americanas'

    # Função principal e inicial da classe
    def __init__(self):
        Page.__init__(self)
        self.url = self.url
        self.title = self.title

    # Função que retorna o xpath do elemento span com o valor do produto
    @staticmethod
    def span_product_price_element():
        return '//div/span[contains(@class, "price__SalesPrice")]'

    # Função que retorna o xpath do elemento h1 com o nome do produto
    @staticmethod
    def h1_product_name_element():
        return '//h1[@id="product-name-default"]'

    # Função que retorna o xpath do elemento span com o código do produto
    @staticmethod
    def span_product_code_element():
        return '//div[contains(@class, "product-header")]/span[contains(@class, "product-header")]'

    # Função que retorna o xpath do elemento span para compra do produto
    @staticmethod
    def span_buy_product_element():
        return '//span[text()="comprar"]'
