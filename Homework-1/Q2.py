# Q2
loop = 0
sum = 0

while True:
    loop += 1
    number = input(f"Loop number {loop}, please enter a number: ")
    number = int(number)

    if number < 0:
        break

    sum += number
    print(f"The sum is now {sum}.\n")

print("Thank you, goodbye")
