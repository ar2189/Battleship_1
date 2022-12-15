<h1>Battleship</h1>
<br>
<p>Battleship is a Python terminal gamewhich runs in the Code Institute mock terminal on Heroku.
The user and computer place their ship on the board and both have to eliminate the enemy ship before each of them.</p>
<br>
<p>Below you will find the live version of my project.</p>


<h2>How to play</h2>
<br>
<p>Battleship is based on the classic pen-and-paper game. In this version the player decides the size of the board.<br>
After that the player places one ship on the board. The computer does the same and chooses to place a ship in a random position.
The player ship location is marked by a # while the computer ship is hidden from the player. Player missed attacks are marked by an X and computer missed
attacks are marked by a *. When either sinks the enemy battleship a message occurs who hit and tells the player if the player won or lost.</p>
<br><br>

<h2>Features</h2>
<br>
<h3>Existing features</h3>
<ul>Adjust the size of the board
  <li>The player is asked to adjust the board size between 2 and 10.</li>
  <li>This feature also lets the player choose how long the might last. If it is a small board then it wont take long.
  if it is a large board, it might take a while to finish the game.</li>
  <li>Once the size of the board is decided, the player sets the ship inside the adjusted board. The computer does the same.</li>
  <li>After that the game describes the signs for the player ship(#), player missed hits(X) and computer missed hits(*)</li>
  <li>Player is then asked to guess a row and a column where player wants to attack.</li>
  <li>Player can only enter integers. If not then the games asks player to try again until the correct row and column are inputed.</li>
  <li>The game continues until one of the players hits the enemy ship.</li>
  <li>Once hit the one who hits wins the game. The game then tells how many moves it took for one side to win.</li>
  <li>When the game ends it asks if the player wants to play again.</li>
</ul>

