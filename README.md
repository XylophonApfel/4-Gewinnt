


Testfall 1

Testfall-ID: VG-001

Vorbedingungen:

Eingabe Testen => Buchstabe eingeben ->Fehlermeldung -> erneute Eingabe
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

Ja: Der Spieler mit den 4 gleichen Farben in einer Reihe (Vertikal, Horizontal, Diagonal) hat gewonnen.

Erwartetes Ergebnis:

 Das Spiel ist beendet, erneut spielen?

 Nein: Das Spiel wird fortgesetzt oder es ergibt sich ein Unentschieden.

Bei Unentschieden folgt Testfall-ID: VG-004.

=====================================================================================================

Testfall: 4:

Testfall-ID: VG-004

Testbeschreibung: Überprüfen ob es ein Unentschieden ist.

Vorbedingungen: Das Spiel ist gestartet.

Spieler 1 und Spieler 2 haben bereits mehrere Spielzüge vollzogen.

Prüfen ob das Spielfeld voll ist (Vertikal, Horizontal, Diagonal)

Erwartetes Ergebnis:

Ja: Wenn es voll ist dann Unentschieden, erneut spielen?

Nein: Spiel wird fortgesetzt.



===============================================================================
Funktionstabelle:

| Name | Beschreibung | Argument | Rückgabe |
|------|-------------|----------|----------|
| input_player | Namen der Spieler | player | None/Manuel |
| generate_board | Initialisieren des Spielfelds | Mehrdimensionale Liste/Dic | None | -> Pavlos
| move | Fragt Spieler nach Spalte |  | player, column/Manuel/Pavlos|
| check_horizontal | Prüft ob wagrecht vier in einer Reihe sind | board,player | winner/Aron |
| check_vertical | Prüft ob senkrecht vier in einer Reihe sind | board,player | winner/Aron |
| check_diagonal | Prüft ob diagonal vier in einer Reihe sind | board,player | winner/Aron | 
| Readme erstellen | beschreibt im Readme was geprüft werden muss | Non | Manuel| 
 
	
 
	
 
	
  




 
	
 
	
 
	
 
 
 