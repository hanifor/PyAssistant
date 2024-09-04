from notifypy import Notify
class Bildirim(Notify):
    def __init__(self):
        super().__init__()

    def gonder(self):
        self.send()

    def setTitle(self,title:str):
        self.title = title

    def set_message(self,message : str):
        self.message = message

    def set_image(self,image_path:str):
        self.icon = image_path




