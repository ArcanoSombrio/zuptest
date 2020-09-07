from page.page import Page


# Classe da página de listagem dos produtos filtrados
class SmartphonePage(Page):
    url = ''
    title = 'Celulares e Smartphones em Promoção nas americanas'

    # Função principal e inicial da classe
    def __init__(self):
        Page.__init__(self)
        self.url = self.url
        self.title = self.title

    # Função que retorna o xpath do elemento span do checkbox de filtro samsung
    @staticmethod
    def span_samsung_element():
        return '//a/span[text()="samsung"]'

    # Função que retorna o xpath do elemento div do primeiro produto exibido na lista de cards
    @staticmethod
    def div_first_product_element():
        return '(//div[contains(@class, "product-grid-item")])[1]'
