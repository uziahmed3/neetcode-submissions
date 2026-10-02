class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        i, j = 0, 0
        while queue:
            student = queue.popleft()

            if student == sandwiches[i]:
                i += 1
                j = 0
            else:
                j += 1
                queue.append(student)
            if j == len(queue):
                return j
        return 0

        