'''
Trie (Prefix tree)

Also known as prefix trees, a trie is a tree-based data structure used for efficient storage and retrieval of words or strings. Each node represents a character or symbol, with a pointer to the next character in the word. Each typically also has a marker to indicate whether it represents the tail (last character) of a word (as some words may continue).

By leveraging shared prefixes, redundant characters/nodes are minimised, resulting in efficient storage. It also makes trie operations like prefix search or autocomplete fast. The time complexity of these operations is typically proportional to the length of the input and not dependent on the size of the trie.

Trie structures can be further optimised through techniques like compression or path merging (combining common suffixes).
'''


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_string(self, word: str) -> None:
        nxt = self.root
        for i in word:
            nxt = nxt.add_char(i)
            nxt.freq += 1
        nxt.end_of_key = True

    def search_string(self, string: str) -> bool:
        nxt2 = self.root
        for i in string:
            if i not in nxt2.nodes:
                return False
            nxt2 = nxt2.nodes[i]
        return nxt2.end_of_key

    def count_prefix(self, prefix: str) -> int:
        nxt = self.root
        for i in prefix:
            if i not in nxt.nodes:
                return 0
            nxt = nxt.nodes[i]
        return nxt.freq


class TrieNode:

    def __init__(self):
        self.nodes = {}
        self.end_of_key = False
        self.freq = 0

    def add_char(self, c: chr):
        if c not in self.nodes:
            self.nodes[c] = TrieNode()
        return self.nodes[c]


trie = Trie()

words = ["AMBER", "ALICE", "AMPLE", "BALLOON", "BALL", "BLAST", "BAND", "DENSE", "DUTCH", "DECK", "DANCE", "DRAMA", "MESS",
         "MAVERICK", "MAVEN", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PEAK", "PACK", "ZEST", "ZEAL", "ZAP", "ZIP", "ZIPPER"]

for word in words:
    trie.add_string(word)

more_words = ["APPLE", "AMPLIFIER", "AMPLE", "BALLOON", "BALL", "DART", "DUTCH", "DECK", "DRAM", "FLAG", "MOP",
              "MAVERICK", "MANSION", "PHYSICS", "PHONE", "PHANTOM", "PASS", "PECK", "PAIN", "ZAM", "ZEST", "ZAP", "ZIP", "ZEBRA"]

for word in more_words:
    if trie.search_string(word):
        print(word)

prefixes = ["A", "AM", "B", "BALL", "BA", "C", "CA" "DUTCH",
            "DECK", "GA", "J", "MA", "P", "PH", "PE", "Z", "ZIP"]

for prefix in prefixes:
    print(trie.count_prefix(prefix))
