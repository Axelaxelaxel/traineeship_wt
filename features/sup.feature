
Feature: banktransfer

Background:
    Given I have 5000 euro in my bank account
    And my bank allows me to transfer 1000 euro max
 
Scenario Outline: 
 When I transfer <amount> euro to my friends bank account
 Then the money has <state> been transferred
 Examples:
 |amount|state          |
 |-1    |not            |
 |0     |not            |
 |1     |succesfully    |
 |999   |succesfully    |
 |1000  |succesfully    |
 |1001  |not            |
 |4999  |not            |
 |5000  |not            |
 |5001  |not            |

 