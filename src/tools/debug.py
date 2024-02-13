import os
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Define the directories
directories = [
    "assets/word lists/",
    "assets/word lists/phonics/",
    "assets/word lists/phonics/consonants/",
    "assets/word lists/phonics/vowels/"
]

# For each directory, get all text files and read their content
for directory in directories:
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as f:
                content = f.read()
                engine.say(content)
                engine.runAndWait()