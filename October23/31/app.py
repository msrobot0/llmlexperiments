def count_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    print("Welcome to the 'In the Beginning Was the Word' program.")
    text = input("Enter a text: ")
    word_count = count_words(text)
    print(f"The text contains {word_count} words.")

