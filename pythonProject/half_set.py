class Solution(object):

    def can_partition_recursive(self, dp, num, sum_total, curr_index):
        if sum_total == 0:
            return True

        if len(num) == 0 or curr_index >= len(num):
            return False

        if num[curr_index] <= sum_total:
            if self.can_partition_recursive(dp, num, sum_total - num[curr_index], curr_index + 1):
                dp[curr_index][sum_total - 1] = True
                return True

        return (dp[curr_index - 1][sum_total - 1] == self.can_partition_recursive(
            dp,
            num,
            sum_total,
            curr_index + 1
        ))

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        sum_total = 0
        N = len(nums)
        for i in range(N):
            sum_total += nums[i]

        if sum_total % 2 != 0:
            return False

        sum_total = int(sum_total / 2.0)
        dp = [[False] * (sum_total + 1) for _ in range(N)]

        for i in range(N):
            dp[i][0] = True

        for s in range(1, sum_total + 1):
            dp[0][s] = nums[0] == s

        for i in range(1, N):
            for s in range(1, sum_total + 1):
                if dp[i-1][s]:
                    dp[i][s] = dp[i-1][s]
                elif s >= nums[i]:
                    dp[i][s] = dp[i - 1][s - nums[i]]

        return dp[N - 1][sum_total]

s = Solution()
print(s.canPartition([1,5,11,5]))