vowels = 'aeiouy'

# Get input from user
word = input("Enter a word for us to count vowels: ")

# Declare 'total' outside of the loop
total = 0 


# for each letter in 'word'
for character in word:
    # print the character
    print(character)

    # if the character exists in the 'aeiou', which is a list of vowels aka a string of vowels
    if character.lower() in vowels:
        total += 1

print(f"There are {total} vowels in {word}")