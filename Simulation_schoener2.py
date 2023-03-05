import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import math
import seaborn as sns

sns.set_theme()
sns.set_context("notebook", font_scale=1.25)

ERSTES_JAHR    = 2024
LETZTES_JAHR   = 2050
JAHRESSCHRITTE = (LETZTES_JAHR - ERSTES_JAHR) // 2 + 1

# Leistung der ersten Anlage
GRUNDLEISTUNG = 36000

# Zielleistung aller Anlagen im Jahr 2050
ZIELLEISTUNG = 3712385000

JAHRE = [ERSTES_JAHR + 2 * i for i in range(JAHRESSCHRITTE)]

def simuliere_gesamtleistung_fuer_n_anlagen_mit_effizienssteigerung_e_bis_2050(n, e):
    
    letzte_leistung = GRUNDLEISTUNG

    gesamtleistung = [letzte_leistung]
    
    for jahresschritt in range(1, JAHRESSCHRITTE):

        naechste_leistung = letzte_leistung + GRUNDLEISTUNG * n * e ** jahresschritt

        gesamtleistung.append(naechste_leistung)

        letzte_leistung = naechste_leistung

    return gesamtleistung


def finde_effizienssteigerung_fuer_n_anlagen(n):

    eff = 2

    delta_eff = .5

    err = 1e20

    while 100 < abs(err):

        gesamtleistung = simuliere_gesamtleistung_fuer_n_anlagen_mit_effizienssteigerung_e_bis_2050(n, eff)

        err = gesamtleistung[len(gesamtleistung) - 1] - ZIELLEISTUNG

        if err < 0:
            eff += delta_eff
        else:
            if 0 < err:
                eff -= delta_eff
            else:
                break

        delta_eff *= .75

    return eff

# Beispiel:
ANZAHL_ANLAGEN = 5
LEISTUNGSZUWACHS = 2.039 # 1.68
# Gesamtleistungsentwicklung fuer 5 Anlagen mit ner Leistungsteigerung von 68% ~ 1.68
leistung_5_168 = simuliere_gesamtleistung_fuer_n_anlagen_mit_effizienssteigerung_e_bis_2050(ANZAHL_ANLAGEN, LEISTUNGSZUWACHS)

plt.plot(JAHRE, leistung_5_168)
# plt.plot([2024, 2050], [ZIELLEISTUNG, ZIELLEISTUNG])
plt.axhline(y = ZIELLEISTUNG, color = 'g', linestyle = '-', alpha=0.5)
plt.text(2024, 3712385000, "10% Ziel", size=20, color="g", alpha=0.5)

plt.title('Gesamtleistungsentwicklung fuer ' + str(ANZAHL_ANLAGEN) + ' Anlagen bei einer Effizienssteigerung von 103.9%' )
plt.xlabel('Jahre')
plt.ylabel('Gesamtleistung in t CO$_2$')
plt.grid('both')
plt.show()

MAXIMALE_ANZAHL_ANLAGEN = 100 # 1000
ANLAGEN = [n for n in range(1, MAXIMALE_ANZAHL_ANLAGEN + 1)]

effiziensteigerungen = [100 * (finde_effizienssteigerung_fuer_n_anlagen(n) - 1) for n in ANLAGEN] 

# Effiziens gegen Anzahl Anlagen
plt.plot(ANLAGEN, effiziensteigerungen)
plt.title('Direct Air Capture Effizienssteigerung gegen Anzahl neuer Anlagen')
plt.xlabel('Anzahl neuer Anlagen alle zwei Jahre')
plt.ylabel('Leistungssteigerung neuer Anlagen alle zwei Jahre in %')
plt.grid('both')
plt.show()