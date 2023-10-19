import os
from datetime import datetime

# Define the path to the experiment log file
log_file = 'experiment_log.txt'

# Check if the log file exists, create it if not
if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        f.write("Experiment Log\n")
        f.write("----------------\n")

def log_experiment():
    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Prompt the user for an experiment description
    experiment_description = input("Enter a description of the experiment: ")

    # Append the experiment details to the log file
    with open(log_file, 'a') as f:
        f.write(f"\nDate and Time: {current_time}\n")
        f.write(f"Experiment Description: {experiment_description}\n")
        f.write("-" * 40 + "\n")

if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. Log an experiment")
        print("2. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            log_experiment()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please select a valid option.")


