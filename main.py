from tkinter import *
from web import Web

class Window(Tk):
    def __init__(self,web : Web,renkPaleti : dict):
        super().__init__()
        arka_plan = renkPaleti["Koyu Mavi"]
        daha_acik = renkPaleti["Daha Açık (Koyu Mavi)"]
        text = renkPaleti["Daha açık"]
        self.isStartedChrome = False

        self.web = web
        self.geometry("500x500")
        self.title("PyAssistant")
        self.config(padx=10,background=arka_plan)

        getUrlFrame = Frame(self,width=500,height=100,background=arka_plan)
        getUrlFrame.place(y = 0,x = 10)

        self.getWebUrlButton = Button(master=getUrlFrame,text="Git",command=self.getWebUrlButtonClicked,background=daha_acik,foreground="#EAF1F7",width=5,font=("Times New Roman",12))
        self.getWebUrlButton.place(y = 5,x = 320)

        self.getWebUrlEntry = Entry(master=getUrlFrame,width=50,background=daha_acik,foreground=text)
        self.getWebUrlEntry.place(y=10,x = 5)

        self.youtubeButton = Button(master=getUrlFrame,text="Youtube",font=("Arial",13),background=daha_acik,foreground=text,command=self.youtubeButtonClicked)
        self.youtubeButton.place(y = 40, x = 20)

        self.instaButton = Button(master=getUrlFrame,text="İnstagram", font=("Arial", 13), background=daha_acik, foreground=text,command=self.instaButtonClicked)
        self.instaButton.place(y = 40, x = 100)



        self.searchInput = Entry(background=daha_acik,foreground=text,width=40)
        self.searchInput.place(y = 80, x = 13)

        self.searchButton = Button(background=daha_acik,foreground=text,text="Ara",width=5,font=("Times New Roman",12),command=self.searchButtonCommand)
        self.searchButton.place(y = 75, x = 283)


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

    def searchButtonCommand(self):
        if not self.isStartedChrome:
            self.web.startChrome()
            self.isStartedChrome = True
        if self.web.isPageOpen:
            self.web.newTab()
        self.web.searchGoogle(self.searchInput.get())

class Renk:
    def __init__(self):
        #334F70 Koyu Mavi
        #6E98BA Daha Açık
        #A6C4E0 Beyazımsı
        #C5D7ED Grimsi
        #EAF1F7 Daha açık
        self.renkPaleti1 = {
            "Koyu Mavi": "#334F70",
            "Daha Açık (Koyu Mavi)" : "#6E98BA",
            "Beyazımsı" : "#A6C4E0",
            "Grimsi" : "#C5D7ED",
            "Daha açık" : "#EAF1F7"
        }