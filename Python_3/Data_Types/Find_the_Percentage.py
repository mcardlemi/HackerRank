""" 
The student class is building. Not cleanly, on more practice I would refine this. 
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.averageGrade = self.average()
    
    def __lt__(self, other): 
    # thinking a default , sort="Grade", with conditional if for sorting types. 
    # need to look up restricted input formats [grade[0], name, averageGrade]
    # needs to then implement sort() with possible parameters. also understand that function more
        if float(self.averageGrade) > float(other.averageGrade):
            return 0
        else:
            return 1
    
    def __str__(self):
        return self.name+ ", " + str(self.grade)
    
    def average(self):
        y = 0
        for i in range(len(self.grade)):
            y+= self.grade[i]
        return y/len(self.grade)
        
    def matchName(self, search):
        if self.name == search:
            return 1
        else:
            return 0


def searchNames(arr, search, p=0):
    if arr[p].matchName(search):
        return p
    else:
        return searchNames(arr, search, p+1)

def secondLow(arr, p):
    if arr[0].grade == arr[p].grade:
        return secondLow(arr, p+1)
    else:
        return arr[p].grade
        
def matchingGrade(arr, toMatch):
    names= []
    for i in range(len(arr)):
        if arr[i].grade == toMatch:
            names.append(arr[i].name)
    names.sort()                            #lame Alphabetical
    for i in range(len(names)):
        print(names[i])
    return None

if __name__ == '__main__':
    n = int(input())
    roster = []
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        roster.append(Student(name, scores))
    query_name = input()
    print(format(roster[searchNames(roster, query_name)].averageGrade, ".2f"))
    
