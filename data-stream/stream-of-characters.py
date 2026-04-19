class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = []
        self.root = TrieNode()
        self.max_len = 0
        for word in words:
            self.max_len = max(self.max_len, len(word))
            node = root
            for ch in words[::-1]:
                if ch not in node.children:
                    node[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream)>self.max_len:
            self.stream.pop(0)
        node = self.root
        for l in reversed(self.stream):
            if l not in node.children:
                return False
            node = node.children[l]
            if node.is_word:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)