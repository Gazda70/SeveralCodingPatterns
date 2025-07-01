# Python program for Huffman Coding
import heapq

class Node:
    def __init__(self, info=None, freq=0, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(chars, freq):
    priority_queue = [Node(info=c, freq=f) for c, f in zip(chars, freq)]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = Node(info='', freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]


def generate_huffman_codes(root, code="", huffman_codes = {}):
    if root is not None:
        if root.info == '':
            generate_huffman_codes(root.left, code + "0", huffman_codes)
            generate_huffman_codes(root.right, code + "1", huffman_codes)
        else:
            huffman_codes[root.info] = code
        return huffman_codes


# Given example
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [4, 7, 15, 17, 22, 42]

# Build the Huffman tree
root = build_huffman_tree(chars, freq)

# Generate Huffman codes
huffman_codes = generate_huffman_codes(root)

# Print Huffman codes
for char, code in huffman_codes.items():
    print(f"Character: {char}, Code: {code}")