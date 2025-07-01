def pair_with_target_sum(arr, sum):
    lp = 0
    rp = len(arr) - 1
    res = arr[lp] + arr[rp]

    while res != sum and lp < rp:
        if res < sum:
            lp+=1
        else:
            rp-=1
        res = arr[lp] + arr[rp]

    return [lp, rp]

print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
print(pair_with_target_sum([2, 5, 9, 11], 11))

def pair_with_target_sum(arr, sum):
    lp = 0
    rp = len(arr) - 1
    res = arr[lp] + arr[rp]

    while res != sum and lp < rp:
        if res < sum:
            lp+=1
        else:
            rp-=1
        res = arr[lp] + arr[rp]

    return [lp, rp]


def pair_with_target_sum(arr, sum):
    lp = 0
    rp = len(arr) - 1
    res = arr[lp] + arr[rp]

    while res != sum and lp < rp:
        if res < sum:
            lp+=1
        else:
            rp-=1
        res = arr[lp] + arr[rp]

    return [lp, rp]


def pair_with_target_sum(arr, sum):
    lp = 0
    rp = len(arr) - 1
    while lp < rp:
        sum_total = arr[lp] + arr[rp]
        if sum_total == sum:
            break
        if sum_total > sum:
            rp -= 1
        else:
            lp += 1
    return [lp, rp]