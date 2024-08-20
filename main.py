import time
import random
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language.",
    "ChatGPT helps people with their coding problems.",
    "Typing fast requires practice and dedication.",
    "Consistency is the key to improvement."
]
def get_random_sentence(sentences):
    return random.choice(sentences)
def typing_speed_test():
    sentence = get_random_sentence(sentences)
    print("Type the following sentence:")
    print(sentence)
    print()
    # Start the timer
    start_time = time.time()
    # Get user input
    user_input = input("Your input: ")
    # End the timer
    end_time = time.time()
    # Calculate time taken
    time_taken = end_time - start_time
    # Calculate words per minute (WPM)
    word_count = len(sentence.split())
    wpm = (word_count / time_taken) * 60
    # Calculate accuracy
    correct_chars = 0
    for i in range(min(len(sentence), len(user_input))):
        if sentence[i] == user_input[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(sentence)) * 100
    # Display results
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
if __name__ == "__main__":
    typing_speed_test()
