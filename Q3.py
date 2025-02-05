# Q3
array = []
is_true = True

while is_true:
    new_word = input("Please enter a new word: ")

    for current_word in array:
        if new_word == current_word:
            is_true = False
    else:
        array.append(new_word)

    print(array)

print(f"The word {new_word} already exists in the array...")
