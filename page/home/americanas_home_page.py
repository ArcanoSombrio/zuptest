from page.page import Page


# Classe da página principal do portal americanas
class HomePage(Page):
    url = 'https://www.americanas.com.br/?opn=AFLACOM&epar=afilio'
    title = 'Americanas - Tudo. A toda hora. Em qualquer lugar.'

    # Função principal e inicial da classe
    def __init__(self):
        Page.__init__(self)
        self.url = self.url
        self.title = self.title

    # Função que retorna o xpath do elemento input do campo de busca da página home
    @staticmethod
    def input_search_element():
        return '//input[@id="h_search-input"]'

    # Função que retorna o xpath do elemento button do campo de busca da página home
    @staticmethod
    def button_search_element():
        return '//button[@id="h_search-btn"]'

    # Função que retorna o xpath do elemento div da mensagem do lgpd
    @staticmethod
    def div_lgpd_element():
        return '//div[@id="footer-lgpd"]'

    # Função que retorna o xpath do elemento button para confirmação do lgpd
    @staticmethod
    def button_confirm_lgpd():
        return '//button[@id="lgpd-accept"]'

    # Função que retorna o xpath do elemento div para acesso ao login
    @staticmethod
    def div_user_element():
        return '//div[@id="h_user"]'

    # Função que retorna o xpath do elemento a para acesso a página de login
    @staticmethod
    def a_signin_element():
        return '//a[@id="h_usr-signin"]'

    # Função que retorna o xpath do elemento li para acesso a categoria celulares
    @staticmethod
    def li_phone_element():
        return '//div[@id="h_destaques"]/ul/li[1]'
