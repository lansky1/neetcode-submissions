# Attempt 1

from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        skipped_students = 0
        student_queue = deque(students)
        sandwich_queue = deque(sandwiches)

        while skipped_students != len(student_queue):
            if student_queue[0] == sandwich_queue[0]:
                skipped_students = 0
                student_queue.popleft()
                sandwich_queue.popleft()
            else:
                skipped_students += 1
                student_queue.append(student_queue.popleft())

        return len(student_queue)
