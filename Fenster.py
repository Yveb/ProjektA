import tkinter as tk
from Datei import Datei

class Fenster:
    # Fenstermodalitäten
    
    def Create(
        fensterBreite = 450,
        fensterHoehe = 450,
        fensterHintergrundFarbe = "#ffffff",
        schriftFarben = "#000000",
        fensterTitel = "ProjektA",
        knopfFarbe = "#bfefff",
        knopfBreite = 130,
        knopfHoehe = 50,
        eintragsfeldBreite = 130,
        eintragsfeldHoehe = 30,
        eintragsfeldHintergrundFarbe = "#c6e2ff"):
        
        # Fenstererstellung(init)
        fenster = tk.Tk()
        fenster.geometry(f"{fensterBreite}x{fensterHoehe}")
        fenster.title(fensterTitel)
        fenster.configure(background=fensterHintergrundFarbe)
        fenster.resizable(False, False)

        # Funktionen definieren
        def meine_aktion():
            eingabe = eintragsfeld.get()
            if eingabe.strip():
                desktopPfad = Datei.GetDesktopPfad()
                Datei.Create(desktopPfad, eingabe) 
                print(f"Datei'{eingabe}' wurde erstellt auf:{desktopPfad}")
            else:
                print("Bitte einen Dateinamen eingeben")
        # FensterInhalt(widgets) 
        #knopf
        
        knopf = tk.Button(fenster)
        knopf.configure(background=knopfFarbe, text="Datei erstellen", command=meine_aktion, foreground=schriftFarben)
        
        knopf.place(width=knopfBreite,
                    height=knopfHoehe,
                    x=fensterBreite/2,
                    y=fensterHoehe/2,
                    anchor="center")
        
        #eintragsfeld
        eintragsfeld = tk.Entry(fenster)
        eintragsfeld.configure(
                    background=eintragsfeldHintergrundFarbe,
                    foreground=schriftFarben)
        
        eintragsfeld.place(width=eintragsfeldBreite,
                    height=eintragsfeldHoehe,
                    x=fensterBreite/2,
                    y=fensterHoehe/2-60, 
                    anchor="center")
          
      
        return fenster
    
    def Run(fenster): 
         fenster.mainloop()
