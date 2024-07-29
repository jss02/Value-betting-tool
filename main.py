import os
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Install chrome driver in current directory
    os.environ['WEB_DRIVER_MANAGER_CACHE_DIR'] = os.getcwd()
    ChromeDriverManager().install()

