

Feature: Tic-Tac-Toe

  The Tic-Tac-Toe game does the best move depending on the previous human
  move. Test these moves.

    Background:
          Given we have an empty tic-tac-toe board
  
  
  Scenario: First move
   When I play X on column 2 and row 2 on the board
    And I ask the computer to do its best move for O
   Then the board has a O in column 1 and row 1 on the board

  Scenario: Computer wins
   When I play X on column 2 and row 2 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 2 and row 3 on the board
    And I ask the computer to do its best move for O 
    And I play X on column 1 and row 3 on the board
    And I ask the computer to do its best move for O 
   Then O is the winner of the game

   Scenario: Tie
   When the following game is being played
    |p|c|r|
    |X|1|1|
    |O|1|2|
    |X|1|3|
    |O|2|2|
    |X|2|1|
    |O|3|1|
    |X|2|3|
    |O|3|3|
    |X|3|2|
    Then it's a tie
