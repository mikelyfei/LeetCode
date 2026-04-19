from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.pos = defaultdict(set)

    def insert(self, val: int) -> bool:
        flag = val in self.pos
        self.nums.append(val)
        self.pos[val].add(len(self.nums) - 1)
        return not flag

    def remove(self, val: int) -> bool:
        if val in self.pos:
            idx = self.pos[val].pop()
            last_val = self.nums[-1]
            last_idx = len(self.nums) - 1
            if last_idx != idx:
                self.nums[idx] = last_val
                self.pos[last_val].remove(last_idx)
                self.pos[last_val].add(idx)
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()