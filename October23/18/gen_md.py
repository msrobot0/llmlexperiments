import os
from datetime import datetime

# Define the path to the experiment log file
log_file = 'experiment_log.md'

# Check if the log file exists, create it if not
if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        f.write("# Experiment Log\n")

def log_experiment():
    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Prompt the user for experiment details
    experiment_title = input("Enter a title for the experiment: ")
    experiment_description = input("Enter a brief description: ")
    github_link = input("Enter the GitHub link (if any): ")
    youtube_link = input("Enter the YouTube link (if any): ")

    # Create a Markdown section for the experiment
    markdown_content = f"""
## Experiment: {experiment_title}
- **Date and Time:** {current_time}
- **Description:** {experiment_description}
- **GitHub Link:** {github_link}
- **YouTube Link:** {youtube_link}
"""

    # Collect prompts and results
    prompts = []
    results = []
    while True:
        prompt = input("Enter a prompt (or 'q' to finish): ")
        if prompt == 'q':
            break
        result = input("Enter the result (formatted with code markdown): ")
        prompts.append(prompt)
        results.append(result)

    # Collect additional descriptions
    initial_summary = input("Enter an initial summary: ")
    inspiration = input("Enter inspiration for the experiment: ")
    final_analysis = input("Enter a final analysis and conclusion: ")

    # Append the experiment details to the log file
    with open(log_file, 'a') as f:
        f.write(markdown_content)
        for prompt, result in zip(prompts, results):
            f.write(f"**Prompt:** {prompt}\n\n")
            f.write(f"**Result:**\n\n```\n{result}\n```\n\n")
        f.write(f"**Initial Summary:** {initial_summary}\n\n")
        f.write(f"**Inspiration:** {inspiration}\n\n")
        f.write(f"**Final Analysis and Conclusion:** {final_analysis}\n\n")

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


