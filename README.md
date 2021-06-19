# Online Repertorium van teksten in het handschrift Hulthem

Dit is de code-repository van de code en data voor de migratie naar het internet van het digitale repertorium van teksten in het handschrift Hulthem op CD-ROM. Het [Online Repertorium](https://jorisvanzundert.github.io/repertorium_hulthem/) vind je op: https://jorisvanzundert.github.io/repertorium_hulthem/.

In het Repertorium van teksten in het Handschrift-van Hulthem: [hs. Brussel, Koninklijke Bibliotheek van België, 15.589-15.623](https://uurl.kbr.be/1737555) is een verscheidenheid aan gegevens te vinden over alle teksten die het Handschrift-van Hulthem, de ‘Nachtwacht van de Middelnederlandse letterkunde’, bevat. Het Repertorium werd vervaardigd door Greet Jungman en Hans Voorbij en verscheen in 1999 bij [Uitgeverij Verloren](https://verloren.nl/boeken/2086/262/165/middeleeuwen/repertorium-van-teksten-in-het-handschrift-van-hulthem). Een papieren boek voor de inleidende teksten, met achterin een CD-ROM met het Repertorium. De software op de CD-ROM is op moderne computers niet meer te gebruiken. Wel is er [virtual machine](https://github.com/HuygensING/hulthem) software waarmee de CD-ROM in oorspronkelijk formaat kan worden gebruikt.

Dit project vervangt de CD-ROM en maakt alle inhoudelijke gegevens op de CD-ROM opnieuw toegankelijk. (De CD-ROM bevat ook een databasestructuur en diverse indexen. Deze zijn niet overgenomen. De informatiestructuur is gereflecteerd in de structuur van de HTML-bronnen.) Een zoekfunctie staat op de lijst van 'todos'.

Dit project voorziet in een rechtstreekse 'port' (migratie) van de informatie op de CD-ROM naar HTML. Het idee is dat dit een technologisch vederlichte site oplevert die beter bestand is tegen de snelle ontwikkelingen in IT-technologie. Afgezien van de meer verfijnde elementen van opmaak zou de huidige site ook in 1999 hebben gefunctioneerd.

Versie 0.1.0b is de eerste bèta-release van het project. De primaire migratie is daarmee afgerond en alle informatie van de CD-ROM is [opnieuw eenvoudig toegankelijk](https://jorisvanzundert.github.io/repertorium_hulthem/). Er blijft echter veel over om te wensen.

## Vervolgstappen

### Noodzakelijk eisen en wensen (Must Haves)
1. Data [FAIR](https://www.go-fair.org/fair-principles/) toegankelijk maken. Op dit moment hebben de HTML-elementen die de eigenlijke data dragen geen unieke en persistente identifiers. Wel is in de meeste gevallen de 'provenance' aangegeven (verwijzend naar het bestand en het regelnummer waar de informatie op de CD-ROM vandaan komt).
2. Alle infornatie moet beschikbaar komen in een generiek en open data-georiënteerd formaat (HTML is primair presentatie-georiënteerd), zoals JSON.
3. Naast het aanbrengen van unieke IDs moet alle informatie ook downloadbaar gemaakt worden als deelbestanden, zowel via de grafische frontend als een computationele toegang (API).

### Belangrijke eisen en wensen (Should Haves)
1. Alle data en pagina's zodanig technisch metadateren dat de informatie maximaal vindbaar wordt via zoekmachines op het internet.
2. Publicatie in de repository van de oorspronkelijke inhoud van de CD-ROM. 
3. In verband met het punt hierboven en de gemigreerde data alswel de migratiecode: gepubliceerde open source/open access licenties voor alle bronnen op de site.

### Secundaire eisen en wensen (Nice to Haves)
1. Accessibility conformance: checks en implementatie van verbeteringen waardoor de site toegankelijker wordt voor gebruikers met (bijv. visuele) beperkingen.
2. Engels 'locale' (interface en opschriften van velden ook beschikbaar in het Engels. (Eventueel: Duits, Frans?)
3. Zoekfunctionaliteit, over al het materiaal en per veld/categorie. (Faceted search?)

--JZ_20210619
