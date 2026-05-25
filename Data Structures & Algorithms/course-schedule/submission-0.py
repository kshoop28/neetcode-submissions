class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []   

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visiting = set()

    # DFS helper function
        def dfs(course):
            if course in visiting:
                return False

            #base case if there are no prequiste, continue
            #no need to dive more into it
            if len(preMap[course]) == 0:
                return True
            
            # ok so if there is a prequisite
            # add it to the visiting set
            visiting.add(course)

            #loop through preq and call dfs on it
            for prereq in preMap[course]:
                can_finish = dfs(prereq)
                if not can_finish:
                    return False 

            #if the dfs loop passes then remove preq 
            # remove from visitng and continue
            # dfs(preq) == good
            visiting.remove(course)
            preMap[course] = []  
            return True

        for c in range(numCourses):
            can_finish = dfs(c)
            if not can_finish:
                return False
# in the end all the preq should be empty
# example: 0:[], 1:[]...
        return True
'''
Build a graph mapping each course to its prerequisites.

Use DFS: if you revisit a course in the current path → cycle → return False.

If all DFS calls finish safely → return True (no cycles).
'''