#Q] Write a Program to implement Regular Expression?
import re
# Sample text
text = "Hello World! Today is 06th January 2025."
# 1. Check if the text contains the word 'World'
if re.search(r"World", text):
 print("The word 'World' is found in the text!")
else:
 print("The word 'World' is not found in the text.")
# 2. Extract all numbers from the text
numbers = re.findall(r"\d+", text)
print("Extracted Numbers:", numbers)
# 3. Replace the word 'Hello' with 'Hi'
updated_text = re.sub(r"Hello", "Hi", text)
print("Updated Text:", updated_text)
# 4. Split the text by spaces
words = re.split(r"\s+", text)
print("Split Words:", words)
