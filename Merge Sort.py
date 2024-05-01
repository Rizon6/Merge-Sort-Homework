def main():
    array = read_file("numbers-4.txt")
    print(merge_sort(array))

def merge(array_a, array_b):
    array_c = []

    while array_a and array_b:
        if array_a[0] < array_b[0]:
            array_c.append(array_a.pop(0))
        else:
            array_c.append(array_b.pop(0))
    
    while array_a:
        array_c.append(array_a.pop(0))

    while array_b:
        array_c.append(array_b.pop(0))
    return array_c

def merge_sort(array):
    if len(array) == 1:
        return array
    
    mid = len(array) // 2
    array_one = array[:mid]
    array_two = array[mid:]

    array_one = merge_sort(array_one)
    array_two = merge_sort(array_two)

    return merge(array_one, array_two)

def read_file(file):
    array = []
    with open(file, 'r') as file:
        for line in file:
            array.append(int(line))
    return array

main()