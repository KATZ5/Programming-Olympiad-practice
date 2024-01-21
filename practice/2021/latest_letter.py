def new_func(x):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_value = 0
    for i in user_input:
        if letters.index(i) > letter_value:
            letter_value = letters.index(i)
    return letters[letter_value]

user_input = input().upper()
result  = new_func(user_input)
print(result)