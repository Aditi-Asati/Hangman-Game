# Hangman

Hangman, fundamentally is a guessing game.

This implementation of the hangman game is focused on guessing fruit names.

A random fruit name is chosen with about half of its characters revealed while the rest are masked in order for the player to guess them.

A certain number of chances will be allowed to guess the fruit name, character by character and if the player correctly guesses all masked characters of the fruit, then the game is over and the player wins. 

To increase the game difficulty, we've also added timeout for guesses. Each guess will have a timeout of 15s. If the timeout expires, one chance will be reduced from the total number of chances.

Enjoy :)