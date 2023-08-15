
# Tic-Tac-Toe Game
A simple command-line implementation of the classic Tic-Tac-Toe game in Python.

# Game Overview
This is a two-player implementation of Tic-Tac-Toe, where the players take turns to place their marks ('X' and 'O') on a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

# Features
Interactive command-line interface.
Input validation to ensure players choose available positions.
Win detection for both 'X' and 'O' players.
Graceful handling of invalid inputs.

# How to Play
Clone the repository to your local machine.
Open your terminal or command prompt and navigate to the project directory.
Run the script by entering: python tic_tac_toe.py
Enter the names of the two players.
During your turn, enter the row and column numbers (1-3) where you want to place your mark.

# Example Gameplay

'X player Name: Alice'
O player Name: Bob

   |   |   
-----------
   |   |   
-----------
   |   |   

Alice

Enter the row number (1-3) > 2
Enter the column number (1-3) > 2

   |   |   
-----------
   | X |   
-----------
   |   |   

Bob

Enter the row number (1-3) > 1
Enter the column number (1-3) > 2

   | O |   
-----------
   | X |   
-----------
   |   |   

...

Alice

Enter the row number (1-3) > 3
Enter the column number (1-3) > 3

   | O |   
-----------
   | X |   
-----------
   |   | X
'
# Alice is win
Future Enhancements
This implementation provides a basic foundation for playing Tic-Tac-Toe in the terminal. Here are some ideas for future enhancements:

Implement a graphical user interface (GUI) using a library like Tkinter.
Add more sophisticated win detection algorithms to reduce repetitive code.
Create an AI opponent for single-player gameplay.
Implement error handling for unexpected input during gameplay.
Feel free to contribute to this project by forking the repository, making your enhancements, and submitting a pull request!

# Contributors
Mohamed Ashour
#License
This project is licensed under the MIT License.


