'''
ID: robinhood1

Solution converts courses into a linked list. Searches for starting node (one w/ null prev)
and then scans linked list until reaching mid node

Need to order and prev -> next part of question should have been a giveaway to use linked list
Go over calculating mid
'''

"""
You're developing a system for scheduling advising meetings with students in a Computer Science program. Each meeting should be scheduled when a student has completed 50% of their academic program.

Each course at our university has at most one prerequisite that must be taken first. No two courses share a prerequisite. There is only one path through the program.

Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the student will be taking when they are halfway through their program. (If a track has an even number of courses, and therefore has two "middle" courses, you should return the first one.)

Sample input 1: (arbitrarily ordered)
prereqs_courses1 = [
	["Foundations of Computer Science", "Operating Systems"],
	["Data Structures", "Algorithms"],
	["Computer Networks", "Computer Architecture"],
	["Algorithms", "Foundations of Computer Science"],
	["Computer Architecture", "Data Structures"],
	["Software Design", "Computer Networks"]
]

In this case, the order of the courses in the program is:
	Software Design
	Computer Networks
	Computer Architecture
	Data Structures
	Algorithms
	Foundations of Computer Science
	Operating Systems

Sample output 1:
	"Data Structures"


Sample input 2:
prereqs_courses2 = [
    ["Algorithms", "Foundations of Computer Science"],
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Logic"],
    ["Logic", "Compilers"],
    ["Compilers", "Distributed Systems"],
]


Sample output 2:
	"Foundations of Computer Science"

Sample input 3:
prereqs_courses3 = [
	["Data Structures", "Algorithms"],
]


Sample output 3:
	"Data Structures"

Complexity analysis variables:

n: number of pairs in the input


"""

prereqs_courses1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"],
]

 #  7 course
 # Software Design", "Computer Networks" "Computer Architecture" "Data Structures" "Algorithms" "Foundations of Computer Science" "Operating Systems"

prereqs_courses2 = [
    ["Algorithms", "Foundations of Computer Science"],
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Logic"],
    ["Logic", "Compilers"],
    ["Compilers", "Distributed Systems"],
 ]

 # 6 course
 # "Data Structures", "Algorithms"" "Foundations of Computer Science" "Logic" "Compilers" "Distributed Systems"

prereqs_courses3 = [
    ["Data Structures", "Algorithms"],
]

from collections import defaultdict
from typing import List
import math


class Node:
    def __init__(self, val, p=None, n=None):
        self.val = val
        self.p = p
        self.n = None

def middle_course(pr: List[List[str]]):
    course_node = defaultdict(lambda: False)

    for courses in pr:
        if not course_node[courses[0]]:
            course_node.update({courses[0] : Node(courses[0], None, courses[1])})
        if not course_node[courses[1]]:
            course_node.update({courses[1] : Node(courses[1], courses[0], None)})


        if course_node[courses[0]]:
            course = course_node[courses[0]]
            course.n = course_node[courses[1]]
        if course_node[courses[1]]:
            course = course_node[courses[1]]
            course.p = course_node[courses[0]]

    # get first node

    curr = None

    for course in list(course_node.values()):
        if course.p == None:
            curr = course

    med = math.ceil(len(list(course_node.values())) / 2)

    count = 1

    while count != med:
        curr = curr.n
        count += 1

    return curr.val


'''
def middle_course(pr):
    # find first course
    
    count = defaultdict(lambda: (False, 0))
    course_map = dict()
    
    courses_set = set()
    
    for r in pr:
        count_pr = count[r[0]][0]
        count.update({r[0]: (True, count_pr + 1)})
        count.update({r[1]: (False, count_pr + 1)})
        
        # add to course map
        course_map.update({r[0]: r[1]})
        
        courses_set.add(r[0])
        courses_set.add(r[1])
    
    curr_course = None
    for course in count:
        if count[course][0] and count[course][1] ==1:
            curr_course = course
    
    
            
    count = 1
    stop = len(courses_set) // 2
    
    print(course_map)
    while count != stop:
        curr_course = course_map[curr_course]
        count += 1
    
    return curr_course
'''
    
print(middle_course(prereqs_courses3))
print(middle_course(prereqs_courses2))
print(middle_course(prereqs_courses1))