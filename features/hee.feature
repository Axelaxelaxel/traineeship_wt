Feature: duckduckgo
    searching on duckduckgo in the browser

    Scenario: search
        Given I have an open chrome browser
        When the browser is on the webpage duckduckgo.com
        And I fill in the search bar with hee
        And I execute the search
        Then I'll quit the browser

