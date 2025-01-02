import tkinter as tk 

# Fenstermodalitäten
fensterBreite=450
fensterHoehe=450
fensterHintergrundFarbe="#FFC7EF"
schriftFarben="#000000"
fensterTitel="ProjektA"
knopfFarbe="#CB0794"
knopfBreite=130
knopfHoehe=50


# Fenstererstellung(init)
fenster = tk.Tk()
fenster.geometry(f"{fensterBreite}x{fensterHoehe}")
fenster.title(fensterTitel)
fenster.configure(background=fensterHintergrundFarbe)

# FensterInhalt(widgets)
knopf = tk.Button(fenster)
knopf.configure(background=knopfFarbe, text="Touch Me", foreground=schriftFarben)
knopf.place(width=knopfBreite,height=knopfHoehe,x=fensterBreite/2, y=fensterHoehe/2,anchor="center")
fenster.mainloop()
