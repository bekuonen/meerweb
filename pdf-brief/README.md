# PDF-Briefe für Vorstand und Komitee

Vier ein- bis zweiseitige PDF-Zusammenfassungen — je eine pro Zielgruppe —
im Stil der Website (schwarz/weiss/beige, Orange als Akzent).

## Dateien

- `build.py` — Build-Skript, enthält auch alle Inhalte (Pakete, Richtpreise, Ablauf, Kontakt)
- `style.css` — Layout und Typografie, angelehnt an `static/css/main.css`
- Ausgabe: `static/pdf/meerweb-*.pdf` (werden von Hugo unverändert mitveröffentlicht)

## Neu bauen (z. B. nach Preisänderung)

    cd pdf-brief
    pip install weasyprint        # einmalig
    python3 build.py

Datum im Footer wird automatisch auf das Build-Datum gesetzt.
Versionsnummer bei inhaltlichen Änderungen in `build.py` (VERSION) erhöhen.

## Preise ändern

Alle Preise und Leistungslisten stehen in `build.py` in den Blöcken
`RICHTPREISE` und `DATEN`. Diese müssen mit `content/angebot/_index.md`
übereinstimmen — bei Änderungen beide Stellen anpassen und neu bauen.

## Hinweis

Sobald eine Telefonnummer für das Erstgespräch feststeht, im
`KONTAKT`-Block in build.py eintragen und neu bauen.
