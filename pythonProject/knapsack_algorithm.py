def find_knapsack(profits, weights, capacity):
    def knapsack_recursive(profits, weights, capacity, currIndex):
        if capacity <= 0 or currIndex >= len(weights):
            return 0

        currentProfitWithoutCurrentWeight = 0
        currentProfit = 0

        if weights[currIndex] > capacity:
            currentProfitWithoutCurrentWeight = knapsack_recursive(
                profits,
                weights,
                capacity,
                currIndex + 1
            )
        else:
            currentProfit = knapsack_recursive(
                    profits,
                    weights,
                    capacity - weights[currIndex],
                    currIndex + 1
                ) + profits[currIndex]

        return max(currentProfit, currentProfitWithoutCurrentWeight)

    return knapsack_recursive(profits, weights, capacity, 0)

# find_knapsack([1, 6, 10, 16],
#     [1, 2, 3, 5],
#     7)


def knapsack_recursive(weights, profits, capacity, currIndex):
    if capacity <= 0 or len(weights) == 0 or len(profits) == 0:
        return 0

    profitWithCurrent = 0
    profitWithoutCurrent = 0

    if weights[currIndex] <= capacity:
        profitWithCurrent = knapsack_recursive(
            weights,
            profits,
            capacity - weights[currIndex],
            currIndex + 1
        ) + profits[currIndex]
    profitWithoutCurrent = knapsack_recursive(
        weights,
        profits,
        capacity,
        currIndex + 1
    )

    return max(profitWithCurrent, profitWithoutCurrent)


def knapsack_iterative(weights, profits, capacity, currIndex):
    N = len(weights)
    dp = [[0 for x in range(0, capacity + 1)] for y in range(0, N)]

    for c in range(0, capacity + 1):
        if c <= weights[0]:
            dp[c][0] = 0

    for i in range(0, N):
        dp[0][i] = 0

    for i in range(0, N):
        for c in range(0, capacity + 1):
            if weights[i] <= c:
                dp[c][i] = max(dp[c - weights[i]][i - 1], dp[c][i - 1])
            else:
                dp[c][i] = dp[c][i - 1]

    return dp[N - 1][capacity]

def knapsack_recursive(weights, profits, capacity, currIndex):
    if capacity <= 0 or len(weights) == 0 or len(profits) == 0:
        return 0

    profitWithCurrent = 0
    profitWithoutCurrent = 0

    if weights[currIndex] <= capacity:
        knapsack_recursive(
            weights,
            profits,
            capacity - weights[currIndex],
            currIndex + 1
        ) + profits[currIndex]
    knapsack_recursive(
        weights,
        profits,
        capacity,
        currIndex + 1
    )
    return max(profitWithCurrent, profitWithoutCurrent)

def knapsack_iterative(weights, profits, capacity, currIndex):
    N = len(weights)
    dp = [[0 for x in range(0, capacity + 1)] for y in range(0, N)]

    for c in range(0, capacity + 1):
        if c <= weights[0]:
            dp[c][0] = 0

    for i in range(0, N):
        dp[0][i] = 0

    for i in range(0, N):
        for j in range(0, capacity + 1):
            if weights[i] <= j:
                dp[j][i] = max(dp[j - weights[i]][i - 1], dp[j][i - 1])
            else:
                dp[j][i] = dp[j][i-1]

    return dp[N - 1][capacity]

def subset_sum(nums, sum):
    N = len(nums)

    dp = [[False for _ in range(sum + 1)] for _ in range(N)]

    for w in range(N):
        dp[w][0] = True

    for s in range(1, sum + 1):
        dp[0][s] = nums[0] == s

    for i in range(1, N):
        for j in range(1, sum + 1):
            if dp[i-1][j]:
                dp[i][j] = True
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]
    return dp[N - 1][sum]

def subset_sum_optimised(sum_total, nums):
    dp = [False for _ in range(0, sum_total)]

    dp[0] = True

    for i in range(1, sum_total):
        dp[i] = nums[0] == i

    for i in range(1, len(nums)):
        for s in range(1, sum_total + 1):
            if not dp[s] and s >= nums[i]:
                dp[s] = dp[s - nums[i]]

    return dp[sum_total]

print(subset_sum([1, 2, 3, 4], 6))
print(subset_sum([1, 2, 7, 1, 5], 10))
print(subset_sum([1, 3, 4, 8], 6))

def canPartition(nums):

    def can_partition_recursive(nums, curr_index, sum1, sum2):
        if curr_index == 0:
            return abs(sum1 - sum2)

        diff1 = can_partition_recursive(
            nums,
            curr_index + 1,
            sum1 + nums[curr_index],
            sum2
        )

        diff2 = can_partition_recursive(
            nums,
            curr_index + 1,
            sum1,
            sum2 + nums[curr_index]
        )

        return min(diff1, diff2)

    return can_partition_recursive(nums, 0, 0, 0)

print(canPartition([1, 2, 3, 9]))
def can_partition_with_memoization(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]

    dp = []

    def can_partition_with_memoization_recursive(nums, curr_index, sum1, sum2):
        if curr_index == len(nums):
            return abs(sum1 - sum2)

        diff1 = can_partition_with_memoization_recursive(
            nums,
            curr_index + 1,
            sum1 + nums[curr_index],
            sum2
        )

        diff2 = can_partition_with_memoization_recursive(
            nums,
            curr_index + 1,
            sum1,
            sum2 + nums[curr_index]
        )

        dp[curr_index][sum1] = min(diff1, diff2)

        return dp[curr_index][sum1]

    can_partition_with_memoization_recursive(nums, 0, 0, 0)

print(can_partition_with_memoization([1, 2, 3, 9]))


def knapsack_recursive(weights, profits, capacity, curr_index):
    if capacity == 0 or len(weights) == 0 or len(profits) == 0:
        return 0

    profit_with_curr = 0
    profit_without_curr = 0

    if weights[curr_index] <= capacity:
        profit_with_curr = knapsack_recursive(
            weights,
            profits,
            capacity - weights[curr_index],
            curr_index + 1
        ) + profits[curr_index]

    profit_without_curr = knapsack_recursive(
        weights,
        profits,
        capacity,
        curr_index
    )

    return max(profit_with_curr, profit_without_curr)

def knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_iterative(profits, weights, capacity):
    N = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(N)]

    for i in range(N):
        dp[0][i] = 0

    for j in range(1, capacity + 1):
        if j <= weights[j]:
            dp[j][0] = j

    for i in range(N):
        for c in range(1, capacity + 1):
            if weights[i] <= c:
                dp[c][i] = max(dp[c - weights[i]][i - 1], dp[c][i - 1])
            else:
                dp[c][i] = dp[c][i - 1]

    return dp[capacity][N - 1]

def knapsack_1(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weights, capacity, curr_index):
    if capacity == 0 or len(weights) == 0 or len(profits) == 0:
        return 0
    profit_with_current = 0
    profit_without_current = 0

    if weights[curr_index] <= capacity:
        profit_with_current = knapsack_recursive(
            profits,
            weights,
            capacity - weights[curr_index],
            curr_index + 1
        ) + profits[curr_index]

    profit_without_current = knapsack_recursive(
        profits,
        weights,
        capacity,
        curr_index + 1
    )

    return max(profit_with_current, profit_without_current)

def knapsack_iterative(profits, weights, capacity, curr_index):
    N = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(N)]

    for i in range(N):
        dp[i][0] = 0

    for j in range(1, capacity + 1):
        if j <= weights[0]:
            dp[0][j] = j

    for i in range(N):
        for c in range(1, capacity + 1):
            if weights[i] <= c:
                dp[c][i] = max(dp[c - weights[i]][i-1], dp[c][i-1])
            else:
                dp[c][i] = dp[c][i-1]

    return dp[capacity][N-1]


def knapsack_recursive(profits, weights, capacity, curr_idx):
    if capacity == 0 or len(weights) == 0 or len(profits) == 0:
        return 0

    profitWCurr = 0
    profitWithoutCurr = 0

    if capacity >= weights[curr_idx]:
        profitWCurr = knapsack_recursive(
            profits,
            weights,
            capacity - weights[curr_idx],
            curr_idx + 1
        ) + profits[curr_idx]

    profitWithoutCurr = knapsack_recursive(
            profits,
            weights,
            capacity,
            curr_idx + 1
        )

    return max(profitWCurr, profitWithoutCurr)


def knapsack_iterative(profits, weights, capacity):
    N = len(weights)
    if capacity <= 0 or N == 0 or len(profits) == 0:
        return 0
    dp = [[0 for _ in range(capacity + 1)] for _ in range(N)]
    for c in range(capacity):
        if weights[0] <= c:
            dp[c][0] = profits[0]
    for i in range(N):
        dp[0][i] = 0

    for i in range(1, N):
        for c in range(1, capacity + 1):
            if weights[i] <= c:
                dp[c][i] = max(dp[c - weights[i]][i - 1] + profits[i],
                               dp[c][i - 1])
            else:
                dp[c][i] = dp[c][i - 1]

    return dp[capacity][N - 1]


def knapsack_recursive(profits, weights, capacity, curr_index):
    N = len(weights)

    profitWithCurrent = 0
    profitWithoutCurrent = knapsack_recursive(
        profits,
        weights,
        capacity,
        curr_index + 1
    )

    if weights[curr_index] <= capacity:
        profitWithCurrent = knapsack_recursive(
            profits,
            weights,
            capacity - weights[curr_index],
            curr_index + 1
        ) + profits[curr_index]

    return max(profitWithCurrent, profitWithoutCurrent)


def knapsack_iterative(profits, weights, capacity, curr_index):
    N = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(N)]
    for c in range(1, capacity + 1):
        if c <= weights[0]:
            dp[c][0] = c
    for i in range(N):
        dp[0][i] = 0

    for i in range(N):
        for c in range(1, capacity + 1):
            if weights[i] <= c:
                dp[c][i] = max(dp[c - weights[i]][i-1], dp[c][i-1])
            else:
                dp[c][i] = dp[c][i-1]

    return dp[capacity][N - 1]















