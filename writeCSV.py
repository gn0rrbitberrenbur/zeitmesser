import csv
import os
from datetime import datetime, timedelta
from zeit import berechne_uhrzeit_differenz_fstring

def erstelle_oder_oeffne_woechentliche_csv(zeitGekommen_entry, zeitGegangen_entry, zeitPause_entry, date, dateiname_prefix='wochenbericht'):

    heute = datetime.now()

    erster_tag_der_woche = heute - timedelta(days=heute.weekday())

    # erstelle dateinamen
    dateiname = f"{dateiname_prefix}_{erster_tag_der_woche.strftime('%d-%m-%Y')}_bis_{(erster_tag_der_woche + timedelta(days=6)).strftime('%d-%m-%Y')}.csv"

    # check ob datei schon existiert
    file_exists = os.path.isfile(dateiname)

    # erstelle/oeffne csv
    with open(dateiname, mode='a', newline='') as csv_file:  # 'a' für Anhängen
        writer = csv.writer(csv_file)

        # wenn erstellen dann schreibe die kopfzeile
        if not file_exists:
            writer.writerow(['Datum', 'Uhrzeit gekommen', 'Uhrzeit gegangen', 'Pause', 'Gesamtzeit'])  # Kopfzeile

        # variablen aus zeit.py holen
        date = date
        gesamtzeit = berechne_uhrzeit_differenz_fstring(zeitGekommen_entry, zeitGegangen_entry, zeitPause_entry)
        uhrzeit_kommen = zeitGekommen_entry.get()
        uhrzeit_gegangen = zeitGegangen_entry.get()
        pause = zeitPause_entry.get()

     
        # die variablen in eine zeile in csv schreiben
        writer.writerow([date, uhrzeit_kommen, uhrzeit_gegangen, pause, gesamtzeit])

    print(f"CSV-Datei '{dateiname}' wurde erstellt oder aktualisiert.")

def lade_woechentliche_csv(dateiname_prefix='wochenbericht'):
    heute = datetime.now()
    erster_tag_der_woche = heute - timedelta(days=heute.weekday())
    dateiname = f"{dateiname_prefix}_{erster_tag_der_woche.strftime('%d-%m-%Y')}_bis_{(erster_tag_der_woche + timedelta(days=6)).strftime('%d-%m-%Y')}.csv"

    daten = []
    if os.path.isfile(dateiname):
        with open(dateiname, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Überspringe die Kopfzeile
            for row in reader:
                daten.append(row)
    return daten

