import random
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            idx = self.pos[val]
            self.nums[idx] = self.nums[-1]
            self.pos[self.nums[idx]] = idx
            self.nums.pop()
            del self.pos[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()