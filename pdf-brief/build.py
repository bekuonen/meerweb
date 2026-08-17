#!/usr/bin/env python3
"""
Meerweb PDF-Briefe — reproduzierbarer Build.

Erzeugt pro Zielgruppe eine ein- bis zweiseitige PDF-Zusammenfassung
im Stil der Website und legt sie unter static/pdf/ ab.

Aufruf:   python3 build.py          (aus dem Ordner pdf-brief/)
Benötigt: pip install weasyprint
Bei Preisänderungen: Werte unten in DATEN bzw. RICHTPREISE anpassen,
dann neu bauen. Datum wird automatisch gesetzt.
"""
import datetime
from pathlib import Path
from weasyprint import HTML

HIER = Path(__file__).parent
ZIEL = HIER.parent / "static" / "pdf"
DATUM = datetime.date.today().strftime("%d.%m.%Y")
VERSION = "1.0"

RICHTPREISE = [
    ("Zusätzliche Inhaltsseite über Paket hinaus", "CHF 200"),
    ("Zweite Sprache (Aufbau/Struktur)", "ab CHF 600"),
    ("Fotografie vor Ort (halber Tag)", "ab CHF 800 (externer Anbieter, Meerweb vermittelt)"),
    ("Newsletter-Anbindung (Mailchimp/CleverReach)", "ab CHF 300"),
    ("Spendenformular (RaiseNow/Payrexx)", "ab CHF 400 + Provider-Gebühren"),
    ("Rechtstexte (Impressum, DSE) durch Anwalt", "nach Aufwand, typisch CHF 400–800 (externer Anbieter)"),
    ("Domain (.ch)", "CHF 15–25 pro Jahr (externer Anbieter)"),
]

ABLAUF = [
    ("01", "Gespräch", "Wir klären, was du brauchst, wen die Website erreichen soll und welche Inhalte vorhanden sind. Das erste Gespräch ist unverbindlich."),
    ("02", "Konzept", "Ich entwickle einen konkreten Vorschlag für Struktur, Gestaltung und Inhalte. Gemeinsam prüfen und schärfen wir die Richtung."),
    ("03", "Umsetzung", "Du erhältst früh einen funktionierenden Entwurf. Rückmeldungen fliessen ein, bevor die Website fertiggestellt wird."),
    ("04", "Veröffentlichung", "Wir prüfen die Website gemeinsam. Danach veröffentliche ich sie und übergebe dir alle vereinbarten Dateien und Zugangsdaten."),
    ("05", "Betreuung (optional)", "Auf Wunsch laufende Betreuung nach dem Start — technischer Betrieb ab CHF 75 pro Monat, monatlich kündbar."),
]

KONTAKT = """
<p><strong>Bernhard Kuonen</strong> — Meerwert Kuonen, Einzelunternehmen</p>
<p>E-Mail: hallo@meerweb.ch — Antwort innerhalb von 24 Stunden</p>
<p>Telefon-Erstgespräch: Dienstag und Donnerstag, 9–12 Uhr — Terminvereinbarung per E-Mail</p>
"""

DATEN = {
    "meerweb-persoenliche-website": {
        "zielgruppe": "Für Einzelpersonen und eigene Projekte",
        "paket": "Persönliche Website",
        "preis": "CHF 2'200",
        "enthalten": [
            "Persönliches Profil mit Biografie und Tätigkeit",
            "Werte, Kompetenzen oder Schwerpunkte",
            "Bis zu 5 Inhaltsseiten",
            "Individuelle Struktur und Gestaltung",
            "Texte gemeinsam entwickelt",
            "Kontaktmöglichkeit",
            "Eine gemeinsame Korrekturrunde",
            "1 Monat technische Unterstützung nach dem Start",
        ],
    },
    "meerweb-npo-ngo": {
        "zielgruppe": "Für NPO, NGO, Vereine und Initiativen",
        "paket": "Website für NPO und NGO",
        "preis": "CHF 3'300",
        "zusatz": "10 % Rabatt für soziale und gemeinnützige Projekte",
        "enthalten": [
            "Auftrag, Werte und Ziele",
            "Projekte, Angebote oder Tätigkeitsbereiche",
            "Team, Vorstand oder verantwortliche Personen",
            "Bis zu 10 Inhaltsseiten",
            "Projektübersicht oder Bereich für aktuelle Meldungen",
            "Kontakt- und Beteiligungsmöglichkeiten",
            "Darstellung von Trägerschaft und Finanzierung",
            "Individuelle Struktur und Gestaltung",
            "Texte im Dialog entwickelt",
            "Hosting-Option Schweiz (Rechenzentrum in der Schweiz) inklusive; alternativ Standard-Hosting auf Cloudflare Pages",
            "Eine gemeinsame Korrekturrunde",
            "3 Monate technische Unterstützung nach dem Start",
        ],
    },
    "meerweb-kleinbetriebe": {
        "zielgruppe": "Für Selbständige und kleine Betriebe",
        "paket": "Website für Kleinbetriebe",
        "preis": "CHF 3'300",
        "enthalten": [
            "Vorstellung des Betriebs und seiner Arbeitsweise",
            "Leistungen und Angebote",
            "Team oder persönliche Ansprechpersonen",
            "Bis zu 10 Inhaltsseiten",
            "Referenzen, Projekte oder Bildergalerie",
            "Kontaktformular oder strukturierte Anfrage",
            "Individuelle Struktur und Gestaltung",
            "Texte gemeinsam entwickelt",
            "Grundlagen für die lokale Auffindbarkeit",
            "Eine gemeinsame Korrekturrunde",
            "3 Monate technische Unterstützung nach dem Start",
        ],
    },
    "meerweb-politische-website": {
        "zielgruppe": "Für Kandidierende, Parlamente und Exekutiven",
        "paket": "Politische Website",
        "preis": "CHF 4'500",
        "zusatz": "Einstieg möglich: Politisches Profil für CHF 2'200",
        "enthalten": [
            "Persönliches Profil mit Biografie, Motivation und Funktionen",
            "Werte und politische Schwerpunkte",
            "Bis zu 5 Themen und 10 Positionen",
            "Politische Arbeit und Resultate mit bis zu 10 Belegen",
            "Mitgliedschaften und Interessenbindungen",
            "Kontaktmöglichkeiten für Bevölkerung und Medien",
            "Eine auf die Person abgestimmte Gestaltungsrichtung",
            "Barrierearme Umsetzung nach WCAG 2.2 AA",
            "Hosting-Option Schweiz (Rechenzentrum in der Schweiz) inklusive; alternativ Standard-Hosting auf Cloudflare Pages",
            "Datenarme Umsetzung ohne externe Tracker",
            "Eine gemeinsame Korrekturrunde",
        ],
    },
}


def html_seite(d: dict) -> str:
    enthalten = "\n".join(f"<li>{e}</li>" for e in d["enthalten"])
    richt = "\n".join(f"<tr><td>{l}</td><td>{p}</td></tr>" for l, p in RICHTPREISE)
    ablauf = "\n".join(
        f'<div class="schritt"><span class="nr">{nr}</span>'
        f'<span class="titel">{t}</span> — {txt}</div>'
        for nr, t, txt in ABLAUF
    )
    zusatz = f'<p class="hinweis">{d["zusatz"]}</p>' if d.get("zusatz") else ""
    return f"""<!DOCTYPE html>
<html lang="de-CH">
<head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head>
<body>
<footer>meerweb.ch · {d['paket']} · Stand: {DATUM} · Version {VERSION}</footer>

<div class="kopf">
  <p class="label">meerweb · {d['zielgruppe']}</p>
  <h1>{d['paket']}</h1>
  <p class="preis">{d['preis']} <span>einmalig</span></p>
  {zusatz}
</div>

<section>
  <h2>Was enthalten ist</h2>
  <ul>{enthalten}</ul>
</section>

<section>
  <h2>Nicht enthalten — Richtpreise für Zusatzleistungen</h2>
  <table>
    <thead><tr><th>Zusatzleistung</th><th>Richtpreis (indikativ)</th></tr></thead>
    <tbody>{richt}</tbody>
  </table>
  <p class="hinweis">Diese Richtpreise sind Erfahrungswerte. Vor jeder externen Beauftragung wird der genaue Preis offengelegt und schriftlich bestätigt.</p>
</section>

<section>
  <h2>So läuft ein Projekt ab</h2>
  <div class="ablauf">{ablauf}</div>
</section>

<section>
  <h2>Ansprechperson</h2>
  <div class="kontakt">{KONTAKT}</div>
</section>

</body>
</html>"""


def main():
    ZIEL.mkdir(parents=True, exist_ok=True)
    for name, d in DATEN.items():
        html = html_seite(d)
        HTML(string=html, base_url=str(HIER)).write_pdf(ZIEL / f"{name}.pdf")
        print(f"gebaut: static/pdf/{name}.pdf")


if __name__ == "__main__":
    main()
