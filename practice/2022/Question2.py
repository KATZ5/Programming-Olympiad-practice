letters = "abcdefghijklmnopqrstuvwxyz"
letters_reversed = letters[::-1]
print(letters_reversed)
input = input()
position = letters_reversed.index(input)
new_string = ""

for letter in range(position, 25, 2):
    new_string = new_string + letters_reversed[letter]
print(new_string)
