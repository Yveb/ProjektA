import tkinter as tk


class Fenster:
    # Fenstermodalitäten
    
    def Create(
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
        fenster = tk.Tk()
        fenster.geometry(f"{fensterBreite}x{fensterHoehe}")
        fenster.title(fensterTitel)
        fenster.configure(background=fensterHintergrundFarbe)
        fenster.resizable(False, False)

        # FensterInhalt(widgets)
        #knopf
        
        knopf = tk.Button(fenster)
        knopf.configure(background=knopfFarbe, text="Touch Me", foreground=schriftFarben)
        
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
