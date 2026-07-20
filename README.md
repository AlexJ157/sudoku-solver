# Sudoku Solver

A Python implementation of a Sudoku solver using a recursive backtracking algorithm.

## Overview

This project solves Sudoku puzzles by using a backtracking search algorithm. The program takes an incomplete Sudoku board as input, finds empty cells, tests possible values, and recursively explores solutions until a valid solution is found.

The project was created to practise:
- Recursion
- Backtracking algorithms
- Problem solving
- Python programming

## Features

- Solves standard 9x9 Sudoku puzzles
- Checks whether numbers are valid according to Sudoku rules
- Uses recursive backtracking to find solutions
- Displays the solved board

## How It Works

The algorithm:
1. Finds an empty cell on the board
2. Tries possible numbers from 1-9
3. Checks if the number is valid
4. Recursively continues solving
5. Backtracks when a solution path fails

## Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/sudoku-solver.git
