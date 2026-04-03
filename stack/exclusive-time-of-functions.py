class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        for log in logs:
            task_id, status, time = log.split(":")
            task_id = int(task_id)
            time = int(time)
            if not stack:
                stack.append([task_id, time])
            elif status == "start":
                prev_task_id, prev_start_time = stack.pop()
                stack.append([task_id, time])
                res[prev_task_id] += time - prev_start_time + 1
            elif status == "end":
                _, start_time = stack.pop()
                execution_time = time - start_time + 1
                res[task_id] += execution_time
                if stack:
                    stack[-1][-1] = time + 1
        return res