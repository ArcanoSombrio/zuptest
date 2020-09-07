from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from drivers.runner import Runner
from drivers.browser import Browser
from utils.get_excel_values import get_excel_values
from utils.get_log_path import get_log_path
from utils.kill_driver import kill_driver
from utils.open_display import open_display
from utils.wait_time import wait_time

runner = Runner()


# Classe que possuí a abstração das funções do Selenium
class Interact:
    # Função principal e inicial da classe que realiza validações do navegador de execução para instanciar o driver
    def __init__(self, browser, headless):
        Browser.browser = browser
        Browser.headless = headless

        if headless is False:
            if Browser.browser == 'F':
                runner.firefox_driver()
            elif Browser.browser == 'C':
                runner.chrome_driver()
            else:
                raise Exception('Navegador não suportado pela plataforma de execução!')
        elif headless is True:
            open_display()
            if Browser.browser == 'F':
                runner.firefox_driver()
            elif Browser.browser == 'C':
                runner.chrome_driver()
            else:
                raise Exception('Navegador não suportado pela plataforma de execução!')
        else:
            raise Exception('Variável headless somente aceita valores True e False!')

    # Função de setup onde são realizados os instanciamentos dos drivers e abertura das aplicações
    @staticmethod
    def setup(browser, headless):
        Interact(browser, headless)
        wait_time(3)

    # Função de teardown onde são realizados os fechamentos das aplicações e finalização dos processos dos drivers
    @staticmethod
    def teardown():
        try:
            Interact.close_browser()
        except WebDriverException:
            pass

        kill_driver(Browser.browser)
        Interact.delay(2)

    # Função para abertura de URL no navegador web
    @staticmethod
    def open_url(url):
        runner.driver.get(url)

    # Função para realizar um click em algum elemento web, desktop ou mobile
    @staticmethod
    def click(selector, element):
        def click_by_css_selector():
            runner.driver.find_element_by_css_selector(element).click()

        def click_by_xpath():
            runner.driver.find_element_by_xpath(element).click()

        def click_by_id():
            runner.driver.find_element_by_id(element).click()

        def click_by_class_name():
            runner.driver.find_element_by_class_name(element).click()

        def click_by_name():
            runner.driver.find_element_by_name(element).click()

        try:
            if selector == 'css':
                click_by_css_selector()
            elif selector == 'xpath':
                click_by_xpath()
            elif selector == 'id':
                click_by_id()
            elif selector == 'class':
                click_by_class_name()
            elif selector == 'name':
                click_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Função para digitação em campo de texto web, desktop ou mobile
    @staticmethod
    def send_keys(selector, element, value):
        def send_keys_by_css_selector():
            runner.driver.find_element_by_css_selector(element).send_keys(value)

        def send_keys_by_xpath():
            runner.driver.find_element_by_xpath(element).send_keys(value)

        def send_keys_by_id():
            runner.driver.find_element_by_id(element).send_keys(value)

        def send_keys_by_class_name():
            runner.driver.find_element_by_class_name(element).send_keys(value)

        def send_keys_by_name():
            runner.driver.find_element_by_name(element).send_keys(value)

        try:
            if selector == 'css':
                send_keys_by_css_selector()
            elif selector == 'xpath':
                send_keys_by_xpath()
            elif selector == 'id':
                send_keys_by_id()
            elif selector == 'class':
                send_keys_by_class_name()
            elif selector == 'name':
                send_keys_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Função para realizar um click duplo em algum elemento web, desktop ou mobile
    @staticmethod
    def double_click(selector, element):
        action = ActionChains(runner.driver)

        def double_click_by_css_selector():
            action.double_click(runner.driver.find_element_by_css_selector(element))

        def double_click_by_xpath():
            action.double_click(runner.driver.find_element_by_xpath(element))

        def double_click_by_id():
            action.double_click(runner.driver.find_element_by_id(element))

        def double_click_by_class_name():
            action.double_click(runner.driver.find_element_by_class_name(element))

        def double_click_by_name():
            action.double_click(runner.driver.find_element_by_name(element))

        try:
            if selector == 'css':
                double_click_by_css_selector()
            elif selector == 'xpath':
                double_click_by_xpath()
            elif selector == 'id':
                double_click_by_id()
            elif selector == 'class':
                double_click_by_class_name()
            elif selector == 'name':
                double_click_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

        action.perform()
        action.reset_actions()

    # Função para aguardar algum elemento web, desktop ou mobile ficar visível
    @staticmethod
    def wait_visible_element(selector, time_wait, element):
        def wait_visible_element_by_css_selector():
            WebDriverWait(runner.driver, time_wait).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, element)))

        def wait_visible_element_by_xpath():
            WebDriverWait(runner.driver, float(time_wait)).until(
                ec.visibility_of_element_located((By.XPATH, str(element))))

        def wait_visible_element_by_id():
            WebDriverWait(runner.driver, float(time_wait)).until(
                ec.visibility_of_element_located((By.ID, str(element))))

        def wait_visible_element_by_class_name():
            WebDriverWait(runner.driver, float(time_wait)).until(
                ec.visibility_of_element_located((By.CLASS_NAME, str(element))))

        def wait_visible_element_by_name():
            WebDriverWait(runner.driver, float(time_wait)).until(
                ec.visibility_of_element_located((By.NAME, str(element))))

        try:
            if selector == 'css':
                wait_visible_element_by_css_selector()
            elif selector == 'xpath':
                wait_visible_element_by_xpath()
            elif selector == 'id':
                wait_visible_element_by_id()
            elif selector == 'class':
                wait_visible_element_by_class_name()
            elif selector == 'name':
                wait_visible_element_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Função para aguardar algum elemento web, desktop ou mobile ficar presente
    @staticmethod
    def wait_presence_element(selector, time_wait, element):
        def wait_presence_element_by_css_selector():
            WebDriverWait(runner.driver, time_wait).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, element)))

        def wait_presence_element_by_xpath():
            WebDriverWait(runner.driver, time_wait).until(
                ec.presence_of_element_located((By.XPATH, element)))

        def wait_presence_element_by_id():
            WebDriverWait(runner.driver, time_wait).until(
                ec.presence_of_element_located((By.ID, element)))

        def wait_presence_element_by_class_name():
            WebDriverWait(runner.driver, time_wait).until(
                ec.presence_of_element_located((By.CLASS_NAME, element)))

        def wait_presence_element_by_name():
            WebDriverWait(runner.driver, time_wait).until(
                ec.presence_of_element_located((By.NAME, element)))

        try:
            if selector == 'css':
                wait_presence_element_by_css_selector()
            elif selector == 'xpath':
                wait_presence_element_by_xpath()
            elif selector == 'id':
                wait_presence_element_by_id()
            elif selector == 'class':
                wait_presence_element_by_class_name()
            elif selector == 'name':
                wait_presence_element_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Função para aguardar a não presença algum elemento web, desktop ou mobile
    @staticmethod
    def wait_element_not_present(selector, time_wait, element):
        def wait_element_not_present_by_css_selector():
            WebDriverWait(runner.driver, time_wait).until(
                ec.invisibility_of_element_located((By.CSS_SELECTOR, element)))

        def wait_element_not_present_by_xpath():
            WebDriverWait(runner.driver, time_wait).until(
                ec.invisibility_of_element_located((By.XPATH, element)))

        def wait_element_not_present_by_id():
            WebDriverWait(runner.driver, time_wait).until(
                ec.invisibility_of_element_located((By.ID, element)))

        def wait_element_not_present_by_class_name():
            WebDriverWait(runner.driver, time_wait).until(
                ec.invisibility_of_element_located((By.CLASS_NAME, element)))

        def wait_element_not_present_by_name():
            WebDriverWait(runner.driver, time_wait).until(
                ec.invisibility_of_element_located((By.NAME, element)))

        try:
            if selector == 'css':
                wait_element_not_present_by_css_selector()
            elif selector == 'xpath':
                wait_element_not_present_by_xpath()
            elif selector == 'id':
                wait_element_not_present_by_id()
            elif selector == 'class':
                wait_element_not_present_by_class_name()
            elif selector == 'name':
                wait_element_not_present_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Função para capturar um texto de algum elemento de input text web, desktop ou mobile
    @staticmethod
    def get_text(selector, element):
        def get_text_by_css_selector():
            return runner.driver.find_element_by_css_selector(element).text

        def get_text_by_xpath():
            return runner.driver.find_element_by_xpath(element).text

        def get_text_by_id():
            return runner.driver.find_element_by_id(element).text

        def get_text_by_class_name():
            return runner.driver.find_element_by_class_name(element).text

        def get_text_by_name():
            return runner.driver.find_element_by_name(element).text

        try:
            if selector == 'css':
                get_text_by_css_selector()
            elif selector == 'xpath':
                get_text_by_xpath()
            elif selector == 'id':
                get_text_by_id()
            elif selector == 'class':
                get_text_by_class_name()
            elif selector == 'name':
                get_text_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Função para limpar o texto de algum elemento de input text web, desktop ou mobile
    @staticmethod
    def clear_text(selector, element):
        def clear_text_by_css_selector():
            runner.driver.find_element_by_css_selector(element).clear()

        def clear_text_by_xpath():
            runner.driver.find_element_by_xpath(element).clear()

        def clear_text_by_id():
            runner.driver.find_element_by_id(element).clear()

        def clear_text_by_class_name():
            runner.driver.find_element_by_class_name(element).clear()

        def clear_text_by_name():
            runner.driver.find_element_by_name(element).clear()

        try:
            if selector == 'css':
                clear_text_by_css_selector()
            elif selector == 'xpath':
                clear_text_by_xpath()
            elif selector == 'id':
                clear_text_by_id()
            elif selector == 'class':
                clear_text_by_class_name()
            elif selector == 'name':
                clear_text_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Função para posicionar o mouse em cima de algum elemento web, desktop ou mobile
    @staticmethod
    def mouse_over(selector, element):
        action = ActionChains(runner.driver)

        def mouse_over_by_css_selector():
            action.move_to_element(runner.driver.find_element_by_css_selector(element)).perform()

        def mouse_over_by_xpath():
            action.move_to_element(runner.driver.find_element_by_xpath(element)).perform()

        def mouse_over_by_id():
            action.move_to_element(runner.driver.find_element_by_id(element)).perform()

        def mouse_over_by_class_name():
            action.move_to_element(runner.driver.find_element_by_class_name(element)).perform()

        def mouse_over_by_name():
            action.move_to_element(runner.driver.find_element_by_name(element)).perform()

        try:
            if selector == 'css':
                mouse_over_by_css_selector()
            elif selector == 'xpath':
                mouse_over_by_xpath()
            elif selector == 'id':
                mouse_over_by_id()
            elif selector == 'class':
                mouse_over_by_class_name()
            elif selector == 'name':
                mouse_over_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

        action.reset_actions()

    # Função para capturar o valor de atributos de algum elemento web, desktop ou mobile
    @staticmethod
    def get_attribute(selector, element, attribute):
        def get_attribute_by_css_selector():
            return runner.driver.find_element_by_css_selector(element).get_attribute(attribute)

        def get_attribute_by_xpath():
            return runner.driver.find_element_by_xpath(element).get_attribute(attribute)

        def get_attribute_by_id():
            return runner.driver.find_element_by_id(element).get_attribute(attribute)

        def get_attribute_by_class_name():
            return runner.driver.find_element_by_class_name(element).get_attribute(attribute)

        def get_attribute_by_name():
            return runner.driver.find_element_by_name(element).get_attribute(attribute)

        try:
            if selector == 'css':
                get_attribute_by_css_selector()
            elif selector == 'xpath':
                get_attribute_by_xpath()
            elif selector == 'id':
                get_attribute_by_id()
            elif selector == 'class':
                get_attribute_by_class_name()
            elif selector == 'name':
                get_attribute_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Função que realiza um delay entre as ações nos testes
    @staticmethod
    def delay(time_seconds):
        wait_time(time_seconds)

    # Função que utiliza o driver para realizar uma espera
    @staticmethod
    def implicity_wait(wait_time):
        runner.driver.implicitly_wait(wait_time)

    # Função que executa um comando JavaScript no console do navegador web
    @staticmethod
    def execute_javascript(script):
        runner.driver.execute_script(script=script)

    # Função que realiza um refresh na página web
    @staticmethod
    def refresh():
        runner.driver.refresh()

    # Função que captura a url atual que o navegador web se encontra
    @staticmethod
    def get_url():
        return runner.driver.current_url()

    # Função que captura o título da página web
    @staticmethod
    def get_title():
        return runner.driver.title

    # Função que realiza uma captura de tela
    @staticmethod
    def get_screenshot():
        runner.driver.save_screenshot(get_log_path(True, Browser.browser))

    # Função que fecha o navegador web ou aplicação desktop
    @staticmethod
    def close_browser():
        runner.driver.close()

    # Função que realiza a chamada de verificação de existência de um arquivo ou pasta
    @staticmethod
    def get_excel(sheet, row, column):
        return get_excel_values(sheet, row, column)
