'''
******************* PROBLEM STATEMENT

******************* NOTES
PYTHON CONCEPTS TO GO OVER:
    1. get vs index of object
    2. nonlocal
    3. deque

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* SOLUTION
'''

from collections import defaultdict
from typing import List


class Solution:
    class Course:
        def __init__(self, id: int = None):
            self.course_id = id
            self.pr = [] # NOTE: Misnomer should have named it requirements
            self.incoming = 0

    def DFS(self, course: Course, seen: List, added: List, ordered_list: List, prereq):
        #if added[course.course_id]:
            #return True
        if seen[course.course_id]:
            return False  # Can catch and terminate

        seen[course.course_id] = True
        to_continue = False
        for pr_id in course.pr:
            pr = prereq[pr_id]
            pr.incoming -= 1
            if pr.incoming == 0:
                ordered_list.append(pr.course_id)
                added[pr.course_id] = True
            to_continue = self.DFS(pr, seen, added, ordered_list, prereq)
            if not to_continue:
                break
            else:
                to_continue = True

        seen[course.course_id] = False
        return to_continue


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create dict of pre-reqs
        prereq = defaultdict(self.Course)

        for req in prerequisites:
            course = self.Course(req[0])
            prereq.update({req[0]: course})
            course.incoming += 1

            course = self.Course(req[1])
            prereq.update({req[1]: course})
            course.pr.append(req[0])


        # create ordered list
        ordered_list = []
        seen = [False] * numCourses  # if not used to catch can eliminate
        added = [False] * numCourses # NOTE: How to do list mathematics
        to_visit = [] # NOTE: Instead of adding course objects here could add keys that map to courses

        for id in range(numCourses):
            course = prereq[id]
            if course.incoming == 0:
                course.course_id = id
                prereq.update({id: course})
                to_visit.append(course)
                ordered_list.append(course.course_id)
                added[id] = True

        while len(to_visit) > 0:
            for index, course in enumerate(to_visit):  # TODO: Does enumerate work here?
                if not seen[index]:
                    to_continue = self.DFS(course, seen, added, ordered_list, prereq)
                    #if not to_continue: # There is a bug w/ to_continue
                        #break
                to_visit.pop(0)

        if len(ordered_list) == numCourses:
            return ordered_list

        return []

if __name__ == '__main__':
    sol = Solution()
    assert sol.findOrder(2, [[1,0]]) == [0,1]
    assert sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
