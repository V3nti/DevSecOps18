array = []
is_true = True

while is_true:
    count = 0
    new_word = input("Please enter a new word: ")

    for current_word in array:
        if new_word.upper() == current_word.upper():
            count += 1
        if count == 2:
            is_true = False
    else:
        array.append(new_word)

    print(array)

print(f"The word {new_word} already exists 2 times in the array...")
