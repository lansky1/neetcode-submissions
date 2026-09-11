# Took hint

from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = [0,0]

        for student in students:
            student_count[student]+=1

        for sandwich in sandwiches:
            if student_count[sandwich] == 0:
                break

            student_count[sandwich]-=1

        return sum(student_count)