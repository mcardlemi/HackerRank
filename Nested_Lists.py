"""
Overly complicated attempt at using classes instead of an array matrix
"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __lt__(self, other):
        if float(self.grade) > float(other.grade):
            return 0
        else:
            return 1
    
    def __str__(self):
        return self.name+ ", " + str(self.grade)

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
    classList = []
    for _ in range(int(input())):
        classList.append(Student(input(), input()))
    classList.sort()
    matchingGrade(classList, secondLow(classList, 0))
