import random
import matplotlib.pyplot as plt

# Task 1: Simulating Coin Tosses
def simulate_coin_tosses():
    """
    Simulates tossing a coin 100 times, counts the number of heads and tails,
    prints the results, and plots the frequencies in a bar chart.
    """
    results = [random.choice(['Heads', 'Tails']) for _ in range(100)]
    heads = results.count('Heads')
    tails = results.count('Tails')
    
    # Print the results
    print('='*50)
    print("Coin Tosses Frequencies\n")
    print(f'Frequency of Heads: {heads}, \nFrequency of Tails: {tails}\n')
    print('='*50)
    
    # Plot the results
    plt.bar(['Heads', 'Tails'], [heads, tails])
    plt.title('Coin Tosses')
    plt.show()

# Task 2: Rolling a Die
def simulate_dice_rolls():
    """
    Simulates rolling a six-sided die 60 times, counts the frequency of each outcome,
    prints the results, and plots the frequencies in a bar chart.
    """
    results = [random.randint(1, 6) for _ in range(60)]
    counts = [results.count(i) for i in range(1, 7)]
    
    # Print the results
    print(f'Rolls: {counts}\n')
    print('='*50)
    
    # Plot the results
    plt.bar(range(1, 7), counts)
    plt.title('Dice Rolls')
    plt.show()

# Task 3: Drawing Cards
def simulate_card_draws():
    """
    Simulates drawing a card from a shuffled deck 20 times, counts how many are red and black,
    prints the results, and plots the frequencies in a bar chart.
    """
    deck = ['Red'] * 26 + ['Black'] * 26  # Standard deck with 26 red and 26 black cards
    random.shuffle(deck)
    results = [random.choice(deck) for _ in range(20)]
    red_count = results.count('Red')
    black_count = results.count('Black')
    
    # Print the results
    print(f'Red: {red_count}, Black: {black_count}\n')
    print('='*50)
    
    # Plot the results
    plt.bar(['Red', 'Black'], [red_count, black_count])
    plt.title('Card Draws')
    plt.show()

# Task 4: Probability of Compound Events
def simulate_compound_events():
    """
    Simulates flipping two coins 50 times, counts the outcomes for both heads, at least one head,
    and neither heads, prints the results, and plots the frequencies in a bar chart.
    """
    both_heads = 0
    at_least_one_head = 0
    neither_heads = 0
    
    # Simulate flipping two coins 50 times
    for _ in range(50):
        flip1 = random.choice(['Heads', 'Tails'])
        flip2 = random.choice(['Heads', 'Tails'])
        if flip1 == 'Heads' and flip2 == 'Heads':
            both_heads += 1
        elif flip1 == 'Heads' or flip2 == 'Heads':
            at_least_one_head += 1
        else:
            neither_heads += 1
    
    # Verify the total number of trials is 50
    total = both_heads + at_least_one_head + neither_heads
    assert total == 50, f"Total should be 50 but is {total}"

    # Print the results
    print(f'Both Heads: {both_heads}, At Least One Head: {at_least_one_head}, Neither Heads: {neither_heads}')
    
    # Plot the results with improved styling
    labels = ['Both Heads', 'At Least One Head', 'Neither Heads']
    counts = [both_heads, at_least_one_head, neither_heads]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, counts, color=colors)

    plt.title('Compound Events', fontsize=16)
    plt.ylabel('Count', fontsize=14)
    plt.xlabel('Event', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add text annotations
    for bar, count in zip(bars, counts):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{count}', ha='center', va='bottom', fontsize=12)
    
    # Adjust the upper horizontal border line
    ax = plt.gca()
    ax.spines['top'].set_visible(False)  # This line hides the top spine

    plt.show()

if __name__ == "__main__":
    # Run all simulations
    simulate_coin_tosses()
    simulate_dice_rolls()
    simulate_card_draws()
    simulate_compound_events()
