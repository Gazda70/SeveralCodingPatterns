# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from heapq import heapify, heappop, heappush


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    result = nums1 + nums2
    min_heap = []
    max_heap = []

    heapify(min_heap)
    heapify(max_heap)

    for el in result:
        if len(max_heap) > 0 and el > max_heap[0] * -1:
            heappush(min_heap, el)
        else:
            heappush(max_heap, -1 * el)
        if len(max_heap) > len(min_heap) + 1:
            ov = heappop(max_heap)
            heappush(min_heap, ov)
        if len(min_heap) > len(max_heap) + 1:
            ov = heappop(min_heap)
            heappush(max_heap, -1 * ov)

    if len(result) % 2 != 0:
        return heappop(min_heap)
    else:
        return (heappop(min_heap) + heappop(max_heap) * -1) / 2


findMedianSortedArrays([1,2], [3,4])

import math

def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    height = len(matrix)
    width = len(matrix[0])
    start = matrix[0][0]
    end = matrix[height - 1][width - 1]

    while start < end:
        mid = math.floor(start + (end - start) / 2)

        count, smaller, larger = countLessEqual(
            matrix,
            mid,
            matrix[0][0],
            matrix[height - 1][width - 1],
            height
        )
        if count == k:
            return smaller
        if count < k:
            start = larger
        else:
            end = smaller
    return start

def countLessEqual(matrix, mid, smaller, larger, height):
    count = 0
    n = len(matrix)
    row = height - 1
    col = 0

    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger

kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)

class MinHeap:
    def __init__(self):
        self.list = []  # a list of [num, groupID]
        self.size = 0

    def push(self, item):
        self.list.append(item)
        self.size += 1
        self.bubble_up(self.size - 1)

    def pop(self):
        if self.size == 0:
            return None

        item = self.list[0]
        self.list[0], self.list[self.size - 1] = self.list[self.size - 1], self.list[0]
        self.size -= 1
        self.list.pop()  # remove the last item
        self.bubble_down(0)
        return item

    def bubble_up(self, index):
        parent = (index - 1) // 2

        if parent < 0 or parent >= self.size:
            return

        if self.list[index][0] < self.list[parent][0]:
            self.list[index], self.list[parent] = self.list[parent], self.list[index]
            self.bubble_up(parent)

    def bubble_down(self, index):
        if index < 0 or index >= self.size:
            return

        left = index * 2 + 1
        right = index * 2 + 2
        min_index = index

        if left < self.size and self.list[left][0] < self.list[min_index][0]:
            min_index = left
        if right < self.size and self.list[right][0] < self.list[min_index][0]:
            min_index = right

        if min_index != index:
            self.list[index], self.list[min_index] = self.list[min_index], self.list[index]
            self.bubble_down(min_index)


def smallestRange(nums):
    min_heap = MinHeap()
    pointers = [0] * len(nums)
    range_start = 0
    range_end = float("inf")
    max_number = float("-inf")

    for i in range(0, len(nums)):
        min_heap.push([nums[i][0], i])
        max_number = max(max_number, nums[i][0])

    while(True):
        min_number, group = min_heap.pop()

        if max_number - min_number < range_end - range_start:
            range_start = min_number
            range_end = max_number

        pointers[group] += 1

        if pointers[group] >= len(nums[group]): break

        min_heap.push([nums[group][pointers[group]], group])
        max_number = max(max_number, nums[group][pointers[group]])

    return range_start, range_end

smallestRange([
  [4, 10, 15, 24, 26],
  [0, 9, 12, 20],
  [5, 18, 22, 30],
])

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def partition(nums, start, end, pivot_idx):
    if start == end:
        return start
    pivot = nums[end]
    for j in range(start, end):
        if nums[j] < pivot:
            swap(nums, start, j)
            start += 1
    swap(nums, start, end)

    return start

def findKthSmallestNumber_rec(nums, k, start, end):
    pivot_idx = math.floor(start + (end - start) / 2)
    pivot_idx = partition(nums, start, end, pivot_idx)

    if pivot_idx == k - 1: return nums[pivot_idx]

    if pivot_idx < k - 1:
        return findKthSmallestNumber_rec(nums, k, start, pivot_idx - 1)
    else:
        return findKthSmallestNumber_rec(nums, k, pivot_idx - 1, end)

def findKthSmallestNumber(nums, k):
    return findKthSmallestNumber_rec(nums, k, 0, len(nums) - 1)

print(findKthSmallestNumber([1, 5, 12, 2, 11, 5], 3))