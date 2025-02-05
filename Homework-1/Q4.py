array1 = [3, 5, 30, 0]
array2 = [1000, 5, 29, -5]
array1_count = 0
array2_count = 0

for i in range(len(array1)):
    if int(array1[i]) > int(array2[i]):
        array1_count += 1
    elif array1[i] < array2[i]:
        array2_count += 1

if array1_count > array2_count:
    print("First array is bigger")
elif array1_count < array2_count:
    print("second array is bigger")
