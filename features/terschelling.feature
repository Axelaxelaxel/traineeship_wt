@wip
Feature: terschelling
    testen van de terschelling website

    Background:
    Given I got me some open browser
    And the browser is on the webpage terschelling.nl/home-terschelling

    Scenario Outline: Browsing
    When i press <a>
    And i press <b>
    And i press <c>
    Then i'am at <d>
    And i close the browser
    Examples:
    |a|b|c|d|
    |Leerlingenvervoer|Privacyverklaring|website van de Autoriteit Persoonsgegevens|https://www.autoriteitpersoonsgegevens.nl/|
    |MENU|Actueel|Toegankelijkheidsverklaring|https://www.terschelling.nl/home-terschelling/toegankelijkheidsverklaring_46110/|
    |Toegangstesten mogelijk|MENU|Regels en beleid|https://www.terschelling.nl/t-regels-beleid|
    |Toegangstesten mogelijk|Hoog contrast|http://testenvoortoegang.nl|https://www.terschelling.nl/t-actueel/nieuws_42180/item/toegangstesten-mogelijk_56790.html|
    |MENU|Politiek & bestuur|Terug naar Terschelling.nl|https://www.terschelling.nl/home-terschelling|


    Scenario Outline: presenting
    When i press <a>
    And i press <b>
    Then <c> <d> is present
    And i close the browser
    Examples:
    |a|b|c|d|
    |Informatie over het coronavirus|Algemene maatregelen|onverminderd van belang|text|

    Scenario: searching
    When i type hello in the searchbar
    And i press ZOEK
    Then i'am at https://www.terschelling.nl/home-terschelling/zoeken_42083/?trefwoord=hello
    And i close the browser

