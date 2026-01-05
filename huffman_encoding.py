import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(char_freq):
    heap = []
    for char, freq in char_freq.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)    # Node with smallest freq
        right = heapq.heappop(heap)   # Node with second smallest freq

        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    root = heap[0]
    
    codes = {}

    def generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:  # Leaf node
            codes[node.char] = current_code
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    return codes

char_freq = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

codes = huffman_encoding(char_freq)

print("Character | Frequency | Huffman Code")
for char in char_freq:
    print(f"{char:^9} | {char_freq[char]:^9} | {codes[char]:^12}")


