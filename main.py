from tkinter import *
from web import Web

class Window(Tk):
    def __init__(self,web : Web):
        super().__init__()

        self.isStartedChrome = False

        self.web = web
        self.geometry("500x500")
        self.title("PyAssistant")
        self.config(padx=20,background="#334F70")
        #334F70 Koyu Mavi
        #6E98BA Daha Açık
        #A6C4E0 Beyazımsı
        #C5D7ED Grimsi
        #EAF1F7 Daha açık
        self.getWebUrlButton = Button(text="Git",command=self.getWebUrlButtonClicked,background="#6E98BA",foreground="#EAF1F7",width=5,font=("Times New Roman",12))
        self.getWebUrlButton.grid(row = 1,column = 2,padx=(10,0))

        self.getWebUrlEntry = Entry(width=50,background="#6E98BA",foreground="#EAF1F7")
        self.getWebUrlEntry.grid(row = 1, column= 1)

        self.youtubeButton = Button(text="Youtube",font=("Arial",13),background="#6E98BA",foreground="#EAF1F7",command=self.youtubeButtonClicked)
        self.youtubeButton.grid(row = 2,column = 1,sticky ="W")

        self.instaButton = Button(text="İnstagram", font=("Arial", 13), background="#6E98BA", foreground="#EAF1F7",command=self.instaButtonClicked)
        self.instaButton.grid(row=2, column=1, sticky="E")

    def getWebUrlButtonClicked(self):
        url = self.getWebUrlEntry.get()
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        if not self.isStartedChrome:
            self.web.startChrome()
            self.isStartedChrome = True
        if self.web.isPageOpen:
            self.web.newTab()
        self.web.get(url)

    def youtubeButtonClicked(self):
        if not self.isStartedChrome:
            self.web.startChrome()
            self.isStartedChrome = True
        if self.web.isPageOpen:
            self.web.newTab()
        self.web.get("https://youtube.com")

    def instaButtonClicked(self):
        if not self.isStartedChrome:
            self.web.startChrome()
            self.isStartedChrome = True
        if self.web.isPageOpen:
            self.web.newTab()
        self.web.get("https://instagram.com")


    @staticmethod
    def rgb_to_hex(rgb: tuple):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])