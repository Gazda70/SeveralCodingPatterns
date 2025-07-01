def average_of_k_elements(arr, k):
    results = []
    slid_sum = 0
    slid_start = 0

    for slid_end in range(len(arr)):
        slid_sum += arr[slid_end]

        if slid_end >= k - 1:
            results.append(slid_sum / k)

            slid_sum -= arr[slid_start]

            slid_start += 1

    return results

print(average_of_k_elements([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))


def average_of_k_elements(arr, k):
    results = []
    slid_sum = 0
    slid_start = 0

    for slid_end in range(len(arr)):
        slid_sum += arr[slid_end]

        if slid_end >= k - 1:
            results.append(slid_sum / k)
            slid_sum -= arr[slid_start]
            slid_start += 1

    return results


def average_of_k_elements(arr, k):
    results = []
    slid_sum = 0
    slid_start = 0

    for slid_end in range(len(arr)):
        slid_sum += arr[slid_end]

        if slid_end >= k - 1:
            results.append(slid_sum / k)
            slid_sum -= arr[slid_start]
            slid_start += 1

    return results