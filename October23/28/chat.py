import random
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set the model to evaluation mode
model.eval()

# Define a function to generate prompts
def generate_video_game_prompt(prompt, max_length=100, temperature=0.7):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=max_length, temperature=temperature, num_return_sequences=1)

    generated_prompt = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_prompt

# Example usage
while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    # Generate a video game prompt based on user input
    generated_prompt = generate_video_game_prompt(user_input, max_length=50, temperature=0.7)

    print("Bot:", generated_prompt)
