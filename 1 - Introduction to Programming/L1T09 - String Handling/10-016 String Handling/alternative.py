# Create random string so we can change characters and words into lower and upper case.
emotion = "i feel happy today"

# Create new variable to hold the new string that will be created.
new_emotion = ""

# Use for loop with len function and if statement to calculate to the conversion of every alt character.
for i in range(len(emotion)):

    if i % 2  == 1:
        new_emotion += emotion[i].upper()

    else:
        new_emotion += emotion[i].lower()    

# The new string will be printed.
print(new_emotion)


# Create a new variable to use the split function to split up the words so that we can choose what we want in lower and upper case.
words = emotion.split()

# Use a for loop to convert every alt word to upper case.
for i in range(1, len(words), 2):
        words[i] = words[i].upper()

# Create new variable to use the join function to join the words back into a string
result_emotion = ' '.join(words)
# The new string will be printed.
print(result_emotion)