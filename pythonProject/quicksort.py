#Lomuto partitioning scheme
def partition_lomuto(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return arr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


print(partition_lomuto([5, 17, 8, 9, 1, 10], 0, 5))


#Hoare partitioning scheme
def partition_hoare(arr, low, high):
    i = low - 1
    j = high + 1
    pivot = arr[low]
    while True:
        i+=1
        while arr[i] < pivot:
            i+=1
        j-=1
        while arr[j] > pivot:
            j-=1

        if i >= j:
            return j

        swap(arr, i, j)

arr = [10, 7, 18, 19, 1, 5]
n = len(arr)
print(partition_hoare(arr, 0, n - 1))


def lilysHomework(arr):
    # Write your code here
    def num_of_swaps(arr):
        map_of_nums = {}
        for i in range(len(arr)):
            map_of_nums[arr[i]] = i
        sorted_arr = sorted(arr)
        count = 0
        for i in range(len(arr)):
            if sorted_arr[i] != arr[i]:
                count += 1
            swap_index = map_of_nums[sorted_arr[i]]
            map_of_nums[arr[i]] = swap_index
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
        return count
    normal_order = num_of_swaps(arr[::])
    reverse_order = num_of_swaps(arr[::-1])
    return min(normal_order, reverse_order)

lilysHomework([3, 7, 15, 12])