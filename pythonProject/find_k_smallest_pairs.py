from heapq import heapify, heappop, heappush, nlargest


def find_k_smallest(arr1, arr2, k):
    if len(arr1) == 0 or len(arr2) == 0:
        return []

    min_heap = []

    heapify(min_heap)

    for el1 in arr1:
        for el2 in arr2:

            element = {
                "idx": [el1, el2],
                "val": el1 + el2
            }

            if len(min_heap) < k:
                heappush(min_heap, element)
            elif element["val"] < min_heap[0]["val"]:
                break
            else:
                heappop(min_heap)
                heappush(min_heap, element)

    return [el["val"] for el in nlargest(k, min_heap)]

