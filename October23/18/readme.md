So today I am going to generate something in the 3D Program blender. I really want a day to reflect on what I am doing - maybe this weekend. For now I am just keeping up the pace. 


I had to do some basic modifications on my system - namely installing the blender python module that I had to build from [source](https://wiki.blender.org/wiki/Building_Blender/Mac) -  ugh - pain. 

It is taking too long so I am going another direction. I am generating a python script to help me document these experiments!
![[gen.png]]

### Prompt 
>  generate a python script that creates a template to document daily experiments with chatgpt generating code
>  
### Code
Creating a Python script to document daily experiments with ChatGPT generating code is a helpful way to keep track of your work and the results you obtain. Below is a simple Python script template that you can use as a starting point. This script uses the `input()` function to take notes on your experiments and stores them in a text file for future reference:

```python
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

```

This script provides a menu where you can choose to log an experiment or quit the program. When you log an experiment, it records the current date and time along with your experiment description into the `experiment_log.txt` file. You can customize the log file's name and structure to suit your preferences.

To use the script:

1. Save it as a Python (.py) file.
2. Run the script.
3. Follow the prompts to log your daily experiments and notes.

This simple template can be expanded to include more features like tagging, categories, or additional metadata to make it more comprehensive based on your needs.

### Update
I wanted to modify this script to collect more data and output as markdown - I am writing this in obsidian or nvim. 

### Prompt 2
> modify this script to output markdown and to collect the following data about an experiment: an image, a github link, an optional youtube link, a list of prompts and results (formated with code markdown), and initial summary and inspiration, and a final analysis and conclusion.

### Code
> To modify the script to output Markdown and collect more detailed information about an experiment, including an image, GitHub link, YouTube link, prompts, results, and additional descriptions, you can use the following modified script:

```python
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

```

This script will collect and organize more detailed information for each experiment, including prompts, results, initial summary, inspiration, and final analysis and conclusion. It generates a Markdown file (`experiment_log.md`) for documentation.

Remember to install any necessary libraries for rendering images or including links to your GitHub and YouTube pages, as those functionalities are not included in the basic script.

OpenAI. (2023). _ChatGPT_ (September 25 Version) [Large language model]. https://chat.openai.com


###  conclusion 
Take take a look at the experiment log in the [github repository for experiment 5](https://github.com/msrobot0/llmlexperiments/tree/main/October23/18).   It needs some work, but I think it will really help me save time in documenting these experiments!![[gen_md.png]]