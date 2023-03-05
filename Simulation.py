import matplotlib.pyplot as plt
import math
import seaborn as sns


sns.set_theme()
sns.set_context("notebook", font_scale=1.25)

# Leistung erste Anlage
grundleistung = 36000

# Zielleistung
zielleistung = 3712385000

# erstes Jahr
y0 = 2024

# letztes Jahr
ye = 2050

# Anzahl von Zweijahresschritten
jahresschritte = int(ye - y0) // 2 + 1

# Maximal erlaubte Schleifen zur Ermittlung der richtigen Leistungsteigerung
max_loops = 30

# Maximale Anzahl neuer Anlagen
# Hier kannste die maximale Anzahl neuer Anlagen einstellen
max_neue_anlagen = 10

# Erstelle Liste mit allen Jahren
year=[y0 + 2 * i for i in range(jahresschritte)]

# Erstelle Liste, in der die Leistungsteigerung alle zwei Jahre fuer alle moeglichen Anzahlen an neuen Anlagen
# wird in Simulation gefuellt
leistungssteigerung = []

# Zeige Zwischenergebnisplots
# Vorsicht!
# Das sind genausoviele wie max_neue_anlagen,
# das kann dauern
# Wenn show_plots = True, dann erscheint der naechste Plot, nachdem der aktuelle geschlossen wird
# Setze max_neue_anlagen in Zeile 23 auf einen kleinen Wert, wenn Du die Plots sehen willst
show_plots = True

# Simulation
for neue_anlagen in range(1, max_neue_anlagen + 1):

    # Erstelle max_loops mit erstem Effizienswert initialisierte Listen fuer die Simulation und deren Plots
    gesamtleistung = []

    # Dieser Wert wird in der Simulation berechnet
    # Starten aber immer mit 100%
    leistungszuwachs = 2

    # Effizienzaenderungsbasis
    # Um diesen Wert wird der Leistungszuwachs entweder erhoeht oder verringert, je nachdem, wie gross der Fehler war
    # Der Wert selbst wird bei jedem Schleifendurchlauf halbiert
    aenderung_leistungszuwachs = .5 

    # Fehler der Simulation, wird, damit erste Schleife laeuft, auf irgendeinen riesigen Wert gesetz
    err = 1e20

    # Schleifenzaehler
    loop = 0

    # Solange loop < max_loops und der absolute Betrag des Fehlers groesser als 100t
    while loop < max_loops and 100 < abs(err):
        
        # Fuelle die Liste gesamtleistung mit den zweijaehrlichen Werten der berechneten Gesamtleisung aller Anlagen
        gesamtleistung.append([grundleistung])

        # Fuer jedes zweite Jahr
        for n in range(1, jahresschritte):

            # Berechne alle 14 gesamtleisungen aller Anlagen fuer die eingestellte Effizienz leistungszuwachs
            gesamtleistung[loop].append(gesamtleistung[loop][len(gesamtleistung[loop]) - 1] + grundleistung * neue_anlagen * leistungszuwachs ** n) ##
        
        # Berechne den Fehler, also die Differenz der Leistung im Jahr 2050 und der Zielleitung zielleistung
        # Wir finden die Gesamtleisung des entsprechenden loops im letzten Feld von gesamtleisung[loop] 
        err = gesamtleistung[loop][len(gesamtleistung[loop]) - 1] - zielleistung

        # Plotte die aktuellen berechneten Werte fuer alle Jahre von 2024 bis 2050
        if show_plots:
            #plt.semilogy(year, gesamtleistung[loop], label=str(loop)+ ": " + str(leistungszuwachs) + " err: " + str(err))
            plt.subplot(1, 2, 1)
            plt.semilogy(year, gesamtleistung[loop], label = str(loop) + ": leistungszuwachs: " + str(leistungszuwachs) + " err: " + str(err))
            plt.subplot(1, 2, 2)
            plt.plot(year, gesamtleistung[loop], label = str(loop) + ": leistungszuwachs: " + str(leistungszuwachs) + " err: " + str(err))

        # Falls der Fehler kleiner als Null, dann war die Leistung zu klein
        if(err < 0):
            # also erhoehe den leistungszuwachs um die aenderung_leistungszuwachs
            leistungszuwachs = leistungszuwachs + aenderung_leistungszuwachs
        else:
            # Andernfalls, falls der Fehler kleiner als Null ist, dann war die Leistung zu hoch     
            if 0 < err:
                # also erniedrige den leistungszuwachs um die aenderung_leistungszuwachs
                leistungszuwachs = leistungszuwachs - aenderung_leistungszuwachs
            else:
                # falls der Fehler gleich 0, dann halte an!
                break
        # Verringere fuer den naechsten Schleifendurchlauf den Wert, um den leistungszuwachs geaendert werden soll
        # aenderung_leistungszuwachs wird immer kleiner 0.5, 0.25, 0.125, ...
        aenderung_leistungszuwachs *= .5

        # Erhoehe den Schleidenzaehler loops um Eins
        loop = loop + 1

    # Plotte eine Legende
    if show_plots:
        #plt.subplot(1,2,1).legend()
        plt.subplot(1,2,2).legend(bbox_to_anchor=(1,1), loc="upper left")

    # Print das Ergebnis fuer die Leistungsbasis
    print(leistungszuwachs)

    # Print den eigentlichen Leistungszuwachs in Prozent: leistungszuwachs - 100%
    print(str(100 * round(leistungszuwachs - 1, 4)) + "%")

    # Merke berechnete leistungssteigerung in % fuer bestimmte Anzahl neuer Anlagen
    leistungssteigerung.append(100 * (leistungszuwachs - 1))

    # Zeige alle Plots
    if show_plots:
        plt.show()

# Plotte das finale Ergebnis    
plt.subplot(1, 1, 1)
# Plotte Effizienssteigerung pro neue Anlage fuer alle moeglichen Anzahlen neuer Anlagen von 1 bis max_neue_anlagen
neue_anlagen = [i for i in range(1, max_neue_anlagen + 1)]
plt.plot(neue_anlagen, leistungssteigerung)
plt.title("Finales Model Direct Air Capture")
plt.xlabel("Anzahl neuer Anlagen alle zwei Jahre")
plt.ylabel("Effizienssteigerung pro Anlage innerhalb zweier Jahre in %")
plt.xticks(range(0, max_neue_anlagen + 1, 2))
plt.yticks(range(int(min(leistungssteigerung) - 1), int(max(leistungssteigerung) + 2)))
plt.grid('both')
plt.show()

# Musste vllt noch mit 'pip install pandas' installieren,
# Falls Du die Erbegnisse in einer Tabelle haben willst
import pandas as pan

result = pan.DataFrame(neue_anlagen, leistungssteigerung)
print(result)