from datetime import datetime, timedelta

def getDate():
    global date
    date = datetime.today().strftime('%A %d.%m.%Y')
    return date

def writeDate(datum_label):
    datum_label.config(text=date)

def berechne_uhrzeit_differenz(zeitGekommen_entry, zeitGegangen_entry, zeitPause_entry):

    format = "%H:%M"

    start_uhrzeit = zeitGekommen_entry.get()
    end_uhrzeit = zeitGegangen_entry.get()
    pausen_zeit = zeitPause_entry.get()

    # kovertieren in datetime objekte
    start_zeit = datetime.strptime(start_uhrzeit, format)
    end_zeit = datetime.strptime(end_uhrzeit, format)

    # pausenzeit in minuten konvertieren
    if pausen_zeit:
        pause_parts = pausen_zeit.split(":")
        pause_stunden = int(pause_parts[0])
        pause_minuten = int(pause_parts[1])
        pausen_dauer = timedelta(hours=pause_stunden, minutes=pause_minuten)
    else:
        pausen_dauer = timedelta(0)  # Wenn keine Pause angegeben ist

    differenz = (end_zeit - start_zeit) - pausen_dauer

    stunden = differenz.seconds // 3600
    minuten = (differenz.seconds % 3600) // 60

    return stunden, minuten

#selbe funktion wie oben, nur returnwerte für writeCSV.py, frag nicht wieso
def berechne_uhrzeit_differenz_fstring(zeitGekommen_entry, zeitGegangen_entry, zeitPause_entry):
    format = "%H:%M"

    start_uhrzeit = zeitGekommen_entry.get()
    end_uhrzeit = zeitGegangen_entry.get()
    pausen_zeit = zeitPause_entry.get()

    start_zeit = datetime.strptime(start_uhrzeit, format)
    end_zeit = datetime.strptime(end_uhrzeit, format)

    if pausen_zeit:
        pause_parts = pausen_zeit.split(":")
        pause_stunden = int(pause_parts[0])
        pause_minuten = int(pause_parts[1])
        pausen_dauer = timedelta(hours=pause_stunden, minutes=pause_minuten)
    else:
        pausen_dauer = timedelta(0)

    differenz = (end_zeit - start_zeit) - pausen_dauer

    stunden = differenz.seconds // 3600
    minuten = (differenz.seconds % 3600) // 60
    
    differenzbetrag = (f"{stunden}:{minuten}")
    return differenzbetrag

def berechnen(zeitGekommen_entry, zeitGegangen_entry, zeitPause_entry, differenz_label):
    start_uhrzeit = zeitGekommen_entry.get()
    end_uhrzeit = zeitGegangen_entry.get()

    # check ob eingabefelder leer sind
    if not start_uhrzeit or not end_uhrzeit:
        differenz_label.config(text="Bitte Uhrzeiten eingeben!")
    else:
        stunden, minuten = berechne_uhrzeit_differenz(zeitGekommen_entry, zeitGegangen_entry, zeitPause_entry)
        differenz_label.config(text=f"Differenz: {stunden} Stunden und {minuten} Minuten.")

def init(datum_label):
    getDate()
    writeDate(datum_label=datum_label)

date = getDate()