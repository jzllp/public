# - task_17.9.1 / Алгоритмы и структуры данных.

# checking input conditions
while True:
    list_of_numbers = input("Enter a sequence of numbers separated by a space: ").split()
    try:
        list_of_numbers_try = [float(x) for x in list_of_numbers]
        break
    except ValueError:
        print("Input Error... Try again!")

while True:
    try:
        any_number = float(input('Enter a random number: '))
        break
    except ValueError:
        print("Input Error... Try again!")

list_of_numbers_try.append(any_number)

list_of_numbers_try.sort()


# find element
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


search_index = binary_search(list_of_numbers_try, any_number, 0, len(list_of_numbers_try) - 1)

if search_index > 0:
    print()
    print('Number index before random number:', search_index - 1, f'|',
          'Number:', list_of_numbers_try[search_index - 1])
else:
    print()
    print('Index before random number not found!')

print('Random number index:', search_index - 0, f'|',
      'Number:', list_of_numbers_try[search_index - 0])

if search_index + 2 > len(list_of_numbers_try):
    print('Index after random number not found!')
else:
    print('Number index after random number:', search_index + 1, f'|',
          'Number:', list_of_numbers_try[search_index + 1])

print()
print('Sorted list of entered numbers:', list_of_numbers_try)
