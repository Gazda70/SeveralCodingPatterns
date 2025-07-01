def insert(trie, word):
    for i, char in enumerate(word):
        if char in trie:
            if trie[char][1] or i == len(word) - 1:
                return True
        else:
            trie[char] = {}, i == len(word) - 1
        trie, _ = trie[char]
    return False

def noPrefix(words):
    trie = {}
    # Write your code here
    for word in words:
        if insert(trie, word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")

noPrefix(["aab",
"defgab",
"abcde",
"aabcde",
"cedaaa",
"bbbbbbbbbb",
"jabjjjad"])