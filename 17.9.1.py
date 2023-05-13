def sort(array_sort):
    for i in range(1, len(array_sort)):
        x = array_sort[i]
        idx = i
        while idx > 0 and array_sort[idx - 1] > x:
            array_sort[idx] = array_sort[idx - 1]
            idx -= 1
        array_sort[idx] = x
    return array_sort


def binary_search(array, element, left, right):
    if left > right:
        return left

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


again = True
while again:
    try:
        input_array = input("Введите последовательность целых чисел через пробел: ")
        input_number = int(input("Введите целое число: "))
        array_list = list(map(int, input_array.split()))
    except ValueError:
        print("Вы ввели некорректные данные, попробуйте еще раз\n")
    else:
        again = False

sort_list = sort(array_list)
if min(sort_list) < input_number <= max(sort_list):
    findex = binary_search(sort_list, input_number, 0, len(sort_list) - 1)
    print(findex + 1)
else:
    print("Число вне диапозона")


