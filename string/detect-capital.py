class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True
        if len(word) == 1:
            return True
        if word[0].isupper():
            if word[1:].isupper() or word[1:].islower():
                return True
        if word[0].islower() and word[1:].islower():
            return True
        return False