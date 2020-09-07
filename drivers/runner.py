from selenium import webdriver as selenium_driver
from utils.get_driver_folder import geckodriver, chromedriver


# Classe que realiza a instância dos drivers
class Runner:
    driver = None

    # Função principal e inicial da classe que leva o driver
    def __init__(self):
        self.driver = self.driver

    # Função que realiza o deploy do chromedriver a partir do executável
    def chrome_driver(self):
        chrome_options = selenium_driver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        self.driver = selenium_driver.Chrome(
            chromedriver(),
            chrome_options=chrome_options
        )
        self.driver.maximize_window()

    # Função que realiza o deploy do geckodriver a partir do executável
    def firefox_driver(self):
        firefox_profile = selenium_driver.FirefoxProfile()
        firefox_profile.set_preference(
            'webdriver.load.strategy',
            'unstable'
        )
        self.driver = selenium_driver.Firefox(
            firefox_profile=firefox_profile,
            executable_path=r'' + geckodriver()
            # firefox_binary="/opt/firefox/firefox"
        )
