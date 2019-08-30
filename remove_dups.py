# Given a list of numbers or strings, create a new list containing
# the same elements as the first list, except with any duplicate
# values removed.  Print the list.

numbers = [1, 3, 5, 7, 9, 9, 2, 4]
uniqueNumbers = []

for number in numbers:
    if number not in uniqueNumbers:
        uniqueNumbers.append(number)

strings = ["The", "Empire", "Strikes", "Back", "Revenge", "Of", "The", "Sith"]
uniqueStrings = []

for string in strings:
    if string not in uniqueStrings:
        uniqueStrings.append(string)

print(f"Original List of Numbers: {numbers} | Unique List of Numbers: {uniqueNumbers}")
print(f"Original List of Strings: {strings} | Unique List of Strings: {uniqueStrings}")