from Fenster import * 
from Datei import *


hauptfenster = Fenster()
Datei.Create(Datei.GetDesktopPfad(), hauptfenster.eintragsfeldText)

hauptfenster.mainloop()
