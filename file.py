import string
import os

# Characters from 'a' to 'k'
letters = string.ascii_lowercase[
    string.ascii_lowercase.index('a') : string.ascii_lowercase.index('k') + 1
]

for letter in letters:
    for digit in range(1, 9):
        filename = f"u{letter}{digit}.txt"
        with open(filename, "w") as f:
            pass  # creates empty file
