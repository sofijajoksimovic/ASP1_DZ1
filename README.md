# ASP1_DZ1 - Algorithms and Data Structures 1: Dice Game Simulation

This project simulates a dice game with various types of moves and scoring combinations. It includes the use of a matrix to track and manage the scores and game state, as well as simulating dice rolls.

## Features

- **Dice Rolls:** Simulates rolling five dice at once and re-rolling specific dice based on user input.  
- **Scoring Combinations:** Implements various scoring combinations such as:  
  - *Jedinice* (Ones)  
  - *Dvojke* (Twos)  
  - *Trojke* (Threes)  
  - *Kenta* (Small and Large)  
  - *Ful* (Full House)  
  - *Poker*  
  - *Jamb* (Yahtzee)  
- **Game State:** Tracks the score for each combination, stores the state in a matrix, and allows players to add new elements to the matrix as they play.  
- **Matrix Representation:** Uses a sparse matrix to track which combinations have been filled in the game and updates the matrix as the game progresses.  
- **Random Functions:** Utilizes a pseudo-random number generator for simulating dice rolls based on a custom seed.  

## Requirements

- Python 3.x  

## How It Works

### Matrix Representation

The game state is represented by a matrix that holds the scores for different combinations across three columns: `Nagore`, `Nadole`, and `Rucna`. As players progress through the game, scores are added to the matrix, and the game state is updated accordingly.

### Dice Rolling

The program uses the `cube()` function to simulate the rolling of five dice. Players can choose to keep specific dice and reroll the others. The `ponovo()` function handles rerolls based on the player's choices.

### Scoring Combinations

The following scoring combinations are implemented:
- **Jedinice (Ones):** The sum of all dice showing 1.  
- **Dvojke (Twos):** The sum of all dice showing 2.  
- **Trojke (Threes):** The sum of all dice showing 3.  
- **Kenta:** A specific sequence of dice (either small or large).  
- **Ful:** A full house (three of one number and two of another).  
- **Poker:** Four of the same number.  
- **Jamb (Yahtzee):** All five dice showing the same number.  

### Adding Scores

Scores are added to the matrix using the `dodajElem()` function, which updates the row and column for the corresponding combination..

## Example Output

```bash
    NAGORE:        NADOLE:        RUCNA:  
1               2               3  
-               -               -  
-               -               -  
...  
SUMA:           0               0               0  
