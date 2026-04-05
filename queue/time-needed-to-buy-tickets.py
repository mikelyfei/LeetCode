class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = []
        for i, ticket in enumerate(tickets):
            queue.append([ticket, i])
        time = 0
        while tickets[k] != 0:
            person, idx = queue.pop(0)
            while person == 0:
                person, idx = queue.pop(0)
            if person > 0:
                person -= 1
                time += 1
                queue.append([person, idx])
                tickets[idx] -= 1
        return time