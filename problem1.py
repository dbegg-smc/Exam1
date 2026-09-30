import string
import sys

name=input("What is your name?")
print("Hello " + name + ", how are you today?")

response = input()

def normalize_input(text):
    normalized_text = text.strip()
    normalized_text = normalized_text.translate(str.maketrans('', '', string.punctuation))
    normalized_text = " ".join(normalized_text.split())
    return normalized_text.lower()

normalized = normalize_input(response)
if normalized == "good":
    print("I'm so glad!")
elif normalized == "bad":
    print("I'm so sorry!")
else:
    print(normalized + ", huh?")

proper_name = name.strip().title()
with open("welcome_letter.txt", "w") as f:
    f.write("It was so great to meet you today, " + proper_name + "!")