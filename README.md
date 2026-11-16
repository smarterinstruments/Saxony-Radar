# Saxony Radar – Vorschau / preview

**Radar der Halbleiter-Wertschöpfungskette – Sachsen.** Wöchentlicher Radar der öffentlichen Aktivitäten von Unternehmen und Instituten des sächsischen Halbleiter-Ökosystems, erstellt vom Czech National Semiconductor Cluster (CNSC) für Silicon Saxony im Rahmen der Absichtserklärung vom 12. 11. 2026.

**Semiconductor Value Chain Radar – Saxony.** Weekly radar of public activities of companies and institutes in the Saxon semiconductor ecosystem, prepared by the Czech National Semiconductor Cluster (CNSC) for Silicon Saxony under the memorandum of understanding of 12 Nov 2026.

- Seite / page: `index.html` (Sprachen: DE, EN, CZ)
- Daten / data: `data/radar_sx.json`; Tabelle / spreadsheet: `data/Saxony_Radar_final_W46_2026-11-16.xlsx`; Übersetzungen der Kurzprofile / profile translations: `data/profiles_translations_de_en.json`
- Reiter „Wertschöpfungskette“ / tab “Value chain map”: alle Organisationen in einem Bild, Klick öffnet die Karte / all organisations in one picture, click opens the card
- Build: `python3 tools/make_sx.py` (Daten) und `python3 tools/build_sx.py` (Seite) (Vorlage / template: `tools/template.html`, abgeleitet vom CNSC Member Activity Radar)

## Stand / status (Ausgabe W46/2026, 16. 11. 2026)

- 536 Organisationen: 481 Mitglieder von Silicon Saxony (öffentliches Mitgliederverzeichnis) und 55 Nichtmitglieder aus CNSC-Recherche (gestrichelt markiert, Merkmal „Silicon Saxony member“); 380 davon durch CNSC-Recherche geprüft (Website, Segment, Kurzprofil mit Produkten und Dienstleistungen – auf der Organisationskarte in DE, EN und CZ, je nach gewählter Sprache; die Tabelle enthält alle drei Fassungen); zugeordnet zu 27 Codes der CNSC-Taxonomie der Wertschöpfungskette (10 Sektoren, Untersegmente 2.4.1–2.4.6). Die 156 noch nicht geprüften Organisationen sind auf der Karte und in der Wertschöpfungskette mit „?“ (ungeprüft) markiert; eine unsichere Zuordnung zusätzlich mit „Zuordnung zu prüfen / unsicher“. Die Zuordnung ist vorläufig und wartet auf die Bestätigung durch Silicon Saxony.
- 68 Meldungen und 5 Termine, bisher von den öffentlichen LinkedIn-Seiten (33) und YouTube-Kanälen (22, über öffentliche RSS-Feeds) ausgewählter Unternehmen und Institute sowie dem wöchentlichen Silicon-Saxony-Podcast „What's Chippening“ (Folgen 87–95, je eine Meldung mit Verweisen auf die genannten sächsischen Organisationen). Alle Meldungstexte sind eigene Zusammenfassungen, keine Zitate.
- Nur öffentliche Informationen; keine personenbezogenen Daten von Ansprechpartnern, keine internen Cluster-Informationen.

Korrekturen und Ergänzungen / corrections and additions: info@semicz.cz, Betreff „Radar Sachsen“.

## IPCEI

IPCEI-Beteiligung (Badge auf der Organisationskarte, Marker in der Wertschöpfungskette, Spalte in der Tabelle) stammt ausschließlich aus öffentlichen Quellen: Pressemitteilung des Freistaats Sachsen zu den neun sächsischen IPCEI-ME/KT-Projekten (2023), BMWK-Erläuterungspapier zum ersten IPCEI Mikroelektronik, Entscheidungen der Europäischen Kommission (IP/18/6862, IP/23/3087). IPCEI AST ist nicht enthalten. / IPCEI participation comes from public sources only; IPCEI AST is not included.

## Qualitätsprüfung / quality check

`python3 tools/check_labels.py index.html` prüft im Headless-Browser, dass sich im Radar keine Beschriftungen überlappen (Labels untereinander, mit Sektorbeschriftungen und mit Punkten), für DE, EN und CZ; erwartetes Ergebnis: `overlaps 0`. / Headless check that no radar labels overlap; expected result `overlaps 0`.
