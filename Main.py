from Fenster import * 
from Datei import *


hauptfenster = Fenster.Create()
Datei.Create(Datei.GetDesktopPfad(), "hallo.exe")


Fenster.Run(hauptfenster)