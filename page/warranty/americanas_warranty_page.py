from page.page import Page


# Classe da página de seleção da garantia e seguro do produto
class WarrantyPage(Page):
    url = ''
    title = 'Americanas'

    # Função principal e inicial da classe
    def __init__(self):
        Page.__init__(self)
        self.url = self.url
        self.title = self.title

    # Função que retorna o xpath do elemento span com opção de não garantia estendida do produto
    @staticmethod
    def span_no_warranty_element():
        return '//span[text()="Sem Garantia Estendida"]'

    # Função que retorna o xpath do elemento span com opção de não seguro do produto
    @staticmethod
    def span_no_safe_element():
        return '//span[text()="Sem Seguro Roubo e Furto"]'

    # Função que retorna o xpath do elemento span para continuação da compra do produto
    @staticmethod
    def span_continue_element():
        return '//span[text()="Continuar"]'
