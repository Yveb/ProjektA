import os

class Datei:
    def GetDesktopPfad(): 
        
        desktopPfad = os.path.join(os.path.expanduser("~"), "Desktop") #erstellt den vollständigen Pfad zum Desktop-Ordner.
        return desktopPfad #gibt diesen Pfad zurück, damit du ihn außerhalb der Methode nutzen kannst (Main.py)
    
    def Create(speicherPfad, dateiName = "demoText.txt"): #Diese Methode erstellt eine leere Datei an einem bestimmten Speicherpfad.
        dateiPfad = os.path.join(speicherPfad, dateiName) #Die Methode os.path.join kombiniert speicherPfad und dateiName zu einem vollständigen Dateipfad und speichert ihn in dateiPfad

       
        with open(dateiPfad, "w") as datei: 
            pass 
           