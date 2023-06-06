# Project Python trojan framework
### De Smedt Laurens 2ITCSC2
### werking video : https://ap.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=6e09f6a1-d75c-4604-973a-b01900f9bcc9
### requirements staan in het mapje info
### test repo : https://github.com/laurensDSM/test0
## Werking:
- momenteel enkel getest op rocky linux 
- Als de gebruiker op een gevaarlijke link klikt dan wordt er een bestand op de computer van de gebruiker gezet.
- Vervolgens zal het script gerund worden. Het programma bevat default deze zaken
    - Main programma 
    - Connectie naar een github repo
    - Een default config 
    - Default module die systeem info zal opslaan
    - Deze informatie zal opgeslagen worden en verzonden worden naar een github repo
        - Dit is een mapje met de hostname + datum + random nummer
        - + en tekst file  zoals : Hallo ik ben op 2023-06-06_17-10-27 besmet
 - Na een tijd die aanpasbaar is zal de main een functie aanroepen die gaat controleren of er op de repo een config file aanwezig is zoja dan gaat hij een git clone uitvoeren en de nieuwe modules inladen die door een hacker zijn online gezet en de oude verwijderen voor de opslag te verminderen. 
 - Hij zal dan deze modules uit voeren en ook de verkregen bestanden opslaan en versturen naar Github (evenutueel ook bestanden verwijderen nadat de module is uitgevoerd) deze zullen in het zelfde mapje terechtkomen 



### Te werk gaan : 
- Eerst proberen om een bestand van een github repo te halen
- Vervolgens een test module te laten werken 
- Die een bestand zal maken in het mapje logs 
- En vervolgens de bestanden zal versturen naar de repo
- Modules maken 
- Config aanpassen 
- Automatisch config inladen voor elke module
- Nieuwe config inladen van github
- Nieuwe modules installeren 

### Modules 
* default om de hacker te laten weten dat hij een nieuwe pc heeft
* folders structuur van de map home
* Wan het wan ip van de klant
* sysinfo systeeminformatie 
* nmap nmap van het netwerk 