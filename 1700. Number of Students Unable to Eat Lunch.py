# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/discuss/1108663/Python-solution


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        sands = {
            'circular': sandwiches.count(0),
            'square': sandwiches.count(1)
        }
        studs = {
            'circular': students.count(0),
            'square': students.count(1)
        }

        # edge case #1 : all sandwhiches are allocated
        if studs['circular'] == sands['circular'] and studs['square'] == studs['square']:
            return 0

        # edge case #2: too many circular sandwiches '0'
        if sands['circular'] > studs['circular']:
            count_index = [index for index, value in enumerate(sandwiches) if value == 0]
            return len(sandwiches) - count_index[studs['circular']]

        # edge case #3: too many square sandwiches '1'
        else:
            count_index = [index for index, value in enumerate(sandwiches) if value == 1]
            return  len(sandwiches) - count_index[studs['square']]
        