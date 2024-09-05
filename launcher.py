from notify import Bildirim as bil
from web import Web as w
from main import Window,Renk

web = w()

renk = Renk()
renk_paleti = renk.renkPaleti1
window = Window(web,renk_paleti)
window.mainloop()
