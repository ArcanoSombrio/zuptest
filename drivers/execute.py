from behave.__main__ import main as behave_main
from urllib3.exceptions import MaxRetryError

from drivers.interact import Interact
from drivers.browser import Browser
from utils.get_features_folder import get_features_folder
from utils.get_log_path import get_log_path


# Classe que realiza a execução do teste utilizando a biblioteca de BDD
class Execute:
    @staticmethod
    def start_bdd_test(stories_list):
        for story in stories_list:
            behave_main(
                [
                    get_features_folder() + story,
                    '-v',
                    '--stop',
                    '-o=%s' % get_log_path(False, Browser.browser),
                    '--summary',
                    '--logcapture',
                    '--logging-level=DEBUG',
                    '--logging-format="%(asctime) s: %(levelname) s: %(message) s"',
                    '--logging-datefmt="%d/%m/%y %I:%M:%S"'
                ]
            )
            if story == 0:
                pass
            else:
                try:
                    Interact.get_screenshot()
                except MaxRetryError:
                    pass
