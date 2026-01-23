# 4-Gewinnt
#What to do: 
Testfall 1 

Testfall-ID: VG-001

Vorbedingungen:

1. Eingabe Testen 
=> Buchstabe eingeben ->Fehlermeldung -> erneute Eingabe

=> 0 oder 8 eingeben -> Fehlermeldung -> erneute Eingabe

=> 1-7 eingeben

Erwartetes Ergebnis:

-> wird erkannt ob Spalte voll ist 

==============================================================================================

Testfall 2

Testfall-ID: VG-002

Vorbedingungen:

das Spiel muss gestartet sein. 

6x nacheinander in einer Reihe eingeben

Erwartetes Ergebnis:

wo landet der Stein? 





===============================================================================================

Testfall 3

Testfall-ID: VG-003

Testbeschreibung: Überprüfen ob ein Spieler gewonnen hat.

Vorbedingungen:

Das Spiel ist gestartet.

Spieler 1 und Spieler 2 haben bereits mehrere Spielzüge vollzogen. 

Prüfen ob 4 gleiche Farben in einer Reihe sind:

Vertikal, Horizontal, Diagonal

Ja: Der Spieler mit den 4 gleichen Farben in einer Reihe (Vertikal, Horizontal, Diagonal)
hat gewonnen.

Erwartetes Ergebnis:

	Das Spiel ist beendet, erneut spielen? 

	Nein: Das Spiel wird fortgesetzt oder es ergibt sich ein Unentschieden.

Bei Unentschieden folgt Testfall-ID: VG-004. 

=====================================================================================================


Testfall: 4: 

Testfall-ID: VG-004

Testbeschreibung: Überprüfen ob es ein Unentschieden ist.

Vorbedingungen:
Das Spiel ist gestartet.

Spieler 1 und Spieler 2 haben bereits mehrere Spielzüge vollzogen. 

Prüfen ob das Spielfeld voll ist (Vertikal, Horizontal, Diagonal)

Erwartetes Ergebnis:

Ja: Wenn es voll ist dann Unentschieden, erneut spielen?

Nein: Spiel wird fortgesetzt.  