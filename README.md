# BFS 5-Tile Puzzle Solver

A Python implementation of a BFS solver for a 5-tile puzzle with 2 A's, 2 B's, and an empty space. Moves follow strict rules for A and B, and the program finds the shortest path from a given start state to the goal state, showing success or failure if it reached a blocked state.

## Features

- Breadth-First Search (BFS) algorithm for puzzle solving  
- Generates all valid child states based on the position of the empty slot  
- Detects and reports if the goal state is found or if the puzzle is blocked  
- Color-coded console output for success and failure messages  

## Requirements

- Python 3.13.3

## Usage

- When you run the program, it will prompt you to enter the start state and the goal state.
- Both states must be 5 characters long and consist of exactly two 'A's, two 'B's, and one underscore `_` representing the empty slot.
- Example valid input: `AA_BB` or `BBA_A`
- The program will then perform a Breadth-First Search (BFS) to find the shortest sequence of moves to transform the start state into the goal state.
- It respects the puzzle rules where 'A' pieces can move or jump to the right, and 'B' pieces can move or jump to the left, swapping positions with the empty slot.
- The program outputs the solution path if the goal was reached, or the path to the blocked state if the problem is an unsolvable combination
- It indicates success if the goal is reached, or failure if the puzzle is unsolvable (blocked state).

## Example
How it should work and show you in the console:
Hello, this code is used to transform a list from one state to another,
there are 2 As and 2 Bs and one empty slot(block) all the time, aka a list of 5 positions,
valid movees are:
 A moving to the right one block to swap with empty slot, or A jumping over one block also to the right to fill the empty slot      
 B moving to the left one block to swap with empty slot, or B jumping over one block also to the left to fill the empty slot        
Enter your start state (use _ for empty square): aa_bb 
Enter your goal state (use _ for empty square): bb_aa 
Your Start State is: AA_BB
Your Goal State is: BB_AA
['A', 'A', '_', 'B', 'B']
['A', '_', 'A', 'B', 'B']
['A', 'B', 'A', '_', 'B']
['A', 'B', 'A', 'B', '_']
['A', 'B', '_', 'B', 'A']
['_', 'B', 'A', 'B', 'A']
['B', '_', 'A', 'B', 'A']
['B', 'B', 'A', '_', 'A']
['B', 'B', '_', 'A', 'A']
Success, Goal Found!!!
