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


lilysHomework([2, 5, 3, 1])