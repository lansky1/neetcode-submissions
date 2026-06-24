"""
Approach: Using Two Deque
"""

from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwich_queue = deque(sandwiches)
        student_queue = deque(students)
        distance_of_unhappy_student = -1

        while len(student_queue) > 0 and distance_of_unhappy_student != len(student_queue):
            if student_queue[0] == sandwich_queue[0]:
                student_queue.popleft()
                sandwich_queue.popleft()
                distance_of_unhappy_student = -1
            else:
                student_queue.rotate(-1)
                distance_of_unhappy_student += 1

        return len(student_queue)
