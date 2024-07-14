# Probability Simulation Program

## Overview

This program simulates various probability experiments and calculates the outcomes. It includes four main tasks: simulating coin tosses, rolling a die, drawing cards from a deck, and calculating the probability of compound events. Each task is implemented in a separate function, and the results are visualized using bar plots.

## Tasks

### Task 1: Simulating Coin Tosses

- **Function:** `simulate_coin_tosses()`
- **Description:** Simulates tossing a coin 100 times and counts the number of heads and tails.
- **How it works:**
  - Randomly selects 'Heads' or 'Tails' for 100 trials.
  - Counts the occurrences of heads and tails.
  - Prints the frequencies and displays a bar plot of the results.

### Task 2: Rolling a Die

- **Function:** `simulate_dice_rolls()`
- **Description:** Simulates rolling a six-sided die 60 times and prints the frequency of each outcome.
- **How it works:**
  - Randomly selects a number between 1 and 6 for 60 trials.
  - Counts the occurrences of each face (1 through 6).
  - Prints the frequencies and displays a bar plot of the results.

### Task 3: Drawing Cards

- **Function:** `simulate_card_draws()`
- **Description:** Simulates drawing a card from a shuffled deck 20 times and counts how many are red versus black.
- **How it works:**
  - Creates a deck with 26 red and 26 black cards and shuffles it.
  - Randomly draws 20 cards from the deck.
  - Counts the number of red and black cards.
  - Prints the frequencies and displays a bar plot of the results.

### Task 4: Probability of Compound Events

- **Function:** `simulate_compound_events()`
- **Description:** Simulates flipping two coins 50 times and counts the outcomes for both heads and at least one head.
- **How it works:**
  - Randomly selects 'Heads' or 'Tails' for each of two coins for 50 trials.
  - Counts the occurrences where both coins are heads and where at least one coin is heads.
  - Prints the frequencies and displays a bar plot of the results.

## Running the Program

To run the program, execute the Python script. The program will sequentially run each of the four tasks. The results of each simulation will be printed to the console and displayed as bar plots.

### Example

```python
if __name__ == "__main__":
    simulate_coin_tosses()
    simulate_dice_rolls()
    simulate_card_draws()
    simulate_compound_events()
