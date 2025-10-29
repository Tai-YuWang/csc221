string = input(str("Please enter a string: ")).lower()

string1 = ''.join([c for c in string if c.isalpha() or c.isspace()])
letter_counts = {}
for char in string:
    if char.isalpha():
        letter_counts[char] = letter_counts.get(char, 0) + 1
    
print(letter_counts)
