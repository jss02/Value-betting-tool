import os
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Install chrome driver in current directory
    os.environ['WDM_LOCAL'] = '1'
    ChromeDriverManager().install()

if __name__ == '__main__':
    main() 