import sys
from webdrivermanager import ChromeDriverManager
from ssl_handler import no_ssl_verification

def manage_webdriver():
    """
    Метод для загрузки, установки и добавления в PYTHONPATH вебдрайвера для работы с selenium
    """
    cdm = ChromeDriverManager()

    with no_ssl_verification():

        _, symlink = cdm.download_and_install()

    sys.path.insert(0, symlink)