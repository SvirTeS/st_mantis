from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
#from fixture.soap import SoapHelper
from fixture.james import JamesHelper


class Application:

    def __init__(self, browser, config):
        if browser == 'chrome':
            self.wd = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe')
        #elif browser == 'firefox':
            #self.wd = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        #elif browser == 'safari':
            #self.wd = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        #self.soap = SoapHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
