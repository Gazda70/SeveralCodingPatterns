def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] != nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        else:
            i += 1

    return nums

print(cyclic_sort([3, 1, 5, 4, 2]))

def cyclic_sort(array):
    for i in range(len(array)):
        while array[i] != i + 1:
            temp = array[i]
            array[i] = array[array[i] - 1]
            array[temp - 1] = temp
    return array


def cyclic_sort(array):
    for i in range(len(array)):
        while array[i] != i + 1:
            temp = array[i]
            array[i] = array[array[i] - 1]
            array[temp - 1] = temp
    return array

print(cyclic_sort([1, 5, 6, 4, 3, 2]))