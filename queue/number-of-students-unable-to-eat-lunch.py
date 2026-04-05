class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num = len(sandwiches)
        n = len(students)
        
        for sandwich in sandwiches:
            turn = 0
            stu = students.pop(0)
            while stu != sandwich:
                students.append(stu)
                turn += 1
                if turn == len(students):
                    return num
                stu = students.pop(0)
            num -= 1
        return num