# Online Repertorium van teksten in het handschrift Hulthem

In het Repertorium van teksten in het Handschrift-van Hulthem: hs. Brussel, Koninklijke Bibliotheek van België, 15.589-15.623 is een verscheidenheid aan gegevens te vinden over alle teksten die het Handschrift-van Hulthem, de ‘Nachtwacht van de Middelnederlandse letterkunde’, bevat. Het Repertorium werd vervaardigd door Greet Jungman en Hans Voorbij en verscheen in 1999 bij Uitgeverij Verloren. Een papieren boek voor de inleidende teksten, met achterin een CD-ROM met het Repertorium. De software op de CD-ROM is op moderne computers niet meer te gebruiken. 

Dit project vervangt de CD-ROM en maakt alle inhoudelijke gegevens op de CD-ROM opnieuw toegankelijk. (De CD-ROM bevat ook een databasestructuur en diverse indexen. Deze zijn niet overgenomen. De informatiestructuur is geteflecteerd in de structuut van de HTML-bronnen. Een indexering met/voor zoekmachines staat hoog op de lijst van 'todos'.)

Dit project voorziet in een rechtstreekse 'port' (migratie) van de informatie op de CD-ROM naar HTML. Het idee is dat dit een technologisch vederlichte site oplevert die beter bestand is tegen de snelle ontwikkelinfen in IT-technologie. Afgezien van de meer verfijnde elementen van opmaak zou de huidige site ook in 1999 hebben gefunctioneerd.

Versie 0.1.0b is de eerste bèta-release van het project. De primaire migratie is daarmee afgerond en alle informatie van de CD-ROM is opnieuw eenvoudig toegankelijk. Er blijft echter veel over om te wensen.

## Vervolgstappen

### Noodzakelijk eisen en wensen (Must Haves)
1. Data [FAIR](https://www.go-fair.org/fair-principles/) toegankelijk maken. Op dit moment hebben de HTML-elementen die de eigenlijke data dragen geen uniekr en persistente identifiers. Wel is in de meeste gevalleb de 'provenance' aangegeven (verwijzend) naar het bestand en het regelnummer waar de informatie op de CD-ROM vandaan komt.
2. Alle infornatie moet beschikbaar komen in een generiek en open data-georiënteerd formaat (HTML is primair presebtatie-georiënteerd), zoals JSON.
3. Naast het aanbrengen van unieke ids moet alle informatie ook downloadbaar gemaakt worden als deelbestanden, zowel via de grafische frontend als een computationele toegang (API).

### Belangrijke eisen en wensen (Should Haves)
1. Alle data en pagina's zodanig technisch metadateren dat de informatie maximaal vindbaar wordt vie zoekmachines op het internet.
2. Publicatie in de repository van de oorspronkelijke inhoud van de CD-ROM. 
3. In verband met het punt hierboven en de gemigreerde data alswel de migratiecode: gepubliceerde open source/open access licenties voor alle bronnen op de site.

### Secundaire eisen en wensen (Nice to haves)
1. Accessibility conformance: checks en implementatie van verbeteringen waardoor de site toegankelijker wordt voor gebruikers met (bijv. visuele) beperkingen.
2. Engels 'locale' (interface en opschriften van velden ook beschikbaar in het Engels. (Eventueel: Duits, Frans?)
3. Zoekfunctionaliteit, over al het materiaal en per veld/categorie. (Faceted search?)

--JZ_20210619
