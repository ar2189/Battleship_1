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
  
  ![Screenshot 2022-12-17 11 05 47](https://user-images.githubusercontent.com/112749480/208236725-1e2eb7d9-2416-4e1e-a387-20135836536d.png)
  
  <li>This feature also lets the player choose how long the might last. If it is a small board then it wont take long.
  if it is a large board, it might take a while to finish the game.</li>
  <li>Once the size of the board is decided, the player sets the ship inside the adjusted board. The computer does the same.</li>
  
  ![Screenshot 2022-12-17 11 06 18](https://user-images.githubusercontent.com/112749480/208236750-107e30cd-cd2f-4298-8c89-1fb7f5d7c71a.png)
  
  <li>After that the game describes the signs for the player ship(#), player missed hits(X) and computer missed hits(*)</li>
  <li>Player is then asked to guess a row and a column where player wants to attack.</li>
  <li>Player can only enter integers. If not then the games asks player to try again until the correct row and column are inputed.</li>
  <li>The game continues until one of the players hits the enemy ship.</li>
  <li>When either the player or computer ship has sunk does the game end. The game then tells how many moves it took for one side to win.</li>
  <li>When the game ends it asks if the player wants to play again.</li>
  
  ![Screenshot 2022-12-17 11 07 16](https://user-images.githubusercontent.com/112749480/208236845-42ee0210-503c-4b8c-869d-4a9b563e25d4.png)
  
</ul>

<br>
<h3>Future Features</h3>
<ul>
  <li>Allow player to place more than one ship.</li>
  <li>Have ships larger than 1x1.</li>
</ul>

<br>
<h2>Data Model</h2>
<br>
<p>I decided to use the place holder method as my model. The game gives the player to choose the size of the board the player wishes to.
Inside that board both player and computer decide where they would wish to place the battleship, with the latter choosing a position randomly but not coinside with the player position.
As you go further in the code you will see the code written for the player to guess a row and column and for the computer to choose one randomely.
It also shows when a player or computer wins, how many moves it took for the game to end.
The code also shows if the player wishes to play again.</p>

<br>
<h2>Testing</h2>
<ul>
  <li>Passed the code through a PEP8 linter and confirmed there are no errors.</li>
  <li>Tested in my local GitHub terminal and the Code Institute Heroku terminal.</li>
</ul>

<br>
<h2>Bugs</h2>
<ul>
  <li>Before writing the code I practised to write the code on Replit where it was more time efficient.</li>
  <li>I had trouble during the first step where it shows me to decide the size of the board, but gave an error when I inputed an integer
    The problem was that I hadn't structured the <action>if</action> statement properly.</li>
  <li>After the game ends, it showed an error when deciding to restart the game. The play_again() statement was missing in the def main().</li>
</ul>

<h2>Deployment</h2>
<ul>
  <li>Fork or clone this repository.</li>
  <li>Create a new Heroku app.</li>
  <li>Set the buildbacks to Python and NideJS in that order.</li>
  <li>Link the Heroku app to the repository.</li>
  <li>Click on <action>Deploy</action>.</li>
</ul>

<br>
<h2>Credits</h2>
<ul>
  <li>Code Institute for deployment terminal.</li>
  <li>Kowledge Mavens(Youtube Channel)</li>
  <li>Pythondex.com</li>
</ul>
