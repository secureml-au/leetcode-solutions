class Solution:
    def countStudents(self, students, sandwiches):
        count = [0, 0] # count[0] = students who want circular, count[1] = square
        for s in students:
            count[s] += 1

        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
            else:
                break # no student wants this sandwich type

        return count[0] + count[1]