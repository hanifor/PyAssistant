from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class Web:
    def __init__(self):
        self.isPageOpen = False
    def get(self,link : str):
        self.driver.get(link)
        self.isPageOpen = True
    def startChrome(self):
        self.driver_path = r"C:\Users\hanif\python\PyAssistant\chromedriver.exe"

        # Mevcut bir profili kullanmak için yolunu belirle
        self.profile_path = r"C:\Users\hanif\AppData\Local\Google\Chrome\User Data"
        self.profile_name = "Default"

        # Chrome seçenekleri
        self.options = Options()
        self.options.add_argument(f"user-data-dir={self.profile_path}")
        self.options.add_argument(f"profile-directory={self.profile_name}")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

        # Chrome sürücüsünü başlat
        self.service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def newTab(self):
        # Önce pencere sayısını kontrol et
        if len(self.driver.window_handles) > 0:
            # Yeni sekme aç
            self.driver.execute_script("window.open('');")
            # Açılan yeni sekmeye geçiş yap
            self.driver.switch_to.window(self.driver.window_handles[-1])
        else:
            print("No window is currently open.")

    def searchGoogle(self,text : str):
        self.driver.get("https://www.google.com/")
        m = self.driver.find_element(By.NAME,"q")
        m.send_keys(text)
        time.sleep(0.2)
        # perform Google search with Keys.ENTER
        m.send_keys(Keys.ENTER)