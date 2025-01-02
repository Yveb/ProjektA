import tkinter as tk 

# Fenstermodalitäten
fensterBreite=450
fensterHoehe=450
fensterHintergrundFarbe="#FFC7EF"
fensterSchriftFarbe="#000000"
fensterTitel="ProjektA"

# Fenstererstellung(init)
fenster = tk.Tk()
fenster.geometry(f"{fensterBreite}x{fensterHoehe}")
fenster.title(fensterTitel)
fenster.configure(background=fensterHintergrundFarbe)
fenster.mainloop()



