text = input(str("Please enter a string: "))
count = {}
for char in text:
    if char.isalpha():
        count[char] = count(char, 0) + 1

print(count)
