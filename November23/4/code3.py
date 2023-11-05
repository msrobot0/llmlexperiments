import random
import time

# Define a list of movements inspired by Yvonne Rainer's style
movements = [
    "Jump",
    "Twist",
    "Crawl",
    "Spin",
    "Walk",
    "Collapse",
    "Extend",
    "Improvise",
    "Pause",
    "Repetition",
]

# Define a function to perform a random movement inspired by Yvonne Rainer
def perform_random_movement():
    movement = random.choice(movements)
    duration = random.uniform(1.0, 4.0)  # Random duration in seconds

    print(f"Performing {movement} for {duration:.2f} seconds...")
    time.sleep(duration)
    print("Movement completed.")

# Simulate a performance with a sequence of random movements
def simulate_performance(num_movements):
    for _ in range(num_movements):
        perform_random_movement()

if __name__ == "__main__":
    print("Welcome to the Yvonne Rainer-inspired performance simulator!")
    num_movevements = len(movements)
    try:
        num_movements = int(input("Enter the number of movements in the performance: "))
    except:
        pass

    simulate_performance(num_movements)

    print("Performance complete. Thank you for exploring Yvonne Rainer's style!")

