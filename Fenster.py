import tkinter as tk


class Fenster(tk.Tk):
    self.eintragsfeldText = None
    # Fenstermodalitäten    
    def super.__init__(
        self,
        eintragsfeldText = None 
        fensterBreite = 450,
        fensterHoehe = 450,
        fensterHintergrundFarbe = "#FFC7EF",
        schriftFarben = "#000000",
        fensterTitel = "ProjektA",
        knopfFarbe = "#CB0794",
        knopfBreite = 130,
        knopfHoehe = 50,
        eintragsfeldBreite = 130,
        eintragsfeldHoehe = 30,
        eintragsfeldHintergrundFarbe = "#CB0790"):
        
        # Fenstererstellung(init)
        self.eintragsfeldText = eintragsfeldText
        self.geometry(f"{fensterBreite}x{fensterHoehe}")
        self.title(fensterTitel)
        self.configure(background=fensterHintergrundFarbe)
        self.resizable(False, False)

        # FensterInhalt(widgets)
        #knopf
        
        knopf = tk.Button(self)
        knopf.configure(background=knopfFarbe, text="Touch Me", foreground=schriftFarben)
        
        knopf.place(width=knopfBreite,
                    height=knopfHoehe,
                    x=fensterBreite/2,
                    y=fensterHoehe/2,
                    anchor="center")
        
        #eintragsfeld
        
        self.eintragsfeldText = tk.StringVar(self, "Beispiel.txt")
        eintragsfeld = tk.Entry(self, textvariable= self.eintragsfeldText)
        eintragsfeld.configure(
                    background=eintragsfeldHintergrundFarbe,
                    foreground=schriftFarben)
        
        eintragsfeld.place(width=eintragsfeldBreite,
                    height=eintragsfeldHoehe,
                    x=fensterBreite/2,
                    y=fensterHoehe/2-60, 
                    anchor="center")
    
        
        return self
   
    