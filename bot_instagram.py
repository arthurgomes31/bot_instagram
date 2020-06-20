from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
import datetime
import shutil
import sys
import pandas as pd




options = Options()
prefs = {'profile.default_content_setting_values.automatic_downloads': 1,
         "download.prompt_for_download": False,
         "download.default_directory": False,
         "download.directory_upgrade": True,
         "safebrowsing.enabled": True,

         }
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path=r'C:\automacao_atual_xml\chromedriver.exe', options=options)
url = 'https://nfse.recife.pe.gov.br/senhaweb/login.aspx'
driver.maximize_window()


driver.get(url)

