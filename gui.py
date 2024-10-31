import tkinter as tk
from tkinter import ttk
from zeit import init
from zeit import berechnen
from writeCSV import erstelle_oder_oeffne_woechentliche_csv, lade_woechentliche_csv
from zeit import *

def mainFun():
    window = tk.Tk()
    window.title("Zeitmesser")
    window.geometry("1200x700")

    datum_label = tk.Label(window, font=("Arial", 17), text="")
    zeitGekommen_label = tk.Label(window, text="Gekommen um (HH:MM):")
    zeitGekommen_entry = tk.Entry(window, width=15, font=("Arial", 17), justify=tk.CENTER)

    zeitGegangen_label = tk.Label(window, text="Gegangen um (HH:MM):")
    zeitGegangen_entry = tk.Entry(window, width=15, font=("Arial", 17), justify=tk.CENTER)

    zeitPause_label = tk.Label(window, text="Pause (HH:MM):")
    zeitPause_entry = tk.Entry(window, width=15, font=("Arial", 17), justify=tk.CENTER)

    differenz_label = tk.Label(window, font=("Arial", 17), text="")

    berechnen_button = tk.Button(window, text="Berechnen", command=lambda: berechnen(zeitGekommen_entry, zeitGegangen_entry, zeitPause_entry, differenz_label))

    writeCSV_button = tk.Button(window, text="Abspeichern", command=lambda: (erstelle_oder_oeffne_woechentliche_csv(zeitGekommen_entry, zeitGegangen_entry, zeitPause_entry, date), aktualisiere_treeview(),lade_woechentliche_csv()), padx=1, pady=1)

    # treeview für CSV-Daten
    treeViewCSV = ttk.Treeview(window, columns=('Datum', 'Uhrzeit gekommen', 'Uhrzeit gegangen', 'Pause', 'Gesamtzeit'), show='headings')
    treeViewCSV.heading('Datum', text='Datum')
    treeViewCSV.heading('Uhrzeit gekommen', text='Uhrzeit gekommen')
    treeViewCSV.heading('Uhrzeit gegangen', text='Uhrzeit gegangen')
    treeViewCSV.heading('Pause', text='Pause')
    treeViewCSV.heading('Gesamtzeit', text='Gesamtzeit')
 
    # csv daten aktuelle woche
    daten = lade_woechentliche_csv()
    for row in daten:
        treeViewCSV.insert('', 'end', values=row)

    # aktualisiere treeview
    def aktualisiere_treeview():
        # Zuerst alle vorhandenen Einträge löschen
        for row in treeViewCSV.get_children():
            treeViewCSV.delete(row)

        daten = lade_woechentliche_csv()
        for row in daten:
            treeViewCSV.insert('', 'end', values=row)        

    init(datum_label)

    datum_label.pack(pady=8)
    zeitGekommen_label.pack(pady=8)
    zeitGekommen_entry.pack(pady=8)
    zeitGegangen_label.pack(pady=8)
    zeitGegangen_entry.pack(pady=8)
    zeitPause_label.pack(pady=8)
    zeitPause_entry.pack(pady=8)
    differenz_label.pack(pady=8)
    berechnen_button.pack(pady=8)
    writeCSV_button.pack(pady=8)
    treeViewCSV.pack(fill='both', expand=True)

    window.mainloop()