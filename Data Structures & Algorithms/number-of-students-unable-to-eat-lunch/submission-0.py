# O(n^2) time complexity

from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        skipped_students = 0
        student_queue = deque(students)
        sandwich_index = 0

        while skipped_students != len(student_queue):
            if student_queue[0] == sandwiches[sandwich_index]:
                skipped_students = 0
                student_queue.popleft()
                sandwich_index += 1
            else:
                skipped_students += 1
                student_queue.append(student_queue.popleft())

        return len(student_queue)
