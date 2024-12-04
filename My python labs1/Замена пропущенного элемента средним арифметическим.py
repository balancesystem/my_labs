numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
count = len(numbers)
# задача — найти пропущенный элемент
index = numbers.index(None)
# и заменить его средним арифметическим всех остальных элементов списка.
total = sum(numbers[:index] + numbers[index + 1:])
average_of_numbers = total/count
numbers[index] = average_of_numbers

print("Измененный список:", numbers)
