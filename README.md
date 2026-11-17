# Saxony Radar – Vorschau / preview

**Radar der Halbleiter-Wertschöpfungskette – Sachsen.** Wöchentlicher Radar der öffentlichen Aktivitäten von Unternehmen und Instituten des sächsischen Halbleiter-Ökosystems, erstellt vom Czech National Semiconductor Cluster (CNSC) für Silicon Saxony im Rahmen der Absichtserklärung vom 12. 11. 2026.

**Semiconductor Value Chain Radar – Saxony.** Weekly radar of public activities of companies and institutes in the Saxon semiconductor ecosystem, prepared by the Czech National Semiconductor Cluster (CNSC) for Silicon Saxony under the memorandum of understanding of 12 Nov 2026.

- Live (GitHub Pages): https://smarterinstruments.github.io/Saxony-Radar/
- Seite / page: `index.html` (Sprachen: DE, EN, CZ)
- Daten / data: `data/radar_sx.json`; Tabelle / spreadsheet: `data/Saxony_Radar_final_W46_2026-11-16.xlsx`; Übersetzungen der Kurzprofile / profile translations: `data/profiles_translations_de_en.json`
- Reiter „Wertschöpfungskette“ / tab “Value chain map”: alle Organisationen in einem Bild, Klick öffnet die Karte / all organisations in one picture, click opens the card
- Build: `python3 tools/make_sx.py` (Daten) und `python3 tools/build_sx.py` (Seite) (Vorlage / template: `tools/template.html`, abgeleitet vom CNSC Member Activity Radar)

## Stand / status (Ausgabe W46/2026, 16. 11. 2026)

- 560 Organisationen: 481 Mitglieder von Silicon Saxony (öffentliches Mitgliederverzeichnis) und 79 Nichtmitglieder aus CNSC-Recherche (darunter seit 17. 11. Spiketronix und ELEMENT 3-5 aus der BMWE-Liste zum IPCEI AST) (gestrichelt markiert, Merkmal „Silicon Saxony member“); 532 davon durch CNSC-Recherche geprüft (15 Recherche-Chargen, 15.–16. 11. 2026) (Website, Segment, Kurzprofil mit Produkten und Dienstleistungen – auf der Organisationskarte in DE, EN und CZ, je nach gewählter Sprache; die Tabelle enthält alle drei Fassungen); zugeordnet zu 27 Codes der CNSC-Taxonomie der Wertschöpfungskette (10 Sektoren, Untersegmente 2.4.1–2.4.6). Die 26 noch nicht geprüften Organisationen sind auf der Karte und in der Wertschöpfungskette mit „?“ (ungeprüft) markiert; eine unsichere Zuordnung zusätzlich mit „Zuordnung zu prüfen / unsicher“. Die Zuordnung ist vorläufig und wartet auf die Bestätigung durch Silicon Saxony.
- 68 Meldungen und 5 Termine, bisher von den öffentlichen LinkedIn-Seiten (33) und YouTube-Kanälen (22, über öffentliche RSS-Feeds) ausgewählter Unternehmen und Institute sowie dem wöchentlichen Silicon-Saxony-Podcast „What's Chippening“ (Folgen 87–95, je eine Meldung mit Verweisen auf die genannten sächsischen Organisationen). Alle Meldungstexte sind eigene Zusammenfassungen, keine Zitate.
- Standort als „Ort (Land)“ aus Recherche bzw. Silicon-Saxony-Profil; 101 Standorte am 17. 11. 2026 anhand der Silicon-Saxony-Profilseiten (Kontakt), Firmenwebsites und Register nachgetragen bzw. korrigiert (`data/city_fixes.json`, Quelle je Eintrag). Ohne Ortsangabe bleiben 4 Organisationen (nur „DE“). Stand: 216 Mitglieder mit sächsischem Sitz, 263 Mitglieder mit Sitz außerhalb Sachsens (207 übriges Deutschland, 24 weitere Länder), 2 ohne Angabe; Nichtmitglieder 13 / 62 / 2. / Sites completed on 17 Nov 2026 from the Silicon Saxony profile pages, company websites and registers; 4 organisations remain without a stated site.
- Nur öffentliche Informationen; keine personenbezogenen Daten von Ansprechpartnern, keine internen Cluster-Informationen.

Korrekturen und Ergänzungen / corrections and additions: info@semicz.cz, Betreff „Radar Sachsen“.

## IPCEI

IPCEI-Beteiligung (Badge auf der Organisationskarte, Marker in der Wertschöpfungskette, Spalte in der Tabelle) stammt ausschließlich aus öffentlichen Quellen: Pressemitteilung des Freistaats Sachsen zu den neun sächsischen IPCEI-ME/KT-Projekten (2023), BMWK-Erläuterungspapier zum ersten IPCEI Mikroelektronik, Entscheidungen der Europäischen Kommission (IP/18/6862, IP/23/3087). IPCEI AST: BMWE-Liste „Beteiligte deutsche Unternehmen“ (Stand 30.06.2026, zur Förderung vorgesehen; Pränotifizierung von 14 Projekten bei der Kommission am 1.7.2026) – Badge „IPCEI AST 2026 · vorgesehen“ bei 11 Organisationen (8 sächsische Gesellschaften, 3 mit sächsischem Standort: Siltronic Freiberg, Wacker Nünchritz, ELEMENT 3-5 Glauchau). Sachsen ist Gründungs- und Initiativregion der European Semiconductor Regions Alliance (ESRA, 2023; `meta.esra`). `meta.json` trägt zusätzlich den Chips-Act-Fußabdruck (`chipsact`: 2 First-of-a-kind-Fabs ESMC/Infineon, 4 von 11 Pilotlinien mit sächsischem Standort, GSS – neues sächsisches Kompetenzzentrum (Details folgen), 2 EuroCDP-DETs) für den Hub. / IPCEI participation comes from public sources only; IPCEI AST from the BMWE list of 30 Jun 2026 (planned, Commission approval pending), 11 organisations tagged “planned”.

## Qualitätsprüfung / quality check

`python3 tools/check_labels.py index.html` prüft im Headless-Browser, dass sich im Radar keine Beschriftungen überlappen (Labels untereinander, mit Sektorbeschriftungen und mit Punkten), für DE, EN und CZ; erwartetes Ergebnis: `overlaps 0`. / Headless check that no radar labels overlap; expected result `overlaps 0`.
